from django.db import models
from django.utils.html import format_html

# 商品模块,主要由分类表和商品表构成。并且想把字段名以中文格式显示
# 商品种类表
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20,verbose_name='种类名称')
    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除') # 逻辑删除,0和1,日后还要用可以再设置

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    # 这里定义在admin中要显示的内容(注意编码问题)
    def __str__(self):
        return self.ttitle

# 商品表
class GoodInfo(models.Model):
    gname = models.CharField(max_length=20,verbose_name='商品名称')
    isDelete = models.BooleanField(default=False,verbose_name='逻辑删除')
    gpic = models.ImageField(upload_to='df_goods',verbose_name='关联图片目录') # 关联的图片

    def gpic_data(self):
        return format_html(
            u'<img src="%s" width="100px"/>',
            self.gname,
        )

    gpic_data.short_description = u'关联图片目录'


    # 意味着价格小数位最多为两位，整数位最多为三位
    gprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='商品价格')# 这里指的是单价
    # 商品的单位，可以为g，kg，斤，两
    gunit = models.CharField(max_length=20,default='500g',verbose_name='商品单位')
    gclick = models.IntegerField(default= 0,verbose_name='商品点击量')
    gjianjie = models.CharField(max_length=200,verbose_name='商品简介')
    gkucun = models.IntegerField(verbose_name='商品库存')
    # 外键关联TypeInfo表
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = 'df_goods_Good'
        verbose_name = '商品信息'
        verbose_name_plural= verbose_name
    def __str__(self):
        return self.gname
