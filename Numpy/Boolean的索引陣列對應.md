
    import numpy as np
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    data = np.random.randn(7,2)

    print(data)
![image](https://user-images.githubusercontent.com/112489587/208304836-164a105b-29c0-40a5-ba23-145bd0fe6808.png)

    print(names == 'Bob')  #輸出Boolean
    
![image](https://user-images.githubusercontent.com/112489587/208304818-f525158a-53c5-4be6-9bcb-26ac1cfda4bd.png)


* 將Boolean為 True的索引位置對照data索引位置輸出   
        data[names == 'Bob']
![image](https://user-images.githubusercontent.com/112489587/208304914-0643e682-8a92-4cce-acd2-ce368e3cfce2.png)


        data[names == 'Bob', 1:]
        #輸出相同
        data[names == 'Bob', 1]
   out >> 與 'Bob' 相同內容的index data的 index 1
![image](https://user-images.githubusercontent.com/112489587/208305715-0af0cce7-ef02-434b-a208-4e1fb3238422.png)

   
        #print(names != 'Bob')  #輸出Boolean
   
        mask = (names == 'Bob') | (names == 'Will')
        print(mask)            #輸出Boolean
  
![image](https://user-images.githubusercontent.com/112489587/208305244-60b7d4e6-d223-474a-8104-1140ee6c6022.png)


        print(data[mask])

![image](https://user-images.githubusercontent.com/112489587/208305206-58d1c9ad-3664-403e-a87f-cf922f84caf2.png)

        data[data < 0] = 0  #小於0的陣列值換成0
        print(data)

![image](https://user-images.githubusercontent.com/112489587/208305080-fe07322f-7164-4dde-a5f0-023fbd632946.png)

* 以判斷式的結果來改變陣列值     
    
        data[names != 'Joe'] = 7
        print(data)

![image](https://user-images.githubusercontent.com/112489587/208305055-6ec69d13-d4a0-4ec3-a18c-63ba4a9fc87a.png)
