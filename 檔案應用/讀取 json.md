    import json

### 以 json.load( ) 函數從 JSON 檔案中取出資料轉入 Python。

    with open('students.json', 'r', encoding='utf-8') as file:
        students = json.load(file)
    print(students)

****

    pydict = {"python": "good", "jun": '100', "python-class": True, "ICQ": False}

### 使用 dumps 將 python 的 Dict 轉成 json 格式的字串

    json2 = json.dumps(pydict, ensure_ascii=False)
    print(json2.__class__)  # <class 'str'>

### 使用 loads 將 json 格式的字串傳成 python 的 Dict

    json3 = json.loads(json2)
    print(json3.__class__)  # <class 'str'>



data.json ==>
{"people": [{"name": "Jack", "website": "jack.com", "from": "USA"}, {"name": "Wendy", "website": "wendy.com", "from": "Canada"}]}

#### 自製輸出型態

    with open('data.json') as file:
        data = json.load(file)
        # 用for迴圈讀取json內的str
        for p in data['people']:
            print('name:' + p['name'])
            print('website:' + p['website'])
            print('From:' + p['from'])
            print()


![image](https://user-images.githubusercontent.com/112489587/211126538-c6c64bb3-16ea-4644-8203-bf3bc23df3ff.png)
