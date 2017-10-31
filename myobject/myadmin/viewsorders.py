from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from myadmin.models import Orders,Detail,Goods
import time

def ordersindex(request):
	list1=Orders.objects.all()
	context={'orderlist':list1}
	return render(request,'myadmin/orders/index.html',context)

def ordersadd(request):
	pass
	# return render(request,'myadmin/orders/add.html')

def ordersinsert(request):
	pass
	'''
	try:
		# 封装订单信息，并执行添加
		orders = Orders()
		orders.uid = request.session['vipuser']['id']
		orders.linkman = request.POST['linkman']
		orders.address = request.POST['address']
		orders.code = request.POST['code']
		orders.phone = request.POST['phone']
		orders.addtime = time.time()
		orders.total = request.session['total']
		orders.status = 0
		orders.save()
		#获取订单详情
		orderlist = request.session['orderlist']
		#遍历购物信息，并添加订单详情信息
		for shop in orderlist.values():
			print(shop)
			detail = Detail()
			detail.orderid = orders.id
			detail.goodsid = shop['id']
			detail.name = shop['goods']
			detail.price = shop['price']
			detail.num = shop['m']
			detail.save()
		context={'info':'添加成功！'}
	except:
		context={'info':'添加失败！'}
	return render(request,'myadmin/info.html',context)
	'''

def ordersedit(request,uid):
	try:
		ob=Orders.objects.get(id=uid)
		context={'order':ob}
		return render(request,'myadmin/orders/edit.html',context)
	except:
		context={'info':'没有找到要修改的信息!'}
	return render(request,'myadmin/info.html',context)

def ordersupdate(request,uid):
	try:
		ob=Orders.objects.get(id=uid)
		ob.status=request.POST['status']
		ob.save()
		context={'info':'修改成功！'}
	except:
		context={'info':'修改失败！'}
	return render(request,'myadmin/info.html',context)

def ordersdetail(request,tid):
	try: 
		detail = Detail.objects.get(id=tid)
		order = Orders.objects.get(id=tid)
		detail.img=Goods.objects.get(id=detail.goodsid).picname
		detail.status = Orders.objects.get(id=detail.orderid).status
		detail.time = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(Orders.objects.get(id=detail.orderid).addtime))))
		context = {'detail':detail,'order':order} 
		return render(request,"myadmin/orders/orderdetail.html",context) 
	except: 
		context = {'info':'没有找到信息！'} 
	return render(request,"myadmin/info.html",context)

