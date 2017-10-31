from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from myweb.models import Types,Goods,Orders,Detail
import time

# 自定义公共信息加载函数
def loadContext(request):
    context={}
    context['typelist'] = Types.objects.filter(pid=0)
    return context

# 浏览购物车
def shopcart(request):
    context = loadContext(request)
    if 'shoplist' not in request.session:
        request.session['shoplist']={}
    return render(request,"myweb/shopcart.html",context)

# 添加购物车
def shopcartadd(request,sid):
    #获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=sid)
    shop = goods.toDict();
    shop['m'] = int(request.POST['m'])
    #从session获取购物车信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
    
    #判断此商品是否在购物车中
    if sid in shoplist:
        #商品数量加一
        shoplist[sid]['m']+=shop['m']
    else:
        #新商品添加
        shoplist[sid]=shop

    #将购物车信息放回到session
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))

def shopcartdel(request,sid):
    shoplist = request.session['shoplist']
    del shoplist[sid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))

def shopcartclear(request):
    context = loadContext(request)
    request.session['shoplist'] = {}
    return render(request,"myweb/shopcart.html",context)

def shopcartchange(request):
    context = loadContext(request)
    shoplist = request.session['shoplist']
    #获取信息
    shopid = request.GET['sid']
    num = int(request.GET['num'])
    if num<1:
        num = 1
    shoplist[shopid]['m'] = num #更改商品数量
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shopcart.html",context)

#================订单处理================================
#订单表单页
def ordersform(request):
    #获取要结账的商品id信息
    ids = request.GET['gids']
    if ids == '':
        return HttpResponse("请选择要结账的商品")
    gids = ids.split(',')
    # 获取购物车中的商品信息
    shoplist = request.session['shoplist']
    #封装要结账的商品信息，以及累计总金额
    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = shoplist[sid]
        total += shoplist[sid]['price']*shoplist[sid]['m'] #累计总金额
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    return render(request,"myweb/ordersform.html")

#订单确认页
def ordersconfirm(request):
    return render(request,"myweb/ordersconfirm.html")

#执行订单添加
def ordersinsert(request):
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
    shoplist = request.session['shoplist']
    #遍历购物信息，并添加订单详情信息
    for shop in orderlist.values():
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()
    request.session['shoplist']=shoplist
    context={'info':'添加成功!'}
    return render(request,'myweb/info.html',context)

#提示信息
def ordersinfo(request):
    list1=Orders.objects.all()
    list2=Detail.objects.all()
    for goods in list2:
        goods.img=Goods.objects.get(id=goods.goodsid).picname
        goods.status = Orders.objects.get(id=goods.orderid).status
        goods.time = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(Orders.objects.get(id=goods.orderid).addtime))))
    context={'orderlist':list1,'detaillist':list2}
    return render(request,'myweb/myorder.html',context)

#提示详细信息
def ordersdetail(request,tid):
    try: 
        detail = Detail.objects.get(id=tid)
        order = Orders.objects.get(id=tid)
        detail.img=Goods.objects.get(id=detail.goodsid).picname
        detail.status = Orders.objects.get(id=detail.orderid).status
        detail.time = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(Orders.objects.get(id=detail.orderid).addtime))))
        context = {'detail':detail,'order':order} 
        return render(request,"myweb/ordersdetail.html",context) 
    except: 
        context = {'info':'没有找到信息！'} 
    return render(request,"myadmin/info.html",context)