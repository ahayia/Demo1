from django.contrib import admin

# Register your models here.
from df_goods.models import TypeInfo,GoodInfo

# 创建类型表和商品信息表的后台管理
class TypeAdmin(admin.ModelAdmin):
    # 内部可以定义显示信息，admin动作等,默认全显示，默认admin动作是删除商品信息
    # 一个类代表一个注册模型
    list_display = ['id','ttitle']
class GoodAdmin(admin.ModelAdmin):

    list_per_page = 6
    # 商品总数较多添加分页,每页最多六条数据
    list_display = ['id', 'gname','gpic',  'gprice', 'gunit', 'gclick', 'gjianjie', 'gkucun', 'gtype']


# 添加触发器
admin.site.register(TypeInfo,TypeAdmin)
admin.site.register(GoodInfo,GoodAdmin)

