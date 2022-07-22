// raqamni teskarisiga o`girish kerak
// misol 123 = 321

module.exports = function(x) {
    var str = Math.abs(x).toString().split("").reverse().join("")
    if(parseInt(str) > 2147483648) str = 0
    else if(x < 0) str = "-" + str
    return parseInt(str)
  }