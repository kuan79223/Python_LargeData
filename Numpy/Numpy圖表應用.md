    import numpy as np
    import matplotlib.pyplot as plt
    # numpy.linspace(start, stop, num=50, endpoint=True,
                                #切割等分,  是否包括最後一個值
                   #retstep=False, dtype=None, axis=0)
                    #是否輸出間隔值 ,輸出的資料型態,軸向

    n = 8
    y = np.zeros(n)
    x1 = np.linspace(0,10,n,endpoint=True)
![image](https://user-images.githubusercontent.com/112489587/208303394-6e9afb98-855a-4cfa-89ec-edde51b79a47.png)
    
    x2 = np.linspace(0,10,n,endpoint=False)
![image](https://user-images.githubusercontent.com/112489587/208303405-168d4931-491f-459c-98a7-bec6a0027d34.png)

    plt.plot(x1,y,'*')
    plt.plot(x2,y+0.5,'*')
    plt.ylim([-0.5,1])
    plt.show()

![image](https://user-images.githubusercontent.com/112489587/208303427-6d099aa2-9220-4cd6-bbe3-1e37efe99000.png)


*************************
* numpy數值計算     

        x = np.linspace(-3,3,50)
        print(x)
        print(len(x))
        y1 = 2 * x + 1
        print(y1)
        y2 = x ** 2
        print(y2)

**************************************
* 圖表設置      

        fig = plt.figure(figsize=(8,5))  # y軸 ,x軸
        ax1 = fig.add_subplot(1,1,1)
        ax1.plot(x,y1,'r--')
        ax1.plot(x,y2,color='red',linestyle='-',linewidth=1)
        plt.xlabel('title x')
        plt.ylabel('title y')
        plt.title('top title')
        plt.show()

![image](https://user-images.githubusercontent.com/112489587/208304281-f15cf5be-2142-4583-8440-1625766dfe98.png)

**************************************
#練習一
        t = np.arange(0,5,0.1)
        y1 = np.sin(2 * np.pi * t)
        y2 = np.cos(2 * np.pi * t)

        fig = plt.figure(figsize=(8,15))
        ax1 = fig.add_subplot(2,1,1)
        ax1.plot(t,y1,'b-.')

        ax2 = fig.add_subplot(2,1,2)
        ax2.plot(t,y2,'r--')

        plt.show()

![image](https://user-images.githubusercontent.com/112489587/208304322-0d17a830-01dc-4d71-a8cf-675ab4a8d409.png)

*************************************
        fig = plt.figure(figsize=(8,5))
        ax1 = fig.add_subplot(1,1,1)
        ax1.plot([1,2,3,4], [1,4,9,16], 'ro')
        plt.text(1,0.5,'First',color='red',fontsize=15)
        plt.text(2,4.5,'Second')
        plt.text(3,8.5,'Third')
        plt.text(4,12.5,'Four')
        plt.text(5,15,'Five')
        plt.text(1.2,12,'numpy', fontsize=20, bbox= {'facecolor':'yellow','alpha':0.2})
                                              #設定文字方塊
        plt.show()

![image](https://user-images.githubusercontent.com/112489587/208304372-24ebdde5-6f7f-4c0a-b6e8-6afe437b1bbc.png)


************************************
* 長條圖       

        index = ['apple', 'banana', 'orange', 'tomato', 'guava']
        values = np.array([5, 7, 3, 4, 6]) * 1000
        fig = plt.figure(figsize=(8,5))
        ax1 = fig.add_subplot(1,1,1)
        ax1.bar(index,values)
        plt.show()

![image](https://user-images.githubusercontent.com/112489587/208304422-4ca79108-e633-4757-b207-137296cfa393.png)


***********************************
* 標註數值      

        index = np.arange(5)
        values = np.array([5, 7, 3, 4, 6]) * 1000
        fig = plt.figure(figsize=(8,5))
        ax1 = fig.add_subplot(1,1,1)
        ax1.bar(index,values)
        plt.xticks(index,['apple', 'banana', 'orange', 'tomato', 'guava'])
        plt.axis([-1,5,0,8000])
        for i in index:
            plt.text(i-0.2,values[i]+200,values[i])
        plt.show()

![image](https://user-images.githubusercontent.com/112489587/208304505-c4cbc073-7b83-4a66-b563-0572f0ab3fbb.png)
