# Ascii 转 16进制
def Ascii2Url(Ascii_Char):
    Hex_Char = ""
    for i in Ascii_Char:
        Hex_Char += '%'+ str(hex(ord(i))).replace("0x","").zfill(2)
    return Hex_Char

# %00 转 Ascii
def Url2Ascii(Url_Char):
    Ascii_Char = ""
    for i in range(len(Url_Char)//3):
        Ascii_Char += chr(int(Url_Char[i*3:i*3+3].replace("%", "0x"), 16))
    return Ascii_Char


print(Ascii2Url("12263*(#&(/flag"))
print(Url2Ascii("%31%32%32%36%33%2a%28%23%26%28%2f%66%6c%61%67"))