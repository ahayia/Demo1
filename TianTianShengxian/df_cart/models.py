from django.db import models

# 购物车模块信息CartInfo

class CartInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE) # 删除关联数据时，与之关联也删除
    goods = models.ForeignKey('df_goods.GoodInfo',on_delete=models.CASCADE)
    count = models.IntegerField()

