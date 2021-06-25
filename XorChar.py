# 异或绕过precht

def finds(s):
    list = [i for i in range(0, 32)] + [i for i in range(127, 255)]
    for j in list:
        for k in list:
            if ord(s) == j ^ k:
                return "{}==%{}^%{}".format(s, str(hex(j))[2:], str(hex(k))[2:])

def find(a):
    for i in a:
        print(finds(i))

find("_GET")
# %80%80%80%80^%df%c7%c5%d4