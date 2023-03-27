# Springboot Dockerfile & docker-compose.yml


## Dockerfile

```docker
# 스테이지 1 (빌더)

# 베이스 이미지: jdk 11 alpine(경량)
FROM adoptopenjdk/openjdk11:jdk-11.0.10_9-alpine AS builder
# 작업 경로 설정 및 프로젝트 가져오기
WORKDIR /app
COPY . .

# 빌드 권한 부여 및 실행(클린)
RUN chmod +x ./gradlew
RUN ./gradlew clean bootJar

# 스테이지 2

# 베이스 이미지: jdk 11 alpine(경량)
FROM adoptopenjdk/openjdk11:jdk-11.0.10_9-alpine
# 빌더 스테이지에서 빌드한 jar 파일 가져오기
COPY --from=builder /app/build/libs/*.jar app.jar

# 8080포트로 실행
EXPOSE 8080
ENTRYPOINT ["java", "-jar","/app.jar"]

```

✔ `./gradlew`를 활용한 멀티스테이지 빌드로 큰 특이 사항은 없다

### CMD vs ENTRYPOINT

✔ 둘 다 빌드 후 컨테이너 최소 실행 단계에서 실행되는 명령어라는 점에서는 동일하다

✔ `ENTRYPOINT`같은 경우에는 항상 실행되는 반면 `CMD`의 경우는 도커 실행 시 명령어로 변경이 가능하다

✔ 꼭 실행되어야되는 명령어의 경우에는 `ENTRYPOINT`를 활용하자

## docker-compose.yml

```yaml
version: "3.7"

services:
  springboot:
    container_name: springboot
    build:
      context: .
      dockerfile: ./Dockerfile
    ports:
      - "8080:8080"
    environment:
      SERVER_MODE: prod
      AWS_ACCESS_KEY: "${AWS_ACCESS_KEY}"
      AWS_SECRET_KEY: "${AWS_SECRET_KEY}"
      JWT_SECRET_KEY: "${JWT_SECRET_KEY}"
```

✔ environment를 통해서 환경변수를 쉽게 설정해줄 수 있다