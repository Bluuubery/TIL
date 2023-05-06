interface User {
    readonly dbId: number
    email: string
    userId: number
    googleId?: string
    // startTrail: () => string // 메서드 생성ㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷ
    startTrail(): string
    getCoupon(couponname: string): number // 이렇게 하면 인자를 넣을 수 잇음
}

// 타입 클래스랑 머가 다른가요?

// 조금 더 느슨한 범위 대충 뭐가 들어갈지는 지정하는데 구체적으로는 하지 않음
// 메서드가 반환해야할 형태는 지정해주는데 그 내부 로직은 어떻게 강조하지 않음 (자바 인터페ㅣㅇ스랑 비슷한듯ㄷ)

const sunjun: User = {
    dbId: 22,
    email: "s@s.com",
    userId: 2121,
    startTrail: () => {
        return "hello"
    },
    getCoupon: (name: "sunjun10") => {
        return 10
    } // 입력 변수 명이 꼭 일치 하지 않아도 됨ㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷ 순서만 맞으면 된다
}

// 예를 들어 인터페이스에 뭘 더 넣고 싶다고 하자
interface User {
    githubToken?: string
}

// reopening이라고 한다 (자기가 넣고 싶은 거 추가하기) // 이게 type과의 가장 큰 차이 type은 뭐 더 넣으려고 하면 에러 뜸

// 상속도 가능하다ㄷㄷㄷ (여러개도 가능)

interface Admin extends User{
    role: "admin" | "ta" | "learner"
}

