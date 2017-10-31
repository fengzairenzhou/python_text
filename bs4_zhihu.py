#coding:utf8
from bs4 import BeautifulSoup
import requests
import json
import time

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}

sess = requests.session()
sess.headers = headers

def getLogin():
    login_url = 'https://www.zhihu.com/#signin'
    response = sess.get(login_url,headers=headers)
    print response.content

    soup = BeautifulSoup(response.text,'lxml')
    token = soup.select('input[name="_xsrf"]')[0]  # 获取xsrf token
    xsrf = token.get('value')

    # 获取验证码图片
    code_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=en' % (time.time() * 1000)

    code_reponse = sess.get(code_url,)

    with open('code.png','wb') as f:
        f.write(code_reponse.content)

    code = raw_input('输入验证码：')

    data = {
        '_xsrf': xsrf,
        'password' : '1234qwer',
        'captcha_type' : 'en',
        'phone_num' : '18600672750',
        'captcha' : code
    }
    # 提交表单
    response = sess.post('https://www.zhihu.com/login/phone_num',data=data,)
    data = json.loads(response.content)
    print json.dumps(data,indent=4,ensure_ascii=False)


def getHomePage():
    response = sess.get('https://www.zhihu.com/people/meng-te-qia-luo-97/activities')
    print response.text

if __name__ == '__main__':
    getLogin()
    getHomePage()