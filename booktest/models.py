from django.db import models


# 设计和表对应的类，模型类
# Create your models here.

# 一类
# 图书类
class BookInfo(models.Model):
    """
    图书模型类
    """
    # 图书名称 CharField说明是字符串类型，max_length最大长度
    btitle = models.CharField(max_length=20)
    # 出版时间 DateField说明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

# 多类
# 英雄人物类
# hname 英雄名
# hgender 性别
# hage 年龄
# hcomment 备注
# hbook 关系属性，建立图书类与英雄类一对多的关系

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hgae = models.IntegerField(default=10)
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey("BookInfo")

    def __str__(self):
        return self.hname