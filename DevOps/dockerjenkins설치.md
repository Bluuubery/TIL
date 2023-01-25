# Jenkins 안에 Docker 설치하기

## 1. 도커 설치

✔ 패키지들이 최신 버전인지 확인

```shell
sudo apt-get update && upgrade
```

✔ apt가 HTTPS를 통해 repository를 이용하는 것을 허용할 수 있도록 해주는 패키지들 설치

```shell
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

✔ docker 공식 GPG key 추가

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

✔ docker repository를 등록

```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

✔ docker 설치

```shell
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## 2. Jenkins 설치


✔ Jenkins 설치 및 컨테이너 구동

```shell
docker run -u 0 -d -p 9090:8080 -p 50000:50000 -v /var/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins jenkins/jenkins:lts
```


※ docker 설치 후 /var/run/docker.sock permission denied가 발생하는 경우

```shell
sudo chmod 666 /var/run/docker.sock
```

9090 포트 접속  
docker logs jenkins 입력 후 비밀번호 입력  
DashBoard > Manager Jenkins > Plugin Manager에서 gitlab, docker 검색 후 각각 상위 4개 항목 설치  

## 3. Jenkins 컨테이너 안 도커 설치

✔ Jenkins 컨테이너 접속

```shell
docker exec -it jenkins /bin/bash
```

✔ docker old version 제거

```shell
apt-get remove docker docker-engine docker.io containerd runc
```

✔ 다음 명령어 차례로 입력

```shell
apt-get update
```

```shell
apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

```shell
mkdir -p /etc/apt/keyrings
```

```shell
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```shell
apt-get update
```

```shell
apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```