## 如何把 numpy array 的資料和 Tensor 做靈活的轉換

### Tensor to Numpy array

    Pytorch = torch.ones(5)
    
    輸出    tensor([1., 1., 1., 1., 1.])
    ------------------------------------
    Numpy = Pytorch.numpy()
    
    轉成 numpy 輸出    [1. 1. 1. 1. 1.]
    
### Numpy array to Tensor

    Numpy = numpy.ones(5)
    
    numpy 輸出    [1. 1. 1. 1. 1.]
    ------------------------------------
    Tensor = torch.from_numpy(Numpy)
    
    轉成 tensor 輸出tensor    ([1., 1., 1., 1., 1.], dtype=torch.float64)
    
    
## 如果你是使用 CPU 來操作 Tensor，在這裡你的 Tensor 跟 Numpy 會共享同一個 memory address ，所以操作會被同步，要特別注意

    Pytorch.add_(1)
    
    print(Pytorch)
    print(Numpy)

    輸出      tensor([2., 2., 2., 2., 2.])
    輸出      [2. 2. 2. 2. 2.]
    

## 使用 GPU
Pytorch 有準備好 GPU 的操作套件，因此可以非常簡單的利用宣告來起用 GPU 來達到加速運算的功能
* 利用 torch.cuda.is_available() 來檢查是否可以使用 GPU cuda

        if torch.cuda.is_available():
        
            device = torch.device("cuda")
            
            tensor_x = torch.ones(5, device=device)    # 將tensor 傳到 cuda
            tensor_y = torch.ones(5)
            tensor_y = tensor_y.to(device)
            tensor_z = tensor_x + tensor_y
            print(tensor_z)


* numpy 只能在 CPU 上面使用，因此如果需要轉回 numpy ，需要先把 Tensor 送回 CPU

        tensor_z =  tensor_z.to("cpu")
        tensor_z =  tensor_z.numpy()
        
## 記住 Pytorch 的基礎運算單位是 Tensor 就沒問題了
## Tensor 的操作有一些記憶體上的使用問題，需要特別注意
