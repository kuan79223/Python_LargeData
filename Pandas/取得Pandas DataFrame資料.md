    dict_data = {
        'name':['Kobe','Wade','JACK'],
        'english':[67,87,77],
        'chinese':[86,94,82]
    }

    df = pd.DataFrame(dict_data)
    # Row
    df.index = ['s1','s2','s3']

    # column 

    df.columns = ['stu_name','eng_score','chin_score']

out >> ![image](https://user-images.githubusercontent.com/112489587/208562693-eedb178b-93cb-4f16-bc58-b718629717ff.png)

### head()：取得第n筆前的資料，並且會回傳一個新的Pandas DataFrame資料集   

    new_df_head = df.head(2)
    
out >> ![image](https://user-images.githubusercontent.com/112489587/208562725-705b0baa-2720-4782-b534-f955dae95343.png)

### tail()：取得最後的n筆資料，並且會回傳一個新的Pandas DataFrame資料集
    
    new_df_tail = df.tail(2)

out >> ![image](https://user-images.githubusercontent.com/112489587/208562989-c1631dd8-f864-44b9-abcc-e2497a246da7.png)

### 取得單一欄位資料(型別為Series)     

      df['stu_name']
    
out >> ![image](https://user-images.githubusercontent.com/112489587/208563305-2f32cc88-21a3-4780-a28c-83d3acf4091f.png)

* 取得單一欄位資料(型別為DataFrame)    
    
      df[['stu_name']]
    
out >> ![image](https://user-images.githubusercontent.com/112489587/208563368-bac970f8-f1e4-4403-999f-57b3a7dbafcb.png)

* 取得多欄位資料(型別為DataFrame)     

      df[['stu_name','eng_score']]
      
out >> ![image](https://user-images.githubusercontent.com/112489587/208563888-26559301-4d5c-4142-8cea-baa6f8727c0f.png)

* 使用索引分割取得資料        


      df[1: 2]
![image](https://user-images.githubusercontent.com/112489587/208565570-00610c96-8e48-46ac-a825-89c624af1ca4.png)

      df[:1 :2]
![image](https://user-images.githubusercontent.com/112489587/208565611-e2b2584f-1112-4ed1-b207-fe8acaf3a110.png)

      df[0: 3]
![image](https://user-images.githubusercontent.com/112489587/208565665-b5b46706-033a-425f-a4d1-6f7f4b19b3f8.png)
      
      df[0: 1:]
![image](https://user-images.githubusercontent.com/112489587/208565694-ebab16b9-6600-4f32-a5b7-cbd0f2ba956d.png)
      
      
## at[資料索引值,欄位名稱]：利用資料索引值及欄位名稱來取得「單一值」       
      dict_data = {
    'name':['Kobe','Wade','JACK'],
    'math':[67,87,77],
    'social':[86,94,82]
    }

    df = pd.DataFrame(dict_data)
    
![image](https://user-images.githubusercontent.com/112489587/208567406-dc36ca36-8fe4-4a34-bb09-b5b9ddd552bc.png)

* 取得 math index 1 的成績
    df.at[1,'math]

out >> 87

