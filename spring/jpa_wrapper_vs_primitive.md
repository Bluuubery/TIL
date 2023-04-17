# JPA에서 엔티티를 생성할 때 Wrapper class를 사용해야할까 primitive type을 사용해야할까?

```java
@Entity
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String name;    
                            
    private int stock; // Integer? int?
}

```

## 1. primitive type & Wrapper Class

### 원시 타입(primitive type)

✔ Java에서 기본으로 제공되는 데이터 타입

✔ int, byte, short, long, float, double, boolean, char 

✔ 장점
- 메모리 사용량이 적다. (스택 영역에 바로 생성)
- 성능이 좋다.

✔ 단점
- **⭐null 값을 허용하지 않는다. (NPE 발생)**


### 래퍼 클래스(wrapper 클래스)

✔ 원시 타입을 객체로 감싸서 사용할 수 있도록 해주는 클래스

✔ Integer, Long, Float, Double, Boolean 등

✔ 장점
- **⭐null 값을 허용한다**
- 다양한 메서드를 제공한다

✔ 단점
- 메모리 사용량이 크다
- 성능이 다소 떨어진다(박싱, 언박싱)


## 2. JPA에서는 뭘 사용해야될까?

![](assets/jpa_wrapper_vs_primitive.md/2023-04-17-17-39-39.png)

✔ JPA에서는 일반적으로 Wrapper 클래스를 사용하는 것이 권장되고 Hibernates의 공식 문서에서는 특히 ID의 경우에 Nullable한 자료형(Wrapper)를 사용할 것을 권장하고 있다

✔ 가장 큰 이유는 db에서 Null값 허용을 통해서 얻는 이점이 크다는 것이다.

✔ 또한 박싱/언박싱이나, 메모리 사용량 등 성능상의 단점 역시 컴퓨팅 성능의 향상으로 인해 큰 영향을 미치지 않을 정도가 되었다.

### 

1. **NULL 값 허용**: Wrapper Class는 NULL 값을 허용하므로, 데이터베이스의 해당 컬럼이 NULL 값을 가질 수 있는 경우 Wrapper Class를 사용하는 것이 적절하다

2. **Optional을 통한 안전한 NULL 처리**: JPA는 `Optional`을 통한 Null 값 처리를 적극적으로 지원하므로 primitive type에서 NPE가 아닌 서비스에 맞게 null 값을 적절하게 처리할 수 있다.

```java
public interface ProductRepository extends JpaRepository<Product, Long> {
    Optional<Product> findById(Long id);
}

@Service
public class ProductService {
    private final ProductRepository productRepository;

    public ProductService(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    // optional을 활용해 상황에 맞게 에러를 처리할 수 있다.
    public Product getProductById(Long id) {
        return productRepository.findById(id)
                .orElseThrow(() -> new ProductNotFoundException("Product not found with id: " + id));
    }
}

```

## 결론

✔ 일반적인 상황에서는 **Null 값 허용**이 가져오는 이점이 커서 Wrapper 클래스를 사용하는 것이 유리하다. 

✔ 그러나 성능이 특히 중요하며, db에서 해당 속성에 대해 항상 값이 존재함이 보장될 경우 primitive type을 사용하는 것이 유리할 수도 있다.
