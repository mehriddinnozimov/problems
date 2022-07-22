// 2 linked list elementlarining yigindisi topilishi kerak
// kiruvchi: l1 = [2,4,3], l2 = [5,6,4]
// chiquvchi: [7,0,8]
// tushuntirish: 342 + 465 = 807.

class Node {
    constructor() {
      var val;
      var next;
    }
  }
     
  function insert( root, item){
    var temp = new Node();
    var ptr;
    temp.val = item;
    temp.next = null;
  
    if (root == null) root = temp;
    else {
      ptr = root;
      while (ptr.next != null)
        ptr = ptr.next;
        ptr.next = temp;
    }
    return root;
  }
  
  function arrayToList( arr, n){
    var root = null;
    for (let i = 0; i < n; i++)
      root = insert(root, arr[i]);
    return root;
  }
  
 module.exports = function(l1, l2) {
    let a1 = [l1.val]
    let a2 = [l2.val]
    while(l1.next !== null){
      l1 = l1.next;
      a1.push(l1.val)
    }
    while(l2.next !== null) {
      l2 = l2.next;
      a2.push(l2.val)
    }
    let num1 = BigInt(a1.reverse().toString().replaceAll(",",""))
    let num2 = BigInt(a2.reverse().toString().replaceAll(",",""))
    let num = num1 + num2
    let arr = Array.from(String(num), numg => Number(numg))
    arr.reverse()
    let n = arr.length;
    var root = arrayToList(arr, n);
    return root
  };
  