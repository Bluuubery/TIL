// // interface왜 씀? -> ios 개발 환경의 사례로 설명해준다는데 =,,,

// interface TakePhoto {
//     cameraMode: string
//     filter: string
//     burst: number
// }

// // 이렇게 구현체한테 필요로 하는 기본적인 얘들을 강제할 수 있음(대충 자바랑 비슷한듯)
// // 코드 전체에 일관성을 부여한다
// class Instagram implements TakePhoto {

//     constructor(
//         public cameraMode: string,
//         public filter: string,
//         public burst: number
//     ){}

// }

// class Youtube implements TakePhoto {

//     constructor(
//         public cameraMode: string,
//         public filter: string,
//         public burst: number,
//         public short: string // 이렇게 구현체에서 필요한 녀석들을 더 넣을 수 있음
//     ){}
// }