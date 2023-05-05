// READONLY, ?, Optional

type User = {
    readonly _id: string // immutable
    name: string
    email: string
    isActive: boolean
    creditCardDetails?: number // ?를 붙이면 옵셔널이 된다
}

let myUser: User = {
    _id: "1234",
    name: "h",
    email: "h@h.com",
    isActive: false
}


type cardNumber = {
    cardnumber: string
}

type cardDate = {
    cardDate: string
}

// 이런 짓도 가능ㄷㄷ (기존 타입 섞어쓰기) 
":?HYU\]    q`15tr\=-// 근데 이렇게 cvv처럼 뒤에 굳이 새로 만들어서 넣지는 말기 가능은 한데 별로임 
type cardDetails = cardNumber & cardDate & {
    cvv: number
}




myUser.email = "newemail@email.com" // 수정이 된다
// myUser._id = "assa" // readonly는 수정이 안된다