// const User = {
//     name: "sun",
//     email: "sun@email.com",
//     isActive: true
// }


// // 함수의 인자로 object를 넘길 떄 타입을 지정해줄 수 있다.
// // const createUser = ({name: string, isPaid: boolean}) => {}

// let newUser = {name: "sun", isPaid: false, email: "sun@email.com"}

// // object를 이런 식으로 넣어주면 에러가 뜨는데
// createUser({name: "sun", isPaid: false, email: "sun@email.com"})
// // 이렇게 인자로 넘기면 변수로 넘기면 에러가 발생을 안 한다 (근본이 자바스크립트라 그럼;;)
// createUser(newUser)



// 반환 형식 지정
const createCourse = (): {name: string, price: number} => {
    return {name: "react", price: 399}
}


// type alias (자바 클래스랑 비슷한듯;)
type User = {
    name: string
    email: string
    isActive: boolean
}

type MyString = string // 이런 것도 가능하다 (굳이 할 이유는 없음)

const createUser = (user: User): User => {
    return {name: "", email: "", isActive: true}
}

createUser({name: "", email: "", isActive: true})



export {}