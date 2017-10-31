from django.conf.urls import url
from . import views,viewsgoods,viewsorders

urlpatterns = [
    # 后台首页
    url(r'^$', views.index,name='myadmin_index'),

    #后台管理员路由
    url(r'^login$', views.login,name='myadmin_login'),
    url(r'^dologin$', views.dologin,name='myadmin_dologin'),
    url(r'^logout$', views.logout,name='myadmin_logout'),
    url(r'^verify$', views.verify,name='myadmin_verify'),#验证码

    #后台用户管理
    url(r'^users$',views.usersindex,name="myadmin_usersindex"),
    url(r'^usersadd$',views.usersadd,name="myadmin_usersadd"),
    url(r'^usersinsert$',views.usersinsert,name="myadmin_usersinsert"),
    url(r'^usersdel/(?P<uid>[0-9]+)$',views.usersdel,name="myadmin_usersdel"),
    url(r'^usersedit/(?P<uid>[0-9]+)$',views.usersedit,name="myadmin_usersedit"),
    url(r'^usersupdate/(?P<uid>[0-9]+)$',views.usersupdate,name="myadmin_usersupdate"),

    #后台商品类别信息管理 
    url(r'^type$', viewsgoods.typeindex, name="myadmin_typeindex"), 
    url(r'^typeadd/(?P<tid>[0-9]+)$', viewsgoods.typeadd, name="myadmin_typeadd"), 
    url(r'^typeinsert$', viewsgoods.typeinsert, name="myadmin_typeinsert"), 
    url(r'^typedel/(?P<tid>[0-9]+)$', viewsgoods.typedel, name="myadmin_typedel"), 
    url(r'^typeedit/(?P<tid>[0-9]+)$', viewsgoods.typeedit, name="myadmin_typeedit"), 
    url(r'^typeupdate/(?P<tid>[0-9]+)$', viewsgoods.typeupdate, name="myadmin_typeupdate"),

    # 后台商品信息管理
    url(r'^goods/(?P<pIndex>[0-9]*)$',viewsgoods.goodsindex,name='myadmin_goodsindex'),
    # url(r'^goods$', viewsgoods.goodsindex, name="myadmin_goodsindex"), 
    url(r'^goodsadd$', viewsgoods.goodsadd, name="myadmin_goodsadd"), 
    url(r'^goodsinsert$', viewsgoods.goodsinsert, name="myadmin_goodsinsert"), 
    url(r'^goodsdel/(?P<gid>[0-9]+)$', viewsgoods.goodsdel, name="myadmin_goodsdel"), 
    url(r'^goodsedit/(?P<gid>[0-9]+)$', viewsgoods.goodsedit, name="myadmin_goodsedit"), 
    url(r'^goodsupdate/(?P<gid>[0-9]+)$', viewsgoods.goodsupdate, name="myadmin_goodsupdate"),

    #后台订单信息管理
    url(r'^orders$',viewsorders.ordersindex,name='myadmin_ordersindex'),
    url(r'^ordersadd$', viewsorders.ordersadd, name="myadmin_ordersadd"), 
    url(r'^ordersinsert$', viewsorders.ordersinsert, name="myadmin_ordersinsert"), 
    url(r'^ordersedit/(?P<uid>[0-9]+)$',viewsorders.ordersedit,name="myadmin_ordersedit"),
    url(r'^ordersupdate/(?P<uid>[0-9]+)$',viewsorders.ordersupdate,name="myadmin_ordersupdate"),
    url(r'^ordersdetail/(?P<tid>[0-9]+)$', viewsorders.ordersdetail,name='myadmin_ordersdetail'),
]
