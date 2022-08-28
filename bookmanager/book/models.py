from django.db import models

# Create your models here.

"""
1、模型类继承自 models.Model
2、系统会自动添加一个主键--id
3、字段
    字段名 = models.类型(选项)

    字段名是数据表的字段名
    字段名不要使用Python、Mysql的关键字
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='书籍名称')

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='姓名')
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
