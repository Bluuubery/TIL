"use strict";
class TakePhoto {
    constructor(cameraMode, filter) {
        this.cameraMode = cameraMode;
        this.filter = filter;
    }
    // 이런식으로 상속받은 자식 클래스한테 메서드를 구현해 전달할 수 있다는 게 차별점,,,,
    getReelTime() {
        // 뭔가 복잡한 연산
        return 8;
    }
}
// const sunjun = new TakePhoto("test", "test") // abstract은 객체를 생성 못한다
class Instagram extends TakePhoto {
    constructor(cameraMode, filter, burst) {
        super(cameraMode, filter); // 이런식으로 해줘야됨 필요한 인자들을 넣어줘야됨
        this.cameraMode = cameraMode;
        this.filter = filter;
        this.burst = burst;
    }
    getSepia() {
        console.log("Sepia");
    }
}
const sunjun = new Instagram("test", "test", 12); // 상속 받은 클래스에서 객체를 생성
