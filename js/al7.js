// satrni raqamga o`tqazish

module.exports = function(s) {
    var num = parseInt(s)
    if(!num) num = 0; else
    if(num > 2147483647) num = 2147483647; else
    if(num < -2147483648) num = -2147483648
    return num
};