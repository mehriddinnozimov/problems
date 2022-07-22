// berilgan arrayni 3 talik yangi arraylarga bo`lib chiqish, 
// bunda yangi array elementlari 0 ga teng bo`lishi kerak


// P.S bu ham yechimi unchalik yaxshi bo`lmagan masala, 
// ammo js dagi eng yaxshi yechgan masalam shu deb hisoblayman
module.exports = function(nums) {
    nums.sort((a, b) => a - b)
    var memo = []
    var arr = []
    var i = 0
    var j = 1
    while(i < nums.length - 1) {
        while(j < nums.length) {
            if(j == i) j++;
            var a = nums[i]
            var b = nums[j]
            var k = 0 - (a + b)
            if(search(nums, k, i, j)) {
                var arr2 = [a, b, k].sort()
                if(!memo[arr2.toString()]) {
                    arr.push(arr2)
                    memo[arr2.toString()] = true;
                }
            }
            j++
        }
        i++
        j = 1 + i;
    }
    return arr
}

function search(arr, val1, val2, val3) {
    if(val1 == arr[val3]) return val1 == arr[val3 + 1]; else
    if(val1 == arr[val2]) return val1 == arr[val2 + 1]; else {
        var start = 0
        var end = arr.length - 1;
        while( start <= end) {
            var m = Math.floor((start + end) / 2)
            if(arr[m] === val1) return true; else
            if(arr[m] > val1) end = m - 1; else start = m + 1;
        }
    }
    return false
}