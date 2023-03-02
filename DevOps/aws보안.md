# 정보 보호 보안

## 정보 보호 보안의 개념

정보의 수집, 가공, 저장, 검색, 송신 중에 정보의 훼손, 변조, 유출 등을 방지하기 위한 관리적, 기술적 수단 또는 그러한 수단으로 이루어지는 행위

### 기업에서 정보 보호의 대상

✔ 출입하는 모든 사람 + 유무형의 정보 자산

### 정보 보호 대책

1. 관리적 보호 대책: 제도, 보안 교육, 훈련, 보안 직무
2. 물리적 보호 대책: 출입통제, 재난 방지
3. 기술적 보호 대책: 네트워크 접근 통제, 보안 소프트웨어, 방화벽

## 사이트 보안

✔ 파일 업로드 취약점

✔ XSS (Cross Site Scripting)

✔ SQL Injection

### 파일 업로드 취약점

✔ 게시판 등의 첨부 파일 기능을 이용해 허가 되지 않은 파일들을 웹서버로 업로드 할 수 있는 취약점 (php, jsp, asp, cji, ji, py 등)

```
httpd.conf
<Directory "/usr/local/apache">
AllowOverride FileInfo
</Directory>
```

```
.htaccess
<FilesMatch "\.(ph|inc|lib)">
 Order allow, deny
  Deny from all
</FilesMatch>

AddType text/html html.htm.php .php3 -php4.phtml.phps in .c gㅑ -pl .shtml-jsp
```

#### 예방

✔ 파일 업로드 디렉토리 "실행"권한 제거

✔ 허용되지 않은 확장자 업로드 제한

### XSS

✔ 관리자가 아닌 일반 사용자가 악성 스크립트 삽입

✔ 홈페이지 접속자의 권한 정보를 탈취하거나 악성코드 감염을 유발할 수 있는 취약점

#### 예방

✔ **XSS 필터 라이브러리**
- ESAPI
- Lucyxss filter

✔ X-XSS-Protection 응답 헤더 사용

