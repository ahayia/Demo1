from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from df_goods.models import *
from df_cart.models import CartInfo

# 视图是一个个函数，必须传递一个参数：request请求对象，里面有用户发送的请求信息，如url地址和其他数据

def get_cart_count(request):
    # 如果用户登陆账号读取购物车数量
    if(request.session.has_key('user_id')):
        return CartInfo.objects.filter(user_id=request.session['user_id']).count()
    else:
        return 0

# 首页
def index(request):
    # 查询所有商品的分类信息
    typeInfo = TypeInfo.objects.all()
    # 从每个分类中，获取4个的商品(每个种类里面最新的四个商品和最热的，点击量最大的四个商品)
    type0 = typeInfo[0].goodinfo_set.order_by('-id')[0:4]  # 按照上传顺序 时令水果
    type01 = typeInfo[0].goodinfo_set.order_by('-gclick')[0:4]  # 按照点击量
    type1 = typeInfo[1].goodinfo_set.order_by('-id')[0:4] # 海鲜水产
    type11 = typeInfo[1].goodinfo_set.order_by('-gclick')[0:4]
    type2 = typeInfo[2].goodinfo_set.order_by('-id')[0:4] # 全品肉类
    type21 = typeInfo[2].goodinfo_set.order_by('-gclick')[0:4]
    type3 = typeInfo[3].goodinfo_set.order_by('-id')[0:4] # 美味蛋品
    type31 = typeInfo[3].goodinfo_set.order_by('-gclick')[0:4]
    type4 = typeInfo[4].goodinfo_set.order_by('-id')[0:4] # 新鲜蔬菜
    type41 = typeInfo[4].goodinfo_set.order_by('-gclick')[0:4]
    type5 = typeInfo[5].goodinfo_set.order_by('-id')[0:4] # 速冻食品
    type51 = typeInfo[5].goodinfo_set.order_by('-gclick')[0:4]

    # 显示购物车的商品总数量
    cart_num = get_cart_count(request)
    context = {
        'title': '首页', 'guest_cart': 1,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
        'cart_num': cart_num,
    }

    return render(request,'df_goods/index.html',context)

# 商品列表信息页和分页
def good_list(request,tid,pindex,sort):
    # tid：商品种类信息，pindex：商品页码，sort：商品显示分类方式，有默认，价格，人气三种分类方式

    # 根据主键查找当前的商品分类 海鲜或者水果
    typeinfo = TypeInfo.objects.get(pk=int(tid))


    # list.html左侧最新的两个商品，在新品推荐这一列
    news = typeinfo.goodinfo_set.order_by('-id')[0:2]

    # list中间栏的商品显示方式
    good_list = []

    cart_num,guest_cart = 0,0 # 默认购物车商品数量和未登录游客的购物车数量显示
    # 验证登陆
    try:
        user_id = request.session['user_id']
    except:
        user_id = None
    if user_id:
        guest_cart = 1
        cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()

    # 中间商品的排序规则
    if(sort == '1'): # 按照默认最新排序
        good_list = GoodInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif(sort == '2'): # 按照价格排序，贵的排前面
        good_list = GoodInfo.objects.filter(gtype_id=int(tid)).order_by('-price')
    elif(sort == '3'): # 按照人气点击量，点击量高的在前面
        good_list = GoodInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')

    # 分页
    paginator = Paginator(good_list,4) # 把商品列表信息进行分页，每页最多四个数据
    # 返回Page对象，包含商品信息
    page = paginator.page(int(pindex))
    # 把标签的信息放到context里
    context = {
        'title' : '商品列表',
        'guest_cart' : guest_cart,
        'cart_num' : cart_num,
        'page' : page,
        'paginator' : paginator,
        'typeinfo' : typeinfo,
        'sort' : sort,
        'news' : news,
    }
    return render(request,'df_goods/list.html',context)
# 单个商品的细节描述页
# 显示详情页
def detail(request,id):
    goods = GoodInfo.objects.get(pk=int(id)) # 根据主键查找商品信息,先实例化GoodInfo对象
    goods.gclick += 1 # 点击一次，点击量加一
    goods.save() # 查询信息保存
    # 获取新品信息
    news = goods.gtype.goodinfo_set.order_by('-id')[:2]
    cart_count = get_cart_count(request)
    context = {
        'title':goods.gtype.ttitle,
        'guest_cart':1,
        'goods':goods,

        'news':news,
        'id':id,
        'cart_count':cart_count,
    }
    response = render(request, 'df_goods/detail.html', context)

    # 记录最近浏览的商品，在用户中心展示
    # 获取最近浏览商品的cookie，如果没有即设为空字符串
    goods_ids = request.COOKIES.get('goods_ids','')
    # 将int类型的id转换为字符串类型
    goods_id = '%d' % goods.id
    # 如果有浏览记录
    if(goods_ids != ''):
        # 把字符串goods_ids拆分成[id1,id2,id3....]列表
        goods_ids1 = goods_ids.split(',')
        # 如果商品已经被记录，删除该商品，重新添加
        if(goods_ids1.count(goods_id)) >= 1:
            goods_ids1.remove(goods_id)
        # 添加到第一个位置
        goods_ids1.insert(0,goods_id)
        # 只维护五个商品，如果超出就删除最后一个
        if(len(goods_ids1)>=6):
            del goods_ids1[5]
        # 最后拼接为字符串存储
        goods_ids = ','.join(goods_ids1)
    else:
        # 如果没有浏览记录直接添加
        goods_ids = goods_id

    # 写入cookies
    response.set_cookie('goods_ids',goods_ids)
    return response


