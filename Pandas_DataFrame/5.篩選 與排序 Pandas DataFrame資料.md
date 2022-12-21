# 資料的篩選

## 通常在處理大量的資料集時，有很高的機率會需要利用條件式來篩選所需的資料，這時候就可以利用中括號 [] 存取欄位來進行資料篩選   

![image](https://user-images.githubusercontent.com/112489587/208804517-f3f832ba-b846-402f-8ced-88d0528ec4b8.png)    

## 另一個最常見的資料篩選情境，就是找出包含特定值的資料集，這時候可以利用Pandas DataFrame的isin()方法()來達成

![image](https://user-images.githubusercontent.com/112489587/208804943-e6a823df-b8da-4bb5-8de3-869aa04bd8df.png)


# 資料的排序

## sort_index()：依照索引值來進行排序，並且會回傳一個新的Pandas DataFrame資料集

![image](https://user-images.githubusercontent.com/112489587/208806433-f9c454c4-c22a-4513-9dcb-647b70bdb699.png)![image](https://user-images.githubusercontent.com/112489587/208806639-212feb82-ba89-4c8d-a042-a606247cbbee.png)
![image](https://user-images.githubusercontent.com/112489587/208806711-4b07eed0-f98e-41b4-ade8-714eb2ade8a3.png)


## sort_values()：依照欄位內容來進行排序，並且會回傳一個新的Pandas DataFrame資料集

![image](https://user-images.githubusercontent.com/112489587/208807526-edbaa681-cd3a-42ce-9ea9-969140106a60.png)![image](https://user-images.githubusercontent.com/112489587/208807678-3190b3ac-2b96-4b9a-b011-d35f1e1f07b8.png)
![image](https://user-images.githubusercontent.com/112489587/208807708-e2deaf27-0a5f-478e-b24c-ad6a95d0e3c8.png)



參考文獻: https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html

