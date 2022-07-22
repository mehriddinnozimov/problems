let n, s, arr, arr1, arr2;

const findMedian = require("./al1")
arr1 = [1,3],
arr2 = [2,4];
console.log(findMedian(arr1, arr2))

const mergeKLists = require("./al2")
arr = [
    {val:1, next: {val:4, next: {val:5, next: null}}},
    {val:1, next: {val:3, next: {val:4, next: null}}},
    {val:2, next: {val:6, next:null}},
]
console.log(mergeKLists(arr))

const bigEl = require("./al3")
arr = [1,2,3,1]
console.log(bigEl(arr))

const isNumber = require("./al4")
s = "-123.456e789"
console.log(isNumber(s))

const addTwoNumbers = require("./al5")
arr1 = {val:1, next: {val:4, next: {val:5, next: null}}},
arr2 = {val:1, next: {val:3, next: {val:4, next: null}}},

console.log(addTwoNumbers(arr1, arr2))

const reverseNum = require("./al6")
n=22323434
console.log(reverseNum(n))

const toNum = require("./al7")
s = "999223213"
console.log(toNum(s))

const toRoman = require("./al8")
n = 2021
console.log(toRoman(n))

const sum3 = require("./al9")
arr = [-1,0,1,2,-1,-4]
console.log(sum3(arr))

const friend = require("../js/al11")
n = 300;
console.log(friend(n))