from django.db import models

# Create your models here.
class banner(models.Model):
    title=models.CharField(max_length=10,verbose_name='首页轮播标题')
    deatil=models.CharField(max_length=40,verbose_name='详情描述')
    def __str__(self):
        return self.title


#只能保存4条数据
class learn(models.Model):
    title=models.CharField(max_length=15,verbose_name='照片主题')
    deatil=models.CharField(max_length=40,verbose_name='照片描述')
    imgpath=models.ImageField(upload_to='ads',verbose_name='照片路径')
    def __str__(self):
        return self.title
class news(models.Model):
    title=models.CharField(max_length=30,verbose_name='新闻标题')
    datetime=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    text=models.TextField(max_length=500,verbose_name='新闻内容')
    imgpath=models.ImageField(upload_to='ads',verbose_name='新闻图片路径')
    def __str__(self):
        return self.title

class us_team(models.Model):
    name=models.CharField(max_length=10,verbose_name='成员名字')
    deatil=models.CharField(max_length=300,verbose_name='成员描述')
    imgpath=models.ImageField(upload_to='ads',verbose_name='成员自画像')
    def __str__(self):
        return self.name


class chose_us(models.Model):
    title=models.CharField(max_length=20,verbose_name='小标题')
    deatil=models.TextField(max_length=300,verbose_name='小标题描述')
    def __str__(self):
        return self.title

#存3条
class service(models.Model):
    imgpath=models.ImageField(upload_to='ads',verbose_name='服务图片')
    title=models.CharField(max_length=30,verbose_name='服务小标题')
    deatil=models.CharField(max_length=100,verbose_name='服务描述')
    def __str__(self):
        return self.title

#存1条
class pro_service(models.Model):
    title=models.CharField(max_length=100,verbose_name='小标题')
    imgpath=models.ImageField(upload_to='ads',verbose_name='图片路径')
    deatil1=models.CharField(max_length=50,verbose_name='描述1')
    deatil2=models.CharField(max_length=50,verbose_name='描述2')
    def __str__(self):
        return self.title

#3*6
class us_suppot(models.Model):
    title=models.CharField(max_length=30,verbose_name='能提供的服务')
    def __str__(self):
        return self.title

class imglist(models.Model):
    imgpath=models.ImageField(upload_to='ads',verbose_name='图片列表(成品图)')


