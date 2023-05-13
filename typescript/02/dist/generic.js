"use strict";
const score = [];
const names = [];
const identityOne = (val) => {
    return val;
};
const identityTwo = (val) => {
    return val;
};
// 인풋과 반환값이 같은 타입이 된다
function identityThree(val) {
    return val;
}
// 보통은 이렇게 줄여서 씀
function identityFour(val) {
    return val;
}
// 이렇게 커스텀 타입을 넣으려고 할 떄 제네릭을 쓰면 좋음,,,
// identityFour<Bottle>({})
function getSearchProducts(products) {
    // do some database operations
    const myIndex = 3;
    return products[myIndex];
}
// 화살표함수에서 쓰기
// 쉼표 붙여서 jsx가 아니라 제너릭이라는 걸 명시적으로 표기해준다
const getMoreSearchProducts = (products) => {
    const myIndex = 3;
    return products[myIndex];
};
function anotherFunction(valOne, valTwo) {
    return {
        valOne,
        valTwo
    };
}
// 확장성을 고려한 코드를 작성하기 좋다.
class Sellable {
    constructor() {
        this.cart = [];
    }
    addToCart(product) {
        this.cart.push(product);
    }
}
