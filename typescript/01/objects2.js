// READONLY, ?, Optional
var myUser = {
    _id: "1234",
    name: "h",
    email: "h@h.com",
    isActive: false
};
myUser.email = "newemail@email.com"; // 수정이 된다
myUser._id = "assa"; // readonly는 수정이 안된다
