# NP初始化的多種方式  

1.針對初始化這部分提供了多種方式:    
              
* 不做初始化 - 例如:np.empty((2, 4))
![image](https://user-images.githubusercontent.com/112489587/208289905-cd3f2755-77ca-4d32-bd46-28baffb4b64f.png)


* 全部規劃為 0 - 例如:np.zeros((3, 4))
![image](https://user-images.githubusercontent.com/112489587/208289970-0f68aca9-50bd-451a-9ed7-c2ea8c82a66c.png)


* 全部規劃為 1 - 例如: np.ones((5, 2))
![image](https://user-images.githubusercontent.com/112489587/208289984-9ea9cd4d-a204-4125-8ac7-ddb9d5b55028.png)

* 全部規劃/填滿為某數，例如 6 - 例如: np.full((3, 3), 6)
![image](https://user-images.githubusercontent.com/112489587/208290001-51cb267d-34f1-415e-ac4f-84461b4c9a85.png)


* 建立對角矩陣，對角皆為 1，其他為 0 - 例如: np.eye(3)
![image](https://user-images.githubusercontent.com/112489587/208290010-a6475098-395a-409d-97b9-da43636a5375.png)


* 建立對角矩陣，對角為 1,2,3,4，其他為 0 - 例如: np.diag([1, 2, 3, 4])
![image](https://user-images.githubusercontent.com/112489587/208290027-5e1be61d-131f-4c07-b8e9-865a6cb19e0c.png)
       
              
              
2.reshape((x,y)) 這個指令就可以將現有的陣列重新規劃為 x 乘以 y 的陣列。   
  
3.np.arange(起始值, 結束值, 固定間隔):也是產生一維陣列，     
  和 np.array( ) 的差別在於 【arange 擁有較大的彈性，而且元素數值是自動化產生。】        

4.np.linspace(起始值, 結束值, 起始與結束的區間內要產生幾個元素 ):   
                  只要給定陣列的區間(起始值、結束值)，就可以要求在這個區間內產生幾個元素。
    
    
    arange(a,b,c) - 不包含 b 由 a 開始 以固定間隔 c 來取值
    ex: np.arange(0,10,5)
![image](https://user-images.githubusercontent.com/112489587/208290357-574579cc-50d1-40ad-af72-e07f7bcecfdc.png)
    
    linspace(a,b,c) - 包含 b 由 a 開始 切割成 c 個資料
    ex: np.linspace(0,10,5)
![image](https://user-images.githubusercontent.com/112489587/208290263-96727b05-53d9-465a-926b-a9dd7aedec20.png)

    linspace(a,b,c,endpoint=False) - 不包含 b 由 a 開始 切割成 c ,預設值為 True 與上例一樣
    ex: np.linspace(0,10,5,endpoint=False)
![image](https://user-images.githubusercontent.com/112489587/208290212-62d6fed6-fd04-4137-b02a-9d573e67a70e.png)



## 基本索引和分割  


    a = np.arange(10)
    print(a[5])     #直接座標 5
    print(a[:5])    # [0 1 2 3 4]
    print(a[5:8])   # [5 6 7]
    a[5:8]=12       # 指定 a 陣列範圍內的值為: 12
    print(a)        # [ 0  1  2  3  4  12  12  12  8  9]


* arr_slice = a[5:8]  #宣告變數 複製 a 陣列片段 
#此時arr_slice為新的陣列 ,陣列值為 [12,12,12]
  
* arr_slice[1] = 12345    
#index 0,1,2 將arr_slice的index 1設為 12345
![image](https://user-images.githubusercontent.com/112489587/208290784-1e13b9c2-b4fc-4e86-9e16-5afb81bc56fe.png)


* arr_slice[:] = 64     
#將arr_slice全部的設為 64


* 明確指定複製陣列   
copy_arr = a[1:4].copy()




************NP array座標解析**************
import numpy as np

list1 = np.arange(9)      #尚未變形前,為直接座標
print(list1)
relist = np.reshape(list1,(3,3)) #reshape後,以索引值來代表
     【= np.array([[0,1,2],[3,4,5],[6,7,8]])】
print(relist)                   #[[0 1 2]
                                # [3 4 5]
                                # [6 7 8]]

print(relist[2])                # [6 7 8]
print(relist[2,:])              # [6 7 8]
print(relist[2:,:])             # [[6 7 8]]

print(relist[:,:2])             #[[0 1]
                                # [3 4]
                                # [6 7]]

print(relist[1,:2])             #[3 4]
print(relist[1:2,:2])           #[[3 4]]


 *陣列指定位置取值
    1.間隔選取【::C】
      以 1 維陣列來說明 x【a:b:c】
        a:選取資料的起始索引
        b:選取資料的結束索引 +1
        c:選取資料間隔，以索引值可以被此值整除的元素，不指定表示 1
    2.倒序 【::-1】
        只是單純的把順序反過來
 *陣列指定位置-給予一個整數
    1.關於指定位置 【row,column】
    2.假設給予一個整數為 N
      如果是給固定的 N，那就代表 row 或 column 等於 N。
      如果是【N:】，那就代表 row 或 column 大於等於 N 的區域。  
      如果是【:N】，那就代表 row 或 column 小於 N 的區域。
      如果是【:】， 那就代表 row 或 column 是任意欄位。
import numpy as np     
 a = np.array([[1,2,3],[3,6,9],[2,4,6]])
print(a)
print(a[0])         #[1 2 3]
print(a[1,2])       #9
print(a[1,1:3])     #[6,9]
print(a[:,1])       #[2,6,4]
a[1,2] = 0
print(a)            #[[1 2 3]
                    # [3 6 0]
                    # [2 4 6]]
print(a[:,0])       #[1 3 2]


******************************************
a = np.array([
[0,1, 2, 3,4,5],
[10,11,12,13,14,15],
[20,21,22,23,24,25],
[30,31,32,33,34,35],
[40,41,42,43,44,45],
[50,51,52,53,54,55],
])
b = a[0,3:5]    #第一列,第3~4欄  shape(2,)
print(b)
c = a[4:,4:]    #第4列之後,第4欄之後 shape(2,2)
print(c)
d = a[:3,:3]    #第3列之前,第3欄之前 shape(3,3)
print(d)
e = a[:,2]      #第2列All,第2欄之前 shape(6,)
print(e)

#指定位置取值
print(a[(0,1,2,3,4),(1,2,3,4,5)])   #絕對位置 shape(5,)

print(a[3:,[0,2,5]])    #第3列之後,第0、2、5欄  shape(3,3)


***********************************************************
******************陣列初始化與重新規劃***********************
x = np.empty((2,4)) #未設值的2*4
print(x)

x = np.zeros((2,4)) #設值0的2*4
print(x)

x = np.ones((2,4))  #設值1的2*4
print(x)

x = np.eye(5)       #建立對角矩陣，對角皆為 1，其他為 0
print(x)

x = np.diag([1,2,3,4])  # 建立對角矩陣，對角為 1,2,3,4，其他為 0 -  【Diagonal】
print(x)                #1 0 0 0
                        #0 2 0 0
                        #0 0 3 0
                        #0 0 0 4
x = np.full((3,3),6)   #全部規劃/填滿為某數
print(x)



**************************************
import numpy as np

  ●(起始值,終止值,切成幾筆) *包括最後一筆
  ●linspace(a,b,c) - 包含 b 由 a 開始 切割成 c 個資料
  x = np.linspace(25,30,5)
  print(x)

  ●linspace(a,b,c,endpoint=False) - 不包含 b 由 a 開始 切割成 c
  x = np.linspace(25,30,5,endpoint = False)
  print(x)

  ●arange(a,b,c) - 不包含 b 由 a 開始 以固定間隔 c 來取值
  x = np.arange(25,30,.5)
  print(x)


  a = np.array([6,7,8,9])
  print(a)
  b = np.arange(4)
  print(b)

  print(a-b)
  print(b**2)
  f = np.array([5,-1,3,9,0])
  print([f<=3])    【陣列值判斷式】
  f[f<=3] = 1      【利用判斷式來改變陣列值】
  print(f)

  ＃.T  【列欄對調的方法】
  a = np.arange(15).reshape((3,5)) ●塑形
  print(a)
  a = np.arange(15).reshape((3,5),order ='F') ●改變陣列值走的方向
  print(a)
  print(a.T)  ●改變陣列形狀
