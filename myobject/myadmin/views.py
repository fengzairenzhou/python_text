from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from myadmin.models import Users
import time

# Create your views here.
#后台首页
def index(request):
	return render(request,'myadmin/index.html')

#===============后台管理员操作==============
#后台登录表单
def login(request):
	return render(request,'myadmin/login.html')

#验证码
def verify(request):
	#引入绘图模块 
	from PIL import Image, ImageDraw, ImageFont 
	#引入随机函数模块 
	import random 
	#定义变量，用于画面的背景色、宽、高 
	bgcolor = (random.randrange(20, 100), random.randrange( 20, 100), 255) 
	width = 100 
	height = 25 
	#创建画面对象 
	im = Image.new('RGB', (width, height), bgcolor) 
	#创建画笔对象 
	draw = ImageDraw.Draw(im) 
	#调用画笔的point()函数绘制噪点 
	for i in range(0, 100): 
		xy = (random.randrange(0, width), random.randrange(0, height)) 
		fill = (random.randrange(0, 255), 255, random.randrange(0, 255)) 
		draw.point(xy, fill=fill) 
	#定义验证码的备选值 
	str1 = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0' 
	#随机选取4个值作为验证码 
	rand_str = '' 
	for i in range(0, 4): 
		rand_str += str1[random.randrange(0, len(str1))] 
	#构造字体对象 
	font = ImageFont.truetype('static/STXIHEI.TTF', 23) 
	#构造字体颜色 
	fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255)) 
	fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255)) 
	#绘制4个字 
	draw.text((5, 0), rand_str[0], font=font, fill=fontcolor1) 
	draw.text((25, 0), rand_str[1], font=font, fill=fontcolor2) 
	draw.text((50, 0), rand_str[2], font=font, fill=fontcolor1) 
	draw.text((75, 0), rand_str[3], font=font, fill=fontcolor2) 
	#释放画笔 
	del draw 
	#存入session，用于做进一步验证 
	request.session['verifycode'] = rand_str 
	#内存文件操作 
	import io 
	buf = io.BytesIO() 
	#将图片保存在内存中，文件类型为png 
	im.save(buf, 'png') 
	#将内存中的图片数据返回给客户端，MIME类型为图片png 
	return HttpResponse(buf.getvalue(),'image/png')

#后台执行登录
def dologin(request):
	#校验验证码
	verifycode = request.session['verifycode']
	code = request.POST['code']
	if verifycode != code:
		context = {'info':'验证码错误!'}
		return render(request,'myadmin/login.html',context)
	try:
		#根据账号获取登陆者信息
		user=Users.objects.get(username=request.POST['username'])
		#判断当前用户是否是管理员用户
		if user.state == 0:
			#验证密码
			import hashlib
			m=hashlib.md5()
			m.update(bytes(request.POST['passwd'],encoding="utf8"))
			if user.passwd == m.hexdigest():
				#登录成功,将登录前的信息放入到session中，跳转界面
				request.session['adminuser'] = user.name
				return redirect(reverse('myadmin_index'))
			else:
				context = {'info':'账号或密码错误'}
		else:
			context = {'info':'账号或密码错误'}
	except:
		context = {'info':'账号或密码错误'}
	return render(request,'myadmin/login.html',context)

#退出后台登录
def logout(request):
	#清除登录的session信息
	del request.session['adminuser']
	#跳转登录界面
	return redirect(reverse('myadmin_login'))

#==============后台会员管理==================
#浏览会员
def usersindex(request):
	list1=Users.objects.all()
	context={'userlist':list1}
	return render(request,'myadmin/users/index.html',context)

#添加会员
def usersadd(request):
	return render(request,'myadmin/users/add.html')

#执行会员添加信息
def usersinsert(request):
	try:
		ob=Users()
		ob.username=request.POST['username']
		ob.name=request.POST['name']
		#获取密码并转为md5
		import hashlib
		m=hashlib.md5()
		m.update(bytes(request.POST['passwd'],encoding="utf8"))
		ob.passwd = m.hexdigest()
		ob.sex = request.POST['sex']
		ob.address = request.POST['address']
		ob.code = request.POST['code']
		ob.phone = request.POST['phone']
		ob.email = request.POST['email']
		ob.state = 1
		ob.addtime = time.time()
		ob.save()
		context={'info':'添加成功！'}
	except:
		context={'info':'添加失败！'}
	return render(request,'myadmin/users/info.html',context)

#执行会员删除信息
def usersdel(request,uid):
	try:
		ob=Users.objects.get(id=uid)
		ob.delete()
		#重定向到浏览页
		return redirect(reverse('myadmin_usersindex'))
	except:
		context={'info':'删除失败！'}
	return render(request,'myadmin/users/info.html',context)

#打开会员信息编辑表单
def usersedit(request,uid):
	try:
		ob=Users.objects.get(id=uid)
		context={'user':ob}
		return render(request,'myadmin/users/edit.html',context)
	except:
		context={'info':'没有找到要修改的信息!'}
	return render(request,'myadmin/users/info.html',context)

#修改会员信息
def usersupdate(request,uid):
	try:
		ob=Users.objects.get(id=uid)
		# ob.username=request.POST['username']
		ob.name=request.POST['name']
		# ob.passwd=request.POST['passwd']
		ob.sex=request.POST['sex']
		ob.address=request.POST['address']
		ob.code=request.POST['code']
		ob.phone=request.POST['phone']
		ob.email=request.POST['email']
		ob.state=request.POST['state']
		# ob.addtime=time.time()
		ob.save()
		context={'info':'修改成功！'}
	except:
		context={'info':'修改失败！'}
	return render(request,'myadmin/users/info.html',context)
