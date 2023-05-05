// 선택지를 제한하는 느낌?

const AISILE = 0
const MIDDLE = 1
const WINDOW = 2

// 이렇게 하기보다 enum으로 조지기

enum SeatChoice {
    AISILE = 10, // 이렇게 하면 기본 값을 지정해줌 (아니면 0부터 시작)
    MIDDLE = 22, // 중간 값을 직접 지정해줄 수도 있다ㄷㄷ
    WINDOW = "window", // 아니면 값을 넣어줄 수 있는데 이렇게 할려면 다 직접 적어줘야됨
    FOURTH = "fourth"
}

const hcSeat = SeatChoice.AISILE

// 이렇게 하면 enum에 적어둔 값이 할당된다

// 암튼 중요한 건 enum을 어떻게 정의할 것인가

// 저렇게 하면 근데 iife 스타일로 자스 코드 생성됨

// 이렇게 하면 코드가 훨씬 덜 생성돼서 이걸 좋아하는 사람도 있음
const enum SeatChoiceConst {
    AISILE = 10, // 이렇게 하면 기본 값을 지정해줌 (아니면 0부터 시작)
    MIDDLE = 22, // 중간 값을 직접 지정해줄 수도 있다ㄷㄷ
    WINDOW = "window", // 아니면 값을 넣어줄 수 있는데 이렇게 할려면 다 직접 적어줘야됨
    FOURTH = "fourth"
}

const hcSeat_ = SeatChoiceConst.AISILE

