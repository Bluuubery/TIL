# 에러: `./gradelw not found error`

## 문제

![](assets/gradlew%20notfound%20error.md/2023-03-20-21-17-13.png)

도커로 springboot 프로젝트 빌드 중에 발생한 에러

./gradlew 파일이 분명히 있는데 없다고 한다 

## 원인

✔ 원인은 **윈도우와 리눅스의 개행방식의 차이**다

윈도우의 경우 CRLF(`\r\n`)을 쓰고 리눅스의 경우 LF(`\n`)을 쓰기 떄문에 윈도우에서 작성한 파일이 리눅스에서 제대로 인식이 안되거나 그 반대의 경우가 종종 발생하게 된다.

위의 사례 역시 윈도우 환경에서 스프링 프로젝트를 생성한 파일을 리눅스 환경에서 돌아가는 docker에서 읽지 못해서 발생했기 때문이다.

## 해결

✔ 개행을 리눅스 방식으로 바꿔주면된다.

`dos2unix` 라는 패키지를 활용하면 간편하다

```shell
# choco는 윈도우에서 쓰이는 패키지 관리자(chocolatey)의 명령어다
# 본인 환경에 맞는 패키지 매니저를 쓰면 된다.
choco install dos2unix

dos2unix ./gradlew
```

![](assets/gradlew%20notfound%20error.md/2023-03-20-21-30-26.png)

패키지를 설치하고 명령어를 정상적으로 입력했으면 다음과 같이 파일이 잘 변환된다.

![](assets/gradlew%20notfound%20error.md/2023-03-20-21-31-00.png)

이후 다시 빌드를 해보면 정상적으로 동작하는 것을 확인할 수 있다.