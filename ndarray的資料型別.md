    型別	            型別碼   
    int8,             uint8	i1, u1    
    int32,            uint32	i3, u3    
    int64,            uint64	i4, u4    
    float16	          f2    
    float32	          f4 or f   
    float64	          f8 or d   
    float128	        f16 or g    
    complex64	        c8    
    complex128	      c16   
    complex256	      c32   
    bool	            ?   
    object	          O   
    string_	          S   
    unicode)	        U   


#### 建立自訂資料類型的ndarrays  

    arr1 = np.array([1,2,3],dtype = np.float64)
    arr2 = np.array([1,2,3],dtype = np.float32)
    print(arr1.dtype,arr2.dtype)

![image](https://user-images.githubusercontent.com/112489587/208301797-df6ec394-229e-4423-8b6d-06af78d094f8.png)

* 使用astype() 轉變資料類型   
* 使用astype(),將會建立一個新的array()    

    a = np.array([1, 2, 3])
    print(a.dtype)

    float_a = a.astype(np.float)
    print(float_a.dtype)
![image](https://user-images.githubusercontent.com/112489587/208301915-b1b2a7e7-99eb-4dca-a302-2a9e72dfadbd.png)


* 如果將浮點數轉換為整數,則小數將被刪除
        b = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
        print(b.dtype)

        int_b = b.astype(np.int32)
        print(int_b)

![image](https://user-images.githubusercontent.com/112489587/208301993-b28133ab-d952-4ade-8219-14be1c30328f.png)

* string轉為number

        s = np.array(['1.23','-9.5','43'])      
        print(s)
        print(s.astype(np.float))


![image](https://user-images.githubusercontent.com/112489587/208302226-b22185b0-c0ba-43b6-85cd-e826a3fdfaaf.png)
