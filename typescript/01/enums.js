// 선택지를 제한하는 느낌?
var AISILE = 0;
var MIDDLE = 1;
var WINDOW = 2;
// 이렇게 하기보다 enum으로 조지기
var SeatChoice;
(function (SeatChoice) {
    SeatChoice[SeatChoice["AISILE"] = 10] = "AISILE";
    SeatChoice[SeatChoice["MIDDLE"] = 22] = "MIDDLE";
    SeatChoice["WINDOW"] = "window";
    SeatChoice["FOURTH"] = "fourth";
})(SeatChoice || (SeatChoice = {}));
var hcSeat = SeatChoice.AISILE;
var hcSeat_ = 10 /* SeatChoiceConst.AISILE */;
