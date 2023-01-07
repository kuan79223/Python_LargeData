## Pytorch 也有一個自己的資料組單位，那就是 Tensor

* 機器學習/深度學習領域鮮少只有單筆資料，因此 Tensor 是一個一維~多維度的運算基本單位
* Tensor 中文翻譯叫做張量，是一個可用來表示在一些向量、純量和其他張量之間的線性關係的多線性函數
* 可以想像成一個高維度向量，也是深度學習裡進行運算的基本元素。

Pytorch and Tensor    
Pytorch 的基本元素都是基於 Tensor 為基礎元素    
Tensor 與 Pytorch 的關聯就類似於 Array 與 Python，就是一個元素    

### 創建 tensor     

* 創建 空的 tensor

      x = torch.empty(2)    
      輸出    tensor([5.2430e+33, 5.4511e-43])

* 創建 多維 tensor

      x = torch.empty(2, 3)   

      輸出    tensor([[0., 0., 0.],
                      [0., 0., 0.]])
* 創建 0 的 tensor         

      x = torch.zeros(2, 3)
      
      輸出    tensor([[0., 0., 0.],
                      [0., 0., 0.]])

#### empty 跟 zeros 的差別在 zeros 是創建零元素，
#### empty 則是單純宣告記憶體區塊，並沒有初始化參數，因此裡面的參數可以是任何值


* 創建 亂數 tensor 

      x = torch.rand(2, 3)
      
      輸出    tensor([[0.6430, 0.0116, 0.1679],
                    [0.8597, 0.1615, 0.4508]])
                    

* 創建 1 的 tensor

      x = torch.ones(2, 3)
      
      輸出    tensor([1., 1., 1.],
                  [1., 1., 1.]])
                  
* 檢查資料型態 torch.dtype
        
      x.dtype
      
      輸出    torch.float32
      預設 dtype 是 torch.float32
      
* 賦予資料型態

      x = torch.ones(2, 3, dtype=torch.int)
      
      輸出    torch.int
      
* 資料大小 torch.size()

      x.size()
      
      輸出    torch.Size([2, 3])
      
* 直接賦予資料大小

      x = torch.tensor([2, 3])

      輸出    torch.Size([2])
      
