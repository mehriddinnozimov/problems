// kiruvchi s raqammi?

module.exports = function(s) {
    return !(s.indexOf("Infinity") > -1 || isNaN(Number(s)))
};