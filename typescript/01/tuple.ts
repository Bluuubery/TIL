// 타스에만 이씅ㅁㄷㄷ

// const user: (string | number)[] = ["hc", 2]

// 근데 순서를 맞추고 싶다면?

let tUser: [string, number, boolean]

tUser = ["hc", 131, true]

// 순서를 바꾸면 안된다
tUser = [true, 131, "hc"]

// api 요청을 주고받을 떄 유용하다

// 딱 숫자 3개만
let rgb: [number, number, number] = [255, 123, 112]

rgb = [225, 123, 112, 111] // 이러면 틀림

// 타입을 이런식으로ㄷㄷㄷ
type UserTuple = [number, string]

const newUser: UserTuple = [11, "dfdf"]

newUser[1] = "dfdfd" // 이렇게 되니까 값의 불변을 보증하진 않는다
newUser.push(true) // 예전엔 됐었다는데 지금 보니까 막힌듯

// 원래는 길이도 정해지는데 push를 쓰면 길이 제한이 뚫려서 문제가 있었다는듯?