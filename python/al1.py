# sudoku yechuvchi
# funksiya yechilmagan sudokuni yechib beradi

kiruvchi = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# chiquvchi = [
#     ["5","3","4","6","7","8","9","1","2"],
#     ["6","7","2","1","9","5","3","4","8"],
#     ["1","9","8","3","4","2","5","6","7"],
#     ["8","5","9","7","6","1","4","2","3"],
#     ["4","2","6","8","5","3","7","9","1"],
#     ["7","1","3","9","2","4","8","5","6"],
#     ["9","6","1","5","3","7","2","8","4"],
#     ["2","8","7","4","1","9","6","3","5"],
#     ["3","4","5","2","8","6","1","7","9"]
# ]

# P.S muammoning yechish usulim o`ta yomon bo`lishi mumkindir, ammo bu men yechgan eng yaxshi masala

import collections
import copy

class Solution:
    def solveSudoku(self, list1, rec = True) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def by_a(k, i):
            n1 = [1,2,3] if k <= 3 else [4,5,6] if k <= 6 else [7,8,9]
            n2 = [1,4,7] if i <= 3 else [2,5,8] if i <= 6 else [3,6,9]
            x = [1,2,3] * 3 if k in [1,4,7] else [4,5,6] * 3 if k in [2,5,8] else [7,8,9] * 3
            n = n1 + n2
            n = [x for x, c in collections.Counter(n).items() if c == 2][0]
            x = x[i-1]
            return {"n": n - 1,"r": x - 1}
        def by_c(n, x):
            k = [1,2,3] if n <= 3 else [4, 5, 6] if n <= 6 else [7, 8, 9]
            i = [1, 2, 3] * 3 if n in [1, 4, 7] else [4, 5, 6] * 3 if n in [2, 5, 8] else [7, 8, 9] * 3
            j = 1 if x < 4 else 2 if x < 7 else 3
            return {"k": k[j - 1] - 1,"i": i[x - 1] - 1}
        pattern = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        list2 = []
        list3 = []
        grand = [list1, list2, list3]
        for x in range(0, 9):
            list2.append([])
            for y in range(0, 9):
                list2[x].append(list1[y][x])
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                mini = []
                for c in range(0, 3):
                     mini += list1[x+c][y:y+3]
                list3.append(mini)
        h = 0
        while h < 9:
            lh = 0
            for i, l in enumerate(grand):
                for x in range(0, 9):
                    for y in range(0, 9):
                        if l[x][y] == "." or isinstance(l[x][y], list):
                            l[x][y] = []
                            for v in pattern:
                                if v not in l[x] and v not in l[x][y]:
                                    l[x][y].append(v)
                        else:
                            if not rec:
                                a = l[x].count(l[x][y])
                                if a > 1:
                                    return "f"
                                else:
                                    lh += 1
                if not rec and lh == 81:
                    return "true"            
            for ind, l in enumerate(grand):
                for x in range(0, 9):
                    for y in range(0, 9):
                        if isinstance(l[x][y], list):
                            n = ""
                            k = ""
                            r = ""
                            i = ""
                            if ind == 2:
                                loc = by_c(x+1, y+1)
                                n = x
                                r = y
                                k = loc["k"]
                                i = loc["i"]
                            elif ind == 0:
                                loc = by_a(x+1, y+1)
                                n = loc["n"]
                                r = loc["r"]
                                k = x
                                i = y
                            else:
                                loc = by_a(y+1, x+1)
                                k = y
                                i = x
                                n = loc["n"]
                                r = loc["r"]
                            newlist = []
                            for ass in list3[n][r]:
                                if ass in list2[i][k] and ass in list1[k][i]:
                                    newlist.append(ass)

                            if len(newlist) == 1:
                                newlist = newlist[0]
                            if len(newlist) == 2 and rec:
                                    temp = copy.deepcopy(list1)
                                    temp[k][i] = newlist[0]
                                    res = self.solveSudoku(temp, False)
                                    if res == "t":
                                        newlist = newlist[0]
                                    elif res == "f":
                                        newlist = newlist[1]
                            else:
                                for val in newlist:
                                    lcha = []
                                    for lx in l[x]:
                                        if isinstance(lx, list) and val not in l[x]:
                                            lcha += lx
                                    count = dict(collections.Counter(lcha))
                                    if val in count and count[val] == 1:
                                        newlist = val
                            list3[n][r] = newlist
                            list2[i][k] = newlist
                            list1[k][i] = newlist   
            c = 0
            for item in list1:
                for x in item:
                    if x == "." or isinstance(x, list):
                        c += 1
            if c == 0:
                break
            h += 1
        return list1

# sol = Solution()
# print(sol.solveSudoku(kiruvchi))