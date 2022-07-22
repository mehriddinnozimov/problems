// arab raqamini rim raqamiga o`zgartirish

module.exports = function(num) {
    if(num > 3999) return num;
    let roman = ""
    let ming = parseInt(num/1000);
    if(ming > 0) {
        num -= (ming * 1000)
        for(let i = 0; i < ming; i++) roman += "M";
    }
    let yuz = parseInt(num/100)
    if(yuz > 0) {
        roman += somefunc(yuz, ["CM", "CD", "D", "C"])
        num -= (yuz * 100)
    }
    let onlik = parseInt(num/10)
    if(onlik > 0) {
        roman += somefunc(onlik, ["XC", "XL", "L", "X"])
        num -= (onlik * 10)
    }
    if(num > 0) {
        roman += somefunc(num, ["IX", "IV", "V", "I"])
    }
    return roman
};

let somefunc = function(val, arr) {
    let roman = ""
    if(val == 9) roman += arr[0]; else
        if(val == 4) roman += arr[1]; else
        if(val >= 5) {
            roman += arr[2]
            let val2 = val - 5
            for(let i = 0; i < val2; i++) roman += arr[3]
        } else for(let i = 0; i < val; i++) roman += arr[3];
        return roman
}