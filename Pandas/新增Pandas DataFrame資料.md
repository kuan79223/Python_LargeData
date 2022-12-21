    import pandas as pd

    data = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
    }

    df = pd.DataFrame(data)

out >> ![image](https://user-images.githubusercontent.com/112489587/208657506-0e3c523a-5c64-4a38-80d5-6f1010abfea8.png)

### insert()：在指定的欄位位置新增欄位資料
    
    #        (第幾欄位, column = 欄位內容, value = [])
    df.insert(2,column = 'english',value=[78, 88, 86, 90])
    
out >> ![image](https://user-images.githubusercontent.com/112489587/208658923-a9edff67-5511-48bb-991e-b5d6b51d507c.png)
    

### append()：新增一筆或一列的資料，透過傳入字典(Dictionary)來指定各欄位的值，
### 並且會回傳一個新的Pandas DataFrame資料集       

    new_df = df.append({'name':'Kobe','math':80,'chinese':90},ignore_index=True)
    
out >> ![image](https://user-images.githubusercontent.com/112489587/208674312-71d19824-f9fd-4d91-bef0-fddb00917b80.png)


### concat 
    # 字典1
    
    data1 = {
        "name": ["Mike", "Sherry", "Cindy", "John"],
        "math": [80, 75, 93, 86],
        "chinese": [63, 90, 85, 70]
    }

    df1 = pd.DataFrame(data1)


out >>![image](https://user-images.githubusercontent.com/112489587/208795779-95e0002c-8893-480c-ac31-658060c22c4e.png)


    # 建立一個新字典
    
    data2 = {
        'name': ['Kobe','Wade'],
        'math': [0, 100],
        'chinese': [0,100]
    }
    
    df2 = pd.DataFrame(data2)


    # 合併兩個字典的 DataFrame
    new_df = pd.concat([df1,df2],igonre_index=True)

out >> ![image](https://user-images.githubusercontent.com/112489587/208795819-34f58adc-4f82-4de5-8a5c-afafa4d0fa79.png)

