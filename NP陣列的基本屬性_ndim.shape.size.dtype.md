
* ndarray.ndim - 維度的數量。  
* ndarray.shape - 顯示出陣列在每個維度上的整數值。      
* ndarray.size - 陣列內元素的總數。    
* ndarray.dtype - 來描述陣列中元素類型的對象。   


# list 與 ndarray 差異 

     list1 = [[1, 2,  3],
              [2, 3, 4]]

     a = np.array(l)
     print(a)
![image](https://user-images.githubusercontent.com/112489587/208300653-147a445a-9dc6-4979-937d-b6027ce807e2.png)

print(a.ndim)  【ndim屬性查詢維度】

out >> 2        (dimension)
               
               【每個陣列都有shape,使用tuple來表示每個維度的大小】
print(a.shape) 【陣列在每個維度上的整數值 [out]: (2,3) 2個維度3個整數】

![image](https://user-images.githubusercontent.com/112489587/208300693-71a56431-8274-42be-8e0f-8b0e22fce94f.png)

print(a.size)  【元素總數量】
out >> 6 
               
               【使用dtype屬性來顯示目前陣列內的資料型態(相同型態)】
print(a.dtype) 【ndarray的資料型別
out >> int


* 產生亂數陣列  
import random
import numpy as np
data = np.random.randn(2,3)    
【隨機得到一個數字，可能是負的或正的，可能大於一或小於一】
print(data)
![image](https://user-images.githubusercontent.com/112489587/208300799-0df543d2-f629-4bfc-b92a-f6bdbb12acb9.png)

print(data * 10)
![image](https://user-images.githubusercontent.com/112489587/208300805-031a4c19-a717-4da4-8b64-a4811dd826d4.png)

data += data
print(data)
![image](https://user-images.githubusercontent.com/112489587/208300818-ea057834-5099-47ae-a244-28829881cead.png)


### 【使用ones(),zeros(),empty(),arange()function建立ndarray】         

          a = np.zeros(10)    

out >> [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

          b = np.zeros((3,6))
         
out >> [[0. 0. 0. 0. 0. 0.]
        [0. 0. 0. 0. 0. 0.]
        [0. 0. 0. 0. 0. 0.]]

          c = np.empty((2,3,2))  #value all is garbage


### 【使用arange()function建立,類似於python range()】      

     array = np.arange(15)
     
![image](https://user-images.githubusercontent.com/112489587/208301189-702183e4-7c59-4024-8c88-e3c3a0654940.png)
    
《np.arange and list 不同語法 ,相同結果》
     
     list = list(range(15))
     
![image](https://user-images.githubusercontent.com/112489587/208301201-858ebd42-0283-43ce-bea1-c677d7b5fccf.png)
     
 
     
