//berilgan n songacha bo`lgan do`st sonlarni topish
// do`st sonlar birinchisining bo`linuvchilari yigindisi 2 chisiga teng bolgan sonlar

function sumFunc(n) {
    let sum = 0
    for (let i = 1; i < n; i++){
        if(n % i == 0) sum += i
    }
    return sum
}

module.exports = function (n) {
    let arr = []
    for(let a = 1; a <= n; a++){
        let a1 = sumFunc(a)
        if(sumFunc(a1) == a && a1 != a) arr.push(a);
    }
    return arr
}