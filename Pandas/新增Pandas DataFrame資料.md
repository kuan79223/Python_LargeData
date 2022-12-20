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
    

