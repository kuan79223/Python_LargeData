# 在 python 產生 json檔  json.dump() 不會 return 任何, 純粹轉檔用

* 儲存為 json 的檔案格式 使用 json.dump() 寫入 json 檔, json可以儲存複雜的 python 的資料結構

    
      import random as r
      import json
      import numpy as np
      
      students = []
      for i in np.arange(0, 3):
        student_dict = {'姓名':'stu'+str(i+1),
                        '國文':r.randint(50,100),
                        '英文':r.randint(50,100),
                        '數學':r.randint(50,100),
                        '自然':r.randint(50,100),
                        '社會':r.randint(50,100)}
        students.append(student_dict)



      with open('students.json', 'w', encoding='utf=8')as file:
        
        json.dump(students, file, ensure_ascii=False)
  

# 以 json.dumps() 的語法 印出 json 內容 資料型態為 str
       
       json.dumps(students, ensure_ascii=False)

      輸出  
      
      [{"姓名": "stu1", "國文": 88, "英文": 86, "數學": 68, "自然": 97, "社會": 100}, {"姓名": "stu2", "國文": 90, "英文": 77, "數學": 78, "自然": 79, "社會": 81}, {"姓名": "stu3", "國文": 62, "英文": 64, "數學": 58, "自然": 89, "社會": 52}]


    
# 讀取 json 檔案 以 json.load() 型態為 list

      with open('students.json', 'r', encoding='utf-8') as file:
          
          students = json.load(file)
      
   







