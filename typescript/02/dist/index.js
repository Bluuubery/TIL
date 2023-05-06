"use strict";
// class User {
//     public email: string // 기본은 public이다
//     #name: string // 이렇게 자스처럼 #을 달수도 있는데 pirvate이 더 낫다고 하는듯
//     private readonly city: string = "Seoul" // private을 걸면 외부에서 접근이 안된다
//     constructor(email: string, name: string) {
//         this.email = email
//         this.#name = name
//     }
// }
class User {
    // 이렇게 생성자에 넣을 수도 있음
    constructor(email, name) {
        this.email = email;
        this.name = name;
        this._courseCount = 1;
        this.city = "Seoul"; // private을 걸면 외부에서 접근이 안된다
    }
    // getter
    get getAppleEmail() {
        return `apple${this.email}`;
    }
    // private 필드에 getter setter 설정하기
    get courseCount() {
        return this._courseCount;
    }
    // setter는 반환 타입이 없다
    set courseCount(courseNum) {
        if (courseNum <= 1) {
            throw new Error("Course count shoud be more than 1");
        }
        this._courseCount = courseNum;
    }
    // privaet 메서드 생성
    deleteToken() {
        console.log("delete token");
    }
}
class Subuser extends User {
    constructor() {
        super(...arguments);
        this.isFamily = true;
    }
    // private은 안 넘어온다
    // protected으로 바꿔주면 상속 받은 클래스에서도 접근 가능함
    changecourseCount() {
        this._courseCount = 4;
    }
}
const sunjun = new User("s@s.com", "sunjun");