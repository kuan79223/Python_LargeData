# 使用ndarray方法做數值計算   
  * 數值計算函數內放入參與計算的兩個陣列。 
  * 進行計算的陣列第一維數量必須是相同。  
  1. np.add( ) 方法代表「加」，也可以使用「+」。  
  2. np.subtract( ) 方法代表「減」，也可以使用「-」。 
  3. np.multiply( )方法代表「乘」，也可以使用「*」。  
  4. np.divide( ) 方法代表「除」，也可以使用「/」。 
  5. np.power(a,n) 代表 a 陣列的 n 次方。 
  6. a 陣列的 n 次方也可以使用 a ** n 方式表示。 
  
  7. np.reciprocal( ) 代表倒數的計算，0.25 為 4.
  
  8. np.remainder(被除數,除數) 餘數

*******************************************************************
####  NP 陣列重要的原因在於,數學運算不需使用for loop迴圈 

      import numpy as np

      【相同size的純值的運算】
      
      a = np.array([[1., 2., 3.],[4., 5., 6.]])
      a
      a*a
      a-a
      1/a
      a**2
out >> ![image](https://user-images.githubusercontent.com/112489587/208288853-3ce209f2-0634-4a6c-98f7-245095acc467.png)

      【使用相同shape做比對,比較2個array】
      
      b = np.array([[0., 4., 1.],[7., 2., 12.]])
      
      print( b > a)

out >> ![image](https://user-images.githubusercontent.com/112489587/208288926-dffe2133-8ff7-4873-b751-6db3363a35af.png)

************************************
#### 當運算中的 2 個數組的形狀不同時，numpy 將自動觸發廣播機制(broadcasting)】  
    
      a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
      b = np.array([10, 10, 10])
      
      c = np.add(a, b)  # (a+b)
      
      d = np.subtract(a, b)  # (a-b)
      
      f = np.multiply(a, b)  # (a*b)
      
      e = np.divide(a, b)  # (a/b)
      

out >> ![image](https://user-images.githubusercontent.com/112489587/208288998-153adfa0-9f76-473e-8c20-e89b043586d6.png)



************************************
    
    import numpy as np
    a =np.array([4, 5, 6])
    
    np.power(a, 2)
out >> ![image](https://user-images.githubusercontent.com/112489587/208289141-8035cae7-61f0-4b37-8631-c7f29551e4fe.png)

    c = np.array([1, 2, 3])
    
    a**c
out >> ![image](https://user-images.githubusercontent.com/112489587/208289149-84ba199c-7ed6-4e66-b7de-68e44ace6a16.png)

    
    b = np.array([0.25,0.5,0.125])
                 #1/4 ,1/2,1/8
    
    np.reciprocal(b)  #倒數
out >> ![image](https://user-images.githubusercontent.com/112489587/208289162-be6428b3-0583-418f-81de-ccf88575950e.png)

    
    np.remainder(a,c) #餘數
out >> ![image](https://user-images.githubusercontent.com/112489587/208289171-53fb1420-e67f-403e-84ed-8e7c65c3805e.png)
