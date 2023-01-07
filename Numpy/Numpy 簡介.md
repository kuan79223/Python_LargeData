# Numpy 簡介  

參考文獻 https://ithelp.ithome.com.tw/articles/10233646

1.  可做到的功能
  * 快速的多維陣列操作。
  * 可靠的科學功能函數庫。
  * 可協助繪圖工具進行繪圖。
2.  NumPy 是幾乎每個科學 Python 應用程序或模組的核心，
  * 它提供了以向量化 形式的快速 N-d 陣列類型可供操作。

3.  NumPy 的核心功能是陣列物件類別。
4.  陣列類似 list，但陣列裡的元素必須是相同的類型。
5.  list 不能直接使用算術運算工具 (+, -, *, /, ...) 。
6.  Numpy 提供更有效率的計算與多維運算工具。
7.  必須引用 numpy 才能運作。

下列範例

        import numpy as np
        array1 = np.arange(5)  #[0 1 2 3 4]
        list1 = list(range(5)) #[0, 1, 2, 3, 4]
![image](https://user-images.githubusercontent.com/112489587/208298597-2a86aa24-a60c-49f3-82e5-28e1c3f369cf.png)
        


        a = [1, 3, 5, 7, 9]
        print(a[2:4])
![image](https://user-images.githubusercontent.com/112489587/208298626-023d4cde-8ba2-4053-b426-3cd4cbd01420.png)


        b = [[1,3,5,7,9],[2,4,6,8,10]]
        print(b[0])
![image](https://user-images.githubusercontent.com/112489587/208298851-94ea488c-b0be-4ba0-b062-ee257a78b24d.png)

        print(b[1][2:4])
![image](https://user-images.githubusercontent.com/112489587/208298829-567a59bd-205b-45d1-88cf-de634dbf9b04.png)
      
        c = [1,3,5,7,9]
        d = [2,4,6,8,10]
        f =  c + d      #list 不能直接使用算術運算工具 (+, -, *, /, ...) 。
        print(f)
        
 ![image](https://user-images.githubusercontent.com/112489587/208298734-dc6f2b54-a8e0-4613-80b0-91edad88031f.png)

        


# 陣列類似 list，但陣列裡的元素必須是相同的類型。    
    
    a = np.array([1,3,5,7,9],dtype = int)
    b = np.array([2,4,6,8,10],dtype = int)
    c = a + b       #Numpy 提供更有效率的計算與多維運算工具。
    print(c)
    print(type(a),type(b))
![image](https://user-images.githubusercontent.com/112489587/208298897-bd336fec-9cc6-4c01-855d-f716c1bc55ee.png)
![image](https://user-images.githubusercontent.com/112489587/208298906-3a4b90c4-a661-47dc-99a9-94f820f43037.png)


* 三元運算子  建立50位學生的中文和英文的分數    
      
      chinese = [r.randint(60,100) for _ in range(50)]
      english = [r.randint(60,100) for _ in range(50)]

      print('chinese',chinese)
      print('english',english)

* 中文和英文分數的總合    
      
      result = []

      for i in range(50):
          total = chinese[i] + english[i]
          result.append(total)

      print(result)

* 使用comprehension來建立中文和英文的總合  

      result = [chinese[i] + english[i] for i in range(50)]
      print(result)


# 最簡潔的程式碼   

    chinese = [r.randint(60,100) for _ in range(50)]
    english = [r.randint(60,100) for _ in range(50)]
    result = []
    result = [chinese[i] + english[i] for i in range(50)]
    print(result)
