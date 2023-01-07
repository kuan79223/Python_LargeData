參考文獻: https://zh.m.wikipedia.org/zh-tw/%E6%8C%87%E6%95%B0%E5%87%BD%E6%95%B0     
#### 指數函數:             
        現今指數函數通常特指以 e 為底數的指數函數 e^x , e^x 為數學中重要的函數，也可寫作 exp(x)。
        這裡的 e 是數學常數，也就是自然對數函數的底數，
        近似值為2.718281828}，又稱為歐拉數。

![image](https://user-images.githubusercontent.com/112489587/201462276-8ba50a0b-b968-4fcb-bdb7-66a68b10e51c.png)        

out >>  2.718281828^80  ~ 2.718281828^99        
![image](https://user-images.githubusercontent.com/112489587/201462202-7f5b4547-b2e1-4afe-991e-85d126a0eb79.png)        

#### 對比x,y的每個陣列元素最大值                  
![image](https://user-images.githubusercontent.com/112489587/201462438-834129dd-6c60-4feb-baba-8bec7b356b98.png)        
out >>          
![image](https://user-images.githubusercontent.com/112489587/201462456-3a3b6ae4-b9f3-4ad4-8707-e6835d50d5de.png)        

#### 餘數(小數點),整數               
![image](https://user-images.githubusercontent.com/112489587/201462559-43fac642-a1d2-4671-ad22-15deda42fd93.png)        
out >>          
![image](https://user-images.githubusercontent.com/112489587/201462569-e5eed473-a5ab-4423-a15e-6b35a8455e99.png)        




### 陣列的判斷式      
    
#### python comprehension(串列綜合表達式)      
![image](https://user-images.githubusercontent.com/112489587/201463188-d5fcc5a3-a763-40d7-8ca9-b70928687d78.png)             

out >>          
![image](https://user-images.githubusercontent.com/112489587/201463202-94babc47-caa1-494c-a63a-e39d2e74fdaa.png)        

        np.where() 相等於python-> x if condition else y    
結果一樣    

#### 在print用判斷符         
![image](https://user-images.githubusercontent.com/112489587/201463339-1930c40f-7c9a-46fd-bdd2-4746f51623f7.png)        

![image](https://user-images.githubusercontent.com/112489587/201463407-ac97cec3-26a3-4398-90aa-c8e69b75f8b8.png)        

        np.where()三個參數  
![image](https://user-images.githubusercontent.com/112489587/201463441-09b04597-8951-4c8c-909c-b57d9049bb1e.png)        
out >>          
![image](https://user-images.githubusercontent.com/112489587/201463454-78216043-46e7-4a03-a967-bcc9baa40896.png)        


![image](https://user-images.githubusercontent.com/112489587/201464195-97d04e1b-02cb-4fa3-897b-141dfba42cc4.png)        
out >>  
![image](https://user-images.githubusercontent.com/112489587/201464380-68c9eb7e-4edc-4eca-af6f-002574a74647.png)

### np.統計方法     
        np.sum( ) 代表某一個陣列內容的總和，也可以指定這個陣列的哪一軸 (axis) 內容總和。
        np.min( ) 代表某一個陣列內容的最小值，也可以指定這個陣列的哪一軸 (axis) 內容的最小值。
        np.max( ) 代表某一個陣列內容的最大值，也可以指定這個陣列的哪一軸 (axis) 內容的最大值。
        amin 與 min 是相同功能的方法。
        amax 與 max 是相同功能的方法。
  
#### 範例 10個同學,每個同學5個分數

![image](https://user-images.githubusercontent.com/112489587/201464824-46df56d3-a5ca-4223-80cc-090acfec23d1.png)

out >>          
![image](https://user-images.githubusercontent.com/112489587/201464848-8b4c8d2e-9794-4782-8ce5-1759e824d0f1.png)

        cumsum( ) && cumprod( )  
![image](https://user-images.githubusercontent.com/112489587/201465166-98d75633-e2d9-4117-b1ec-893a8bb5119a.png)        
out >>          
![image](https://user-images.githubusercontent.com/112489587/201465233-1ad391a6-04d7-4bda-a993-5268cc01e605.png)        

#### 範例: 1家分店30天的營收 與 累計營收      

![image](https://user-images.githubusercontent.com/112489587/201465410-1490bd13-815f-40d4-9349-068168aa9571.png)        
out >>  
![image](https://user-images.githubusercontent.com/112489587/201465422-2192cbb0-e4e1-429f-ae27-42012e3c5daa.png)




