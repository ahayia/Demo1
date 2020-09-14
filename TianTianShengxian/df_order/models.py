from django.db import models


class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True) # 订单编号
    ouser = models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE) # 收货人
    odate = models.DateTimeField(auto_now=True) # 交易日期
    oIspay = models.BooleanField(default=False) # 是否支付
    ototal = models.DecimalField(max_digits=6, decimal_places=2) # 总价
    oaddress = models.CharField(max_length=100) # 发货地址

    class Meta:
        db_table = 'df_orderInfo'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodInfo',on_delete=models.CASCADE) # 和商品表关联
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE) # 和订单表关联
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()

    class Meta:
        db_table = 'df_orderGoods'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name