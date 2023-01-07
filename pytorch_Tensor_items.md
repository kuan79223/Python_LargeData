## 選取部分資料 
以下為一組 5 * 3 的亂數 Tensor
    
    x = torch.rand(5, 3)
    tensor([[0.8033, 0.7967, 0.0952],
            [0.0960, 0.2553, 0.9135],
            [0.5835, 0.1997, 0.4466],
            [0.7153, 0.9609, 0.7458],
            [0.1914, 0.5431, 0.2532]])

* 取得第一 column 的 Tensor

      x[:, 0]
      
      輸出    tensor([0.8033, 0.0960, 0.5835, 0.7153, 0.1914])

* 取得第一 row 的 Tensor   
    
      x[0, :]
    
      輸出    tensor([0.8033, 0.7967, 0.0952])

* 取得第二 column 第三 row 的 Tensor
     
      x[1, 2]
      
      輸出    tensor(0.1997)
      
* 取得第一 row, 取得第一 column 的 item

      x[0, 0].items()
      
      輸出    0.8032872080802917
      
* Reshape Tensor  .view()

      y = x.view(15)
      
      輸出    tensor([0.8033, 0.7967, 0.0952, 0.0960, 0.2553, 0.9135, 0.5835, 0.1997, 0.4466,
                      0.7153, 0.9609, 0.7458, 0.1914, 0.5431, 0.2532])

* 自動分配
      
      y = x.view(-1, 5)
      y.size()
      
      輸出    torch.Size([3, 5])


### torch 的基礎運算

* torch.add(num1, num2)
* torch.sub(num1, num2)
* torch.mul(num1, num2)
* torch.div(num1, num2)

* 把 x1 加到 x2 中

       x2.add_(x1)
