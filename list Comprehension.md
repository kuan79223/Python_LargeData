for loop顯性迴圈

list Comprehension 隱性迴圈

### [ 結果 for loop ]
    [result for n in data]

### [ 結果 for 雙迴圈 ]
    [result for i in data for j in i]

### [ 結果 for 雙迴圈 if 判斷 ]
    [result for i in data for j in i if j % 2 == 0]

### [ 結果 for loop if 判斷 ]
    [result for n in data if n > 0 ]

### [ 結果1 if 判斷 else 結果2 for loop ]
    [1 if n > 0 else 0 for n in data]

### [ 結果1 if 判斷 else 結果2 雙迴圈 ]
    [0 if j %2 == 0 else 1 for i in data for j in i]
