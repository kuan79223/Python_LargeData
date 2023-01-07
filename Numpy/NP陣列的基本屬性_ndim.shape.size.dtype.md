# list 與 ndarray 差異 

     list1 = [[1, 2,  3],
              [2, 3, 4]]

     輸出   [[1, 2, 3], [2, 3, 4]]
     -----------------------------
     numpy_a = numpy.array(list1)
     
     輸出   [[1, 2, 3], 
             [2, 3, 4]]
    
    
* ndarray.ndim - 維度的數量。  

          numpy_a.ndim  【ndim屬性查詢維度】

          輸出   2        (dimension)

* ndarray.shape - 顯示出陣列在每個維度上的整數值。      

                               【每個陣列都有shape,使用tuple來表示每個維度的大小】
          print(numpy_a.shape) 【陣列在每個維度上的整數值 2個維度3個整數】

          輸出   (2, 3)


* ndarray.size - 陣列內元素的總數。 

          numpy_a.size  資料大小  

          輸出   6 

* ndarray.dtype - 來描述陣列中元素類型的對象。

          numpy_a.dtype 【ndarray的資料型別】

          輸出   int32


* 產生亂數陣列  

          import random
          import numpy as np
          data = np.random.randn(2,3)    
          
          【隨機得到一個數字，可能是負的或正的，可能大於一或小於一】
     
![image](https://user-images.githubusercontent.com/112489587/208300799-0df543d2-f629-4bfc-b92a-f6bdbb12acb9.png)

          data * 10
![image](https://user-images.githubusercontent.com/112489587/208300805-031a4c19-a717-4da4-8b64-a4811dd826d4.png)

          data += data

![image](https://user-images.githubusercontent.com/112489587/208300818-ea057834-5099-47ae-a244-28829881cead.png)


### 【使用 ones(), zeros(), empty(), arange() 建立 ndarray】         

          a = np.zeros(10)    

     輸出   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

          b = np.zeros((3,6))
         
     輸出   [[0. 0. 0. 0. 0. 0.]
             [0. 0. 0. 0. 0. 0.]
             [0. 0. 0. 0. 0. 0.]]

          c = np.empty((2,3,2))  #value all is garbage


### 【使用 arange() 建立,類似於python range()】      

     array = np.arange(15)
     
![image](https://user-images.githubusercontent.com/112489587/208301189-702183e4-7c59-4024-8c88-e3c3a0654940.png)
    
《np.arange and list 不同語法 ,相同結果》
     
     list = list(range(15))
     
![image](https://user-images.githubusercontent.com/112489587/208301201-858ebd42-0283-43ce-bea1-c677d7b5fccf.png)
     
 
     
