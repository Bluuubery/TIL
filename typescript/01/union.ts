
// 데이터의 타입이 명확하지 않을 때 union을 사용하면 좋다 any는 쓰지 말자


// 근데 가능한 strict하게 하는 게 좋다 (막 난사하면 any랑 다를 게 업슴,,,)
let score: number | string = 33 
score = "44"


type User = {
    name: string
    id: number
}

type Admin = {
    username: string
    id: number
}

// 이렇게 직접 만든 타입으로 할 수도 있음
let sunjun: User | Admin = {
    name: "sunjun",
    id: 112
}

// admin이 되어버림
sunjun = {
    username: "sunjun",
    id: 112
}

// 함수에 적용할 수 이씀

const getDbId = (id: number | string): void => {
    console.log(`DB id is: ${id}`)

    // id.toLowerCase() // 숫자가 들어올 수 있어서 이렇겐 안된다

    // 이렇게 해줘야댐 (narrowing)
    if (typeof id === "string") {
        id.toLowerCase()
    }

    
}

getDbId(3)
getDbId("asd123")


// array에 써보기

const data: (number | string)[] = [1, 2, 3, "4"] // 이렇게 묶어줘야된다
const data2: number | string[] = [1, 2, 3, "4"] // 이건 숫자거나 string 배열이라는 뜻
const data3: number[] | string[] = [1, 2, 3, "4"] // 이건 숫자 배열이거나 string 배열이라는 뜻


// 아예 값을 지정해줄 수 있다ㄷㄷㄷㄷ

let seatAllotment: "aisle" | "middle" | "window"

seatAllotment = "aisle"
seatAllotment = "crew" // 이걸 막아줌ㄷㄷㄷ