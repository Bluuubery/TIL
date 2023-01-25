## Jenkins 프로젝트 생성 및 CI/CD 구축


1. Jenkins 메인화면에서 '새로운 item' 클릭
2. 이름 작성 및 Freestyle project 선택 후 OK
3. 소스 코드 관리 > Git 선택
4. 빌드 유발 > Build when a change is pushed to Gitlab. 선택 & Secret token > Generate 선택 후 key 복사
5. Build Steps > Execute shell 선택
6. 프로젝트 루트 폴더로 이동 후 Dockerfile 실행하는 쉘 스크립트 작성

```shell
# 프로젝트 루트로 이동이 필요한 경우
cd ${PROJECT_ROOT}

docker build -t ${CONTAINER_NAME} .
docker run -d -p 포트번호:포트번호 ${CONTAINER_NAME} 
```   


7. 빌드 후 조치 > Publish build status to GitLab 선택
8. 맨 아래 저장 버튼 클릭
9. GitLab에서 좌측 Settings > Webhooks
10.   4번에 있는 webhook URL을 URL에 입력하고 복사해 둔 Secret token을 입력
11.   프로젝트에 맞는 Trigger 설정 후 Add webhook 클릭
12.   하단 Project Hooks에서 원하는 Trigger를 유발하여 테스트 가능

