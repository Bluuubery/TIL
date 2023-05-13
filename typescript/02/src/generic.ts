const score: Array<number> = []

const names: Array<string> = []

const identityOne = (val: boolean | number): boolean | number => {
    return val
}

const identityTwo = (val: any): any => {
    return val
}

// 인풋과 반환값이 같은 타입이 된다
function identityThree<Type>(val: Type): Type {
    return val
}

// 보통은 이렇게 줄여서 씀
function identityFour<T>(val: T): T {
    return val
}

interface Bottle {
    brand: string,
    type: number
}

// 이렇게 커스텀 타입을 넣으려고 할 떄 제네릭을 쓰면 좋음,,,
// identityFour<Bottle>({})

function getSearchProducts<T>(products: T[]): T {
    // do some database operations
    const myIndex = 3    
    return products[myIndex]
}

// 화살표함수에서 쓰기
// 쉼표 붙여서 jsx가 아니라 제너릭이라는 걸 명시적으로 표기해준다
const getMoreSearchProducts = <T, >(products: T[]): T => {
    const myIndex = 3
    return products[myIndex]
}


interface Database{
    connection: string,
    username: string,
    password: string
}


function anotherFunction<T, U extends Database>(valOne: T, valTwo: U): object {
    return {
        valOne,
        valTwo
    }
}

// anotherFunction(3, {}) // 이런 식으로 좀 복잡한 경우도 있을 수 있다

interface Quiz {
    name: string
    type: string
}

interface Course{
    name: string
    author: string
    subject: string
}

// 확장성을 고려한 코드를 작성하기 좋다.
class Sellable<T>{
    public cart: T[] = []

    addToCart(product: T){
        this.cart.push(product)
    }
}