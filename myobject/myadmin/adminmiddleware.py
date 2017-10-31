#自定义后台中间件类
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import re

class AdminMiddleWare(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		#定义网站后台不用登录也可访问的路由url
		urllist = ['/myadmin/login','/myadmin/verify','/myadmin/dologin','/myadmin/logout']
		#获取当前路径
		path = request.path
		#判断当前请求是否是网站后台访问,并且path不在urllist中
		if re.match('/myadmin',path) and (path not in urllist):
			#判断当前用户是否登录
			if 'adminuser' not in request.session:
				# 执行登录界面跳转
				return redirect(reverse('myadmin_login'))

		response = self.get_response(request)

		return response