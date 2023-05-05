let greetings: string = "Hello World"

greetings.toLowerCase()

console.log(greetings)

// number

let userId: number = 12345

// boolean

let isLoggedIn = false

isLoggedIn.valueOf

// type inferrence

// 딱봐도 숫자 / 불린인데 굳이 적어야될까?

let userId2 = 12345
let isLoggedIn2 = false

// 이렇게 적어도 알아서 타입 정해줌

// any
// 타입 추측이 안되면 any가 된다
// any는 타입보다 아니라 타입이 정해지지 않았음을 나타내는 표시임
// 가능하면 쓰지 말자
// config에서 noImplicitAny하면 any 안 받아줌

// let hero 이렇게 쓰면 안댐ㄷ
let hero: string

function getHero(){
    return 'thor'
}

hero = getHero()

export {}