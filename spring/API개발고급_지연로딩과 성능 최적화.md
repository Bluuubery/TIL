## 지연 로딩과 성능 최적화

### 주문조회1: 엔티티 직접 노출

```java

    @GetMapping("/api/v1/simple-orders")
    public List<Order> ordersV1() {
        List<Order> all = orderRepository.findAllByString(new OrderSearch());
        for (Order order : all) {
            order.getMember().getName(); //Lazy 강제 초기화
            order.getDelivery().getAddress(); //Lazy 강제 초기화
        }
        return all;
    }

```

✔ **엔티티 직접 노출 지양**

✔ `order -> member` 와 `order -> address` 는 지연 로딩이다. 따라서 실제 엔티티 대신에 프록시 존재

✔ 양방향 관계는 `@Jsonignore` 설정을 해준다.
 - 서로 호출하면서 무한 루프

```java
// Member.java

@Entity
@Getter @Setter
public class Member {

    ...

    @JsonIgnore
    @OneToMany(mappedBy = "member")
    private List<Order> orders = new ArrayList<>();

}
```

### 하이버네이트 모듈 등록 (spring 3.0 미만)

✔ `jackson` 라이브러리는 기본적으로 이 프록시 객체를 json으로 어떻게 생성해야 하는지 모름 예외 발생

✔ `Hibernate5Module` 을 스프링 빈으로 등록

1. build gradle에 의존성 추가
   `implementation 'com.fasterxml.jackson.datatype:jackson-datatype-hibernate5'`

2. `JpashopApplication` 에 다음 코드를 추가
    ```java
    @Bean
    Hibernate5Module hibernate5Module() {
        return new Hibernate5Module();
    }
    ```

## 주문조회 2: 엔티티를 DTO로 변환

```java

    /**
     * V2. 엔티티를 조회해서 DTO로 변환(fetch join 사용X)
     * - 단점: 지연로딩으로 쿼리 N번 호출
     */
    @GetMapping("/api/v2/simple-orders")
    public List<SimpleOrderDto> ordersV2() {
        List<Order> orders = orderRepository.findAll();
        List<SimpleOrderDto> result = orders.stream()
                .map(o -> new SimpleOrderDto(o))
                .collect(toList());

        return result;
    }

    ...

    @Data
    static class SimpleOrderDto {

        private Long orderId;
        private String name;
        private LocalDateTime orderDate; //주문시간
        private OrderStatus orderStatus;
        private Address address;

        public SimpleOrderDto(Order order) {
            orderId = order.getId();
            name = order.getMember().getName();
            orderDate = order.getOrderDate();
            orderStatus = order.getStatus();
            address = order.getDelivery().getAddress();
        }
    }
```

✔ **엔티티를 DTO로 변환하는 일반적인 방법**

✔ 쿼리 1 + N + N번 실행 (N + 1 문제)
- order 조회 1번
- order -> member 지연 로딩 조회 N 번
- order -> delivery 지연 로딩 조회 N 번

## 주문조회3: 엔티티를 DTO로 변환 - 페치 조인 최적화

```java

    /**
     * V3. 엔티티를 조회해서 DTO로 변환(fetch join 사용O)
     * - fetch join으로 쿼리 1번 호출
     */
    @GetMapping("/api/v3/simple-orders")
    public List<SimpleOrderDto> ordersV3() {
        List<Order> orders = orderRepository.findAllWithMemberDelivery();
        List<SimpleOrderDto> result = orders.stream()
                .map(o -> new SimpleOrderDto(o))
                .collect(toList());
        return result;
    }
```

```java
// OrderRepository.java

    public List<Order> findAllWithMemberDelivery() {
        return em.createQuery(
                "select o from Order o" +
                        " join fetch o.member m" +
                        " join fetch o.delivery d", Order.class)
                .getResultList();
    }
```

✔ **엔티티를 페치 조인(fetch join)을 사용해서 쿼리 1번에 조회**

✔ 페치 조인으로 order -> member , order -> delivery 는 이미 조회 된 상태 이므로 지연로딩X

## 주문조회 4: JPA에서 DTO로 바로 조회

```java

    @GetMapping("/api/v4/simple-orders")
    public List<OrderSimpleQueryDto> ordersV4() {
        return orderSimpleQueryRepository.findOrderDtos();
    }
```

```java
// OrderSimpleQueryRepository.java

package jpabook.jpashop.repository.order.simplequery;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class OrderSimpleQueryRepository {

    private final EntityManager em;

    public List<OrderSimpleQueryDto> findOrderDtos() {
        return em.createQuery(
                "select new jpabook.jpashop.repository.order.simplequery.OrderSimpleQueryDto(o.id, m.name, o.orderDate, o.status, d.address)" +
                        " from Order o" +
                        " join o.member m" +
                        " join o.delivery d", OrderSimpleQueryDto.class)
                .getResultList();
    }
}
```

```java
// OrderSimpleQueryDto.java

package jpabook.jpashop.repository.order.simplequery;

import jpabook.jpashop.domain.Address;
import jpabook.jpashop.domain.OrderStatus;
import lombok.Data;

import java.time.LocalDateTime;

@Data
public class OrderSimpleQueryDto {

    private Long orderId;
    private String name;
    private LocalDateTime orderDate; //주문시간
    private OrderStatus orderStatus;
    private Address address;

    public OrderSimpleQueryDto(Long orderId, String name, LocalDateTime orderDate, OrderStatus orderStatus, Address address) {
        this.orderId = orderId;
        this.name = name;
        this.orderDate = orderDate;
        this.orderStatus = orderStatus;
        this.address = address;
    }
}
```

✔ **일반적인 SQL을 사용할 때처럼 원하는 값 선택해서 조회**

✔ new 명령어를 사용해서 JPQL의 결과를 DTO로 즉시 변환

✔ SELECT 절에서 원하는 데이터를 직접 선택하므로 DB 애플리케이션 네트웍 용량 최적화(생각보다 크진 않다)

✔ 리포지토리 재사용성 떨어짐, API 스펙에 맞춘 코드가 리포지토리에 들어가는 단점

## 정리

✔ **쿼리 방식 선택 권장 순서**

1. 우선 엔티티를 DTO로 변환하는 방법을 선택한
2. 필요하면 페치 조인으로 성능 최적화. (대부분의 성능 이슈가 해결됨)
3. 그래도 안되면 DTO로 직접 조회하는 방법을 사용
4. 최후의 방법은 JPA가 제공하는 네이티브 SQL이나 스프링 JDBC Template을 사용해서 SQL을 직접 사용