### 使用append()方法建立 list

    numlist = []
    numlist.append(1)
    numlist.append(2)
    numlist.append(3)
    numlist.append(4)
    numlist.append(5)

### 使用range()方法加上for in迴圈建立

    numlist = []
    for i in range(1,6):
      numlist.append(i)

### 使用list()和range()建立

    list1 = list(range(1,6))

### 語法:[expression for item in iterable ]    

    com_list = [num for num in range(1,6)]

### 使用list comprehension建立,可以用運算式靈活改變內容值

    com_list = [num-1 for num in range(2,7)]


以上語法的輸出結果皆為==>    

    [1, 2, 3, 4, 5]



### 語法:[expression for item in iterable if condition ]

    numlist = [num for num in range(1,6) if num % 2 == 1]

* 相當於以下語法

      numlist = []
      for number in range(1,6):
        if number % 2 == 1:
          numlist.append(number)
  
out >> [1, 3, 5]

* 使用巢狀迴圈    

      rows = range(1,4)
      columns = range(1,3)
      for row in rows:
        for col in columns:
          
out >> ![image](https://user-images.githubusercontent.com/112489587/210942573-15cfbe88-b909-4aca-85ed-1e712f54b73d.png)


### 語法:[expression for item1 in iterable for item2 in iterable]

    rows = range(1,4)
    columns = range(1,3)
    cells = [(row,col) for row in rows for col in columns]

    for cell in cells:
      cell is  <class 'tuple'>

out >> ![image](https://user-images.githubusercontent.com/112489587/210942722-9a6970f7-06b2-4a44-82c0-416ac0f13ad9.png)

    for row,col in cells:
      print(row,col)
      
out >> ![image](https://user-images.githubusercontent.com/112489587/210942573-15cfbe88-b909-4aca-85ed-1e712f54b73d.png)   



### 語法:{ key_expression : value_expression for expression in iterable }
* Dictionary Comprehensions

      '''文字數量'''
      words = 'letters'
      letter_counts = {ch: words.count(ch) for ch in words}

letter_counts ==>
 ![image](https://user-images.githubusercontent.com/112489587/210942933-780b57b3-ff37-4c2a-8b13-023e0443cc39.png)


*  將word變為set,隨機輸出

        letter_counts = {ch: words.count(ch) for ch in set(words)}

letter_counts ==>
![image](https://user-images.githubusercontent.com/112489587/210943110-d2615eeb-4ff7-4503-8022-386b7260790b.png)



    a_set = {number for number in range(1,6) if number % 3 == 1}

a_set ==>
![image](https://user-images.githubusercontent.com/112489587/210943241-1e845ab0-a547-4568-8783-bdfdd0a17d98.png)


### Generator Comprehensions

* tuple 沒有Comprehensions,使用括號()產生的是generator comprehension

      numthing = (number for number in range(1,6))
      print(numthing)  # 產生一個記憶體空間

      numthing is <class 'generator'>


''' generator只可以使用一次,使用完後就被消滅 '''
     
     for number in numthing:
        print(number)

![image](https://user-images.githubusercontent.com/112489587/210943445-b17d6f6a-8801-480a-9bc2-df346d1e0134.png)

    for number in numthing:
      print('!!!!!!!', number)
