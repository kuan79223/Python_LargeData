import json
with open('新北市公共自行車租賃系統.json') as file:
  data = json.load(file)
  if data['success']:
    records = data['result']['records']
  else:
    print('Read fail')

for record in records:
  if '新店區' in record['sarea']:
    print('區域',record['sarea'])
    print('站名',record['sna'])
    print('地址',record['ar'])
    print('緯經度座標[{},{}]'.format(record['lat'],record['lng']))
    print('全部數量',record['tot'])
    print('可借',record['sbi'])
    print('可還',record['bemp'])
    print('----------------------')
    print()
