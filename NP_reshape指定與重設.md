
### 1.指定與重設 
  
  (1) 一個整數指定 
  
  (2) tuple 或 list 指定  
  
  (3) 重設陣列   

###  2.重設新陣列   
  (1) resize 這個動作會依據原本的陣列再設定指定大小的新陣列。   
  
  (2) resize 動作的參數如下:   
          
          numpy.resize(arr1，shape1)
          arr1:原本的陣列
          shape1:新規劃的大小
  (3)如果規劃的新陣列比較大，將會重新複製原有陣列的資料，填滿新的儲存格。 

  (4)resize 這個動作建立新的陣列，而 reshape 則是依據原有的重新規劃，仍會受到原有陣列影響。      
  
  
    a = np.arange(12)
  
out >>  ![image](https://user-images.githubusercontent.com/112489587/208289626-c4bbbd54-1f07-4b2d-8d06-675db4d40c9c.png)

  
    b = a.reshape((3, 4))
  
out >> ![image](https://user-images.githubusercontent.com/112489587/208289635-91788e25-bcda-4387-a3aa-b1954c1832c7.png)

     
    d = a.reshape((3, 4), order='F')  #Fortran

out >> ![image](https://user-images.githubusercontent.com/112489587/208289639-113ca963-231d-451c-8703-0017bbe2c8d4.png)

     
    e = a.reshape((2, 6))
out >> ![image](https://user-images.githubusercontent.com/112489587/208289648-c93837fd-4080-4904-9bc6-d4e8ee2ad4eb.png)

    a.reshape((1, 2, 6))

out >> ![image](https://user-images.githubusercontent.com/112489587/208289659-93115d58-2d14-4ef6-b382-cf9ff20165d6.png)


    a.reshape((1, 2, 1, 6))
out >> ![image](https://user-images.githubusercontent.com/112489587/208289705-2aa27e51-f3af-47f3-a432-da59730e5320.png)


       
    a.reshape((1, 2, 1, 6, 1))
  
out >> ![image](https://user-images.githubusercontent.com/112489587/208289694-b14c3aa5-c5a5-42f8-a2f7-b1a02f0af860.png)

