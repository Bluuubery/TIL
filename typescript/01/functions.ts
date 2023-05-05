// function에서는 inferrence를 잘 못함ㅠ

function addTwoWrong(num) {
    num.toUpperCase() // 이딴 게 되버리면 타입스크리트를 쓸 이유가 없다,,,
    return num + 2
}

addTwoWrong(5)

// 함수는 가급적 타입을 명시해주자
function addTwo(num: number){
    return num + 2
}


addTwo(5)

function getUpper(val: string) {
    return val.toUpperCase()
}

getUpper("hello")

function signUpUser(name: string, email: string, isPaid: boolean){
    
}

signUpUser("kim", "kim@email.com", false)

// default value
let loginUser = (name: string, email: string, isPaid: boolean = false) => {}

loginUser("kim", "kim@email.com")


// 반환값 형태 지정하기
// 입력값만이 아니라 반환값의 형태도 지정해줘야된다.

const addTwoReturnsString = (num: number) => {return "hello"}

let result = addTwoReturnsString(2) // 얘가 스트링이 되어버림,,, 협업할 떄 안 좋음 

// 이렇게 해주자
const addThree = (num: number): number => {
    return num + 3
}

let resultTwo = addThree(2) 

// 여러 개의 타입을 가지는 함수도 있을 수 있다(나주엥 알려줌)
const getValue = (myVal: number) => {
    if (myVal > 5) {
        return true
    }
    return "200 OK"
}


// const heros = ["thor", "spiderman", "ironman"]
const heros = [1, 2, 3]

// 알아서 타입을 추측해준다(똑똑) context switching
// map의 결과값은 적어주는 게 좋을지도,,,
heros.map((hero): string => {
    return `hero is ${hero}`
})

// void의 경우에도 명시해주자
// 여기선 당연해 보이는데 여러 명이서 협업을 할 경우에 중요
const consoleError = (errmsg: string): void => {
    console.log(errmsg)
} 

// never 예외처리나 강제 종료의 경우는 void보다 never를 쓰자
const handleError = (errmsg: string): never => {
    throw new Error(errmsg)
}


export {}