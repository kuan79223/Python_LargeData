      # list內放dictionary

      import random as r
      import json

      students = []
      for i in range(50):
        student_dict = {'姓名':'stu'+str(i),
                        '國文':r.randint(50,100),
                        '英文':r.randint(50,100),
                        '數學':r.randint(50,100),
                        '自然':r.randint(50,100),
                        '社會':r.randint(50,100)}
        students.append(student_dict)


      # json可以儲存複雜的python的資料結構

      # 儲存為json的檔案格式
      # 使用json.dump()

      with open('students.json','w',encoding='utf=8')as file:
        json.dump(students,file,ensure_ascii=False)
  


      print(json.dumps(students, ensure_ascii=False))

輸出為:    
https://github.com/kuan79223/Python_AI-Artificial-Intelligence-/blob/main/%E6%AA%94%E6%A1%88%E7%B3%BB%E7%B5%B1%E7%9A%84%E4%BD%BF%E7%94%A8/students.json
