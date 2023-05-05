
// 배열에 들어갈 타입을 지정해준다
const superHeros: string[] = []
// 이렇게 제너릭을 조질 수 잇음
const heroPower: Array<number> = []

type User_ = {
    name: string
    isActive: boolean
}

const allUsers: Array<User_> = []

superHeros.push("spiderman")

allUsers.push({name: "dfdf", isActive: false})

// 이렇게 2차원 배열할 수도 잇음
const MLModels: number[][] = [
    [255, 255, 255],
    [0, 0, 0]
]