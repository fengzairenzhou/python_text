from django.conf.urls import url
from . import views,viewsorders,viewsusers

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 网站前端商品展示
    url(r'^$', views.index, name="index"), #首页
    url(r'^list$', views.list, name="list"), #列表页
    url(r'^list/(?P<tid>[0-9]+)$', views.list, name="list2"), #带参数列表页
    url(r'^detail/(?P<gid>[0-9]+)$', views.detail, name="detail"), #详情页

    # 会员及个人中心等路由配置
    url(r'^login$', views.login, name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^myinfo$', views.myinfo, name="myinfo"),
   
    # 购物车路由
    url(r'^shopcart$', viewsorders.shopcart,name='shopcart'), #浏览购物车
    url(r'^shopcartadd/(?P<sid>[0-9]+)$', viewsorders.shopcartadd,name='shopcartadd'), #添加购物车
    url(r'^shopcartdel/(?P<sid>[0-9]+)$', viewsorders.shopcartdel,name='shopcartdel'), #从购物车中删除一个商品
    url(r'^shopcartclear$', viewsorders.shopcartclear,name='shopcartclear'), #清空购物车
    url(r'^shopcartchange$', viewsorders.shopcartchange,name='shopcartchange'), #更改购物车中商品数量

    # 订单路由
    url(r'^ordersform$', viewsorders.ordersform,name='ordersform'), #订单表单
    url(r'^ordersconfirm$', viewsorders.ordersconfirm,name='ordersconfirm'), #订单确认
    url(r'^ordersinsert$', viewsorders.ordersinsert,name='ordersinsert'), #执行订单添加
    url(r'^ordersinfo$', viewsorders.ordersinfo,name='ordersinfo'), #订单信息
    url(r'^ordersdetail/(?P<tid>[0-9]+)$', viewsorders.ordersdetail,name='ordersdetail'), #订单详细信息

]
