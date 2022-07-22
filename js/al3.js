// arraydan qo`shnilaridan kattaroq elementli topish

module.exports = function(nums) {
    let i = 0;
    for(let j = 1; j < nums.length; j++){
        if(nums[i] < nums[j]) {
            i = j
        }
    }
    return i
};