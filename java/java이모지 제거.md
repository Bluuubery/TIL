# Java에서 문자열에서 이모지 제거하는 법

## 문제

![](assets/java이모지%20제거.md/2023-03-31-17-44-13.png)

이모지로 된 문자열을 sql에 삽입하려고 하자 에러가 발생한다.

## 원인

MySql에서 일반적으로 문자열 인코딩을 utf8mb3으로 하게 된다. 

이런 상황에서 4바이트인 이모지를 저장하려고 하면 에러가 발생한다.

## 해결

### 2가지 해결책

해결책은 두 가지가 있다.

1. MySql에서 해당 테이블과 칼럼의 데이터 타입을 utf8mb4로 바꿔준다.

2. db에 문자열을 저장할 때 정규식으로 이모지를 제거하고 삽입한다.


내 사례에서는 저장하고자 하는 값에서 이모지가 중요한 요소가 아니고, 서비스에 직접적으로 활용되는 부분이 없어서 2번을 선택했지만 그렇지 않은 경우에는 1번이 더 나은 해결책일 것이다.

### Java에서 정규식으로 이모지 필터링하기

```Java
// 이모지 패턴
private final Pattern EMOJI_PATTERN = Pattern.compile("[\uD83C-\uDBFF\uDC00-\uDFFF]+");

// 이모지 제거
private String removeEmojis(String input) {
    return EMOJI_PATTERN.matcher(input).replaceAll("");
}
```

아래는 해당 메서드를 활용한 서비스 코드의 일부분이다.

```java
List<GameVideo> collect = resultList.stream()
        .map(r -> GameVideo.builder()
                .youtubeId(r.getId().getVideoId())
                // 이모지를 제거하고 삽입!
                .youtubeName(removeEmojis(r.getSnippet().getTitle()))
                .game(gameRepository.findByGameId(gameId).get())
                .createdAt(LocalDateTime.now())
                .build())
        .collect(Collectors.toList());

```

