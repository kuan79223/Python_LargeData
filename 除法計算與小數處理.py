1.python 是使用round(),4捨5入
2.np.around() numpy的4捨5入
3.np.around(array,decimals) 方法代表您要將浮點數資料整數位取四捨五入到第幾個位置，
                            小數位取最接近的偶數，這個方法內需要兩個參數:
            array:進行分析的陣列。
                  decimals小數位數:
                          預設為 0。
                          如果為正數，代表小數位數有幾個位子。
                          如果為負數，代表小數點左邊的正整數將依序四捨五入進位。

import numpy as np
a = np.array([1.0 , 5.45 , 123 , 0.567 , 25.532])
print(a)
print('============')
print(np.around(a))                #預設 decimals =0
print(np.around(a,decimals = 1))   #小數點第幾位     -2 -1 0 1 2
print(np.around(a,decimals = -1))  #整數第幾位

**計算機浮點數問題**
  numpy 官網原文
  關於計算機浮點數問題的文章
  “Lecture Notes on the Status of IEEE 754”, William Kahan
  對於正好在舍入小數值之間的值，NumPy舍入到最接近的偶數值。 

  因此，1.5和 2.5捨入後為2.0，
       -0.5和0.5捨入後為0.0。 
  由於IEEE浮點標準中的小數部分 的不精確表示以及當以10的冪進行縮放時產生的誤差。
  
  
**除法計算與小數處理
  np.floor( ) 方法代表回傳「小於」輸入參數的最大整數。
  np.ceil( ) 方法代表回傳「大於」輸入參數的最小整數。

a = np.array([-1.7 , 1.5 , -0.2, 0.6 , 10])
np.floor(a)
  #out[]:array([-2. , 1., -1.,  0., 10.])

np.ceil(a)
  #out[]:array([-1., 2., -0. , 1. ,10.])