✔ 문자열 치환 (<>&" 등을 &lt; &gt; &amp; &quot; 로 치환)
- 보조적인 방법으로 사용 (공격자가 해제 가능)

### SQL Injection

✔ 게시판, 회원가입 창, URL 등을 통해 부적절한 값을 삽입하여 DB데이터를 빼내거나 로그인 절차 우회 등 비정상 동작을 유발

✔ 굉장히 위험하다

#### 예방

✔ 시큐어 코딩(' ; -- # /* */ 등 입력내용 필터링)
- PreparedStatement: 값을 바인딩하는 시점에서 전달된 특수문자 쿼리 등을 필터링하여 sql injection 예방

```sql
1 preparedStatement = "SELECT * FROM users WHERE name = ?";
2 preparedStatement.setString(1, userName);
3
4 # If someone puts
5' or '1'='1
6
7 # Result
8 SQL FIND name : ' or '1'='1
```

✔ 웹 방화벽 구축

## 웹 서버 보안

✔ 계정관리

✔ root 계정의 PATH 환경변수 설정

✔ 서비스 관리

### 계정 관리

✔ root 계정 원격 접속 제한
- root 계정 보안이 특히 중요하다!
- Telnet 원격 접속 차단
- SSH 원격 접속 차단

```bash
Telnet 원격접속 차단
1 vi /etc/securetty
2 pts/0~ pts/x 설정 제거
3
4 vi /etc/pam.d/login
5 # auth required /lib/security/pam_securetty.so #제거(주석제거)
6 auth required/lib/security/pam_securetty.so
```

``` bash
SSH 원격접속 차단
1 vi /etc/ssh/sshd_config
2 "PermitRootLogin no" 설정
```

✔ 로그인 실패 임계값 설정

✔ 패스워드 복잡도 설정
- public key
- two factor 로그인 설정

### root 계정의 PATH 환경변수 설정

✔ PATH에 디렉토리 경로보다 "."(현재 디렉토리)가 먼저 오면, 변조된 명령어 삽입으로 악의적 기능이 실행될 수 있음

### 서비스 관리

✔ Apache, Nginx 등 잘못된 보안 설정으로 발생할 수 있는 비인가자의 원격 접속, 정보 노출 등을 제한하는 것을 목적으로 한다

✔ Directory Listing: 설정된 모든 Directory 옵션 지시자에서 indexes 제거

```bash
#Directory Listing
Index of /
Name Last modified Size Description
secret/ 2017-01-27 15:40
priv/ 2017-01-27 15:41
edit/ 2017-01-27 15:40
dirl/ 2017-01-27 15:40
config.php 2017-01-27 15:40 11K
Apache/2.4.23 (Wm64) PHP/5.6.25 Server at localhost Port 80
```

```bash
#httpd.conf
1 <Directory />
2 #Options Indexes
3 AllowOverride None
4 Order allow, deny
5 Allow from all
6</Directory>
7
```

### 웹 방화벽(WAF)

✔ L7(OSI 7 Layers)에서 보안 유지

✔ SQL injection, XSS 등 웹 공격 탐지, 차단

✔ DDOS, IP차단, Rate limit 등 규칙 생성

✔ modsecurity

## AWS 보안 가이드

## 클라우드의 장점과 보안

### 클라우드의 장점

✔ 초기 선투자 비용 x

✔ **운영 비용 절감**
- 사용한 만큼만 비용만 낸다
- 그러나 해킹 발생 시? -> 어마어마한 비용 부과

✔ 탄력적인 운영 및 확장

✔ **속도 및 민첩성**
- 수 분만에 인프라 구축 가능
- 빠르게 변화에 대응

✔ 비즈니스에만 집중 가능

✔ 글로벌 확장

✔ 접근성


## 사고 사례

✔ 계정해킹

✔ 데이터 유출

✔ 복구 실패(랜섬웨어)

### 시사점

✔ **계정 보안에 대한 책임은 사용자 본인에게 있다** 

✔ 예방
- MFA 활성화
- AWS access key 보호

✔ 리스크 관리
- ROOT 사용자 보안 강화
- IAM 사용자를 통한 관리

✔ 감지
- 비용 관련 알림 설정

## 모범 사례 

### MFA 활성화

✔ Multi Factor Authentication

✔ 일반적으로 Authentication App 사용
- google OTP, **Twilio Authy**, Microsoft Authenticator

[aws 환경에서 사용하는 MFA의 모든 것](https://aws.amazon.com/ko/blogs/tech/all-for-mfa-in-aws-environment/)

[aws에서 MFA 사용](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_credentials_mfa.html)

### AWS Access Key 보호

✔ AWS CLI나 API 사용시, 인증을 위해 사용되는 자격 증명

✔ access key id와 security access key로 구성

✔ 가이드
- 주기적인 access key 교체 및 미사용 key 제거
- 애플리케이션 별 최소 권한 적용
- **github등 commit 시 주의**
- git-secrets등을 활용한 access key 암호화 및 보호

[AWS 액세스 키 관리를 위한 모범 사례](https://docs.aws.amazon.com/ko_kr/accounts/latest/reference/credentials-access-keys-best-practices.html)

### ROOT 사용자 보안 강화

✔ ROOT 사용자
- AWS 계정 생성 시 사용한 이메일 주소와 패스워드로 인증하는 계정
- 모든 권한을 지니고 있으며, 권한 제약 설정이 불가능
- 해킹 시 피해가 막심하다!

✔ 가이드
- 평상시에는 미사용
- Access Key 생성 금지
- 비밀번호 정책 강화
- MFA 활성화

### IAM 사용자를 통한 괸리

✔ AWS identity and Access Management
- aws 리소스에 대한 엑세스를 안전하게 제어할 수 있는 서비스
- 사용자 및 그룹별 인증 및 권한 부여를 통하여, AWS 리소스에 대한 엑세스를 안전하게 제어

✔ 가이드
- 개별/용도별 사용자 생성
- 그룹을 통한 권란 관리
- 비밀번호 정책 강화

### 비용 관련 알림 설정

✔ 이메일 정보 업데이트
- 자주 쓰는 이메일로 설정 및 확인

✔ Free Tier 한도 초과 경보 생성
- 한도 초과 시 메일이나 SMS 설정

✔ 월별/실시간 예상 요금 경고 설정
- Amazon CloudWatch를 이용한 월간 예상 AWS요금 알림 설정
- AWS chatbot을 사용한 slack에서 예산 알림 수신

[예상 AWS요금을 모니터링하기 위한 결제 겅보 생성](https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)

[AWS 프리티어 사용량 추적](https://docs.aws.amazon.com/ko_kr/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html)

## 계정 침해 시 후속 조치

✔ **AWS support 센터에 case 등록 (최우선!)** 

✔ AWS 가이드에 따라 후속 조치
- 무단으로 생성된 비정상 리소스 삭제
- 전체 사용자 (Root 및 IAM 사용자) 암호 변경
- 모든 AWS access key 교체 및 삭제

[AWS 계정 보안 문제 해결 방법 및 꼭 지켜야 하는 보안 모범 사례](https://aws.amazon.com/ko/blogs/korea/troubleshooting-aws-account-security-issues-and-best-practices/)