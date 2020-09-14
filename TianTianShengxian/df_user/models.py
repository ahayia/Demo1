from django.db import models


# 用户模块对应的表

class UserInfo(models.Model):
    uname = models.CharField(max_length=20,verbose_name='用户名') # 用户名
    upwd = models.CharField(max_length=40,verbose_name='用户密码') # 用户密码
    uemail = models.CharField(max_length=30,verbose_name='邮箱') # 邮箱
    ushou = models.CharField(max_length=200,default='',verbose_name='收货地址') # 收获地址
    uaddress = models.CharField(max_length=200,default='',verbose_name='家庭地址') # 家庭地址
    uphone = models.CharField(max_length=20,default='',verbose_name='电话') # 电话
    uzipcode = models.CharField(max_length=6,null=True,verbose_name='邮政编码') # 邮政编码

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    # 这里定义在admin中要显示的内容
    def __str__(self):
        return self.ttitle.encode('utf-8')
