import os

# 递归获取文件夹大小
def getpathsize(dirpath):
      total = 0
      allname = os.listdir(dirpath)
      for name in allname:
            allpath = os.path.join(dirpath,name)
            if os.path.isfile(allpath):
                  total += os.path.getsize(allpath)
            elif os.path.isdir(allpath):
                  total += getpathsize(allpath)
      return total

dirpath = input('请输入文件夹路径:')

if os.path.isdir(dirpath):
      size=getpathsize(dirpath)
      print(size)
else:
      print('输入路径无效')

