// tartiblangan linked listlarni bir linked listga yig`ish va qayta tartiblash
// lists = [[1,4,5],[1,3,4],[2,6]] bo`lganda natija = [1,1,2,3,4,4,5,6]

module.exports = function(lists) {
    if(lists.length <= 1) return lists[0] != undefined ? lists[0] : null
    var array = []
    var i = 0
    while(i < lists.length){
        array = array.concat(toArray(lists[i]))
        i++
    }
    var list = createL(array.sort((a,b) => a - b))
    return list != undefined ? list : null
};

function toArray(node){
    var arr = []
    let curr = node
    while(curr && node){
        arr.push(curr.val)
        curr = curr.next
    }
    return arr
}

class L{
    constructor(val){
        this.val = val
        this.next = null
    }
}

function createL(a){
    var node, temp;
    for(var i=a.length-1; i >= 0; i--){
        if(!node)
            node = new L(a[i]);
        else {
            temp = new L(a[i]);
            temp.next = node;
            node = temp;
        }
    }
    return node;
}