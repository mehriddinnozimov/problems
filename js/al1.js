// 2 tartiblangan arrayning medianasini topish:
// num1 = [1,3], num2 = [2] natija = 2, [1,2,3] ning medianasi 2

module.exports = function(nums1, nums2) {
    nums1 = nums1.concat(nums2).sort((a, b) => a - b)
    let count = 0
    if(nums1.length == 1) return nums1[0]
    let length = parseInt(nums1.length/2)
    if(nums1.length % 2 == 0) {
        length--
        count = (nums1[length] + nums1[length+1])/2
    } else count = nums1[length]
    return count
};