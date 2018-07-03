'''
# 将16进制字符串转换为字符串
def GetStr(hexString):
    hexString = hexString.replace(" ", "")
    if ((len(hexString) % 2) != 0):
        hexString += " "
    bits = ""
    for x in range(0, len(hexString), 2):
        bits += chr(int(hexString[x:x + 2], 16))
    return bits

with open('F:\微信数据\WeChat Files\zhou_zhi_shuai\Files\800有重量的数据.txt') as f:
    text = f.read()
    lists = text.split('0D')
    lists = lists[1:10]
    print(len(lists))
    for i in lists:
        s = i.split()
        l = s[5:10]
        a = ' '.join(l)
        print(a)
    a = '20 20 20 20 38 30'
    # print(len(a))
    # s = GetStr(a)
    f.close()
'''

import serial.tools.list_ports

plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("没有发现端口!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 9600, timeout=60)
    print("可用端口名>>>", serialFd.name)

import serial
class Ser(object):
    def __init__(self):
        # 打开端口
        self.port = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='E', stopbits=1, timeout=2)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert_hex(response)
        return response

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result