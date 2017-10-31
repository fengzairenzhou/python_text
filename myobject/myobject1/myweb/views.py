from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from myadmin.models import Types,Goods,Users

# 自定义公共信息加载函数
def loadContext(request):
    context={}
    context['typelist'] = Types.objects.filter(pid=0)
    return context

# 会员登录表单
def login(request):
    return render(request,'myweb/login.html')

# 会员执行登录
def dologin(request):
    # 校验验证码
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info':'验证码错误！'}
        return render(request,"myweb/login.html",context)
        
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        #判断当前用户是否是后台管理员用户
        if user.state == 0 or user.state == 1:
            # 验证密码
            import hashlib
            m = hashlib.md5() 
            m.update(bytes(request.POST['password'],encoding="utf8"))
            if user.password == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
                request.session['vipuser'] = user.toDict()
                return redirect(reverse('index'))
            else:
                context = {'info':'登录密码错误！'}
        else:
            context = {'info':'此用户为非法用户！'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"myweb/login.html",context)

# 会员退出
def logout(request):
    # 清除登录的session信息
    del request.session['vipuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('login'))


# 首页
def index(request):
    context = loadContext(request)
    # 获取首页所需商品信息并放置到context
    return render(request,'myweb/index.html',context)

# 列表页
def list(request,tid=0):
    context = loadContext(request)
    # 获取所需商品列表信息并放置到context
    if tid == 0:
        context['goodslist'] = Goods.objects.all()
    else:
        #获取当前类别下的所有子类别信息
        context['types'] = Types.objects.filter(pid=tid)
        # 判断参数ttid是否有值
        if request.GET.get('ttid',None):
            context['goodslist'] = Goods.objects.filter(typeid=request.GET['ttid'])
        else:
            # 获取指定商品类别下的所有商品信息
            context['goodslist'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(tid)+','))
    # 如tid=1的sql：select * from myweb_goods where typeid in(select id from myweb_type where path like '%,1,%')
    return render(request,'myweb/list.html',context)

# 详情页
def detail(request,gid):
    context = loadContext(request)
    # 获取对应商品详情信息并放置到context
    ob = Goods.objects.get(id=gid)
    ob.clicknum += 1
    ob.save()
    context['goods'] = ob
    return render(request,'myweb/detail.html',context)