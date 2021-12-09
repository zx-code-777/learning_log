from django.db import models


class Topic(models.Model):
    """"用户学习的主题"""
    # 存储少量文本，如名称、标题等，可使用CharField,定义CharField属性时，必须告诉Django该在数据库中预留多少空间
    text = models.CharField(max_length=200)
    # 传递实参auto_now_add=True，每当用户创建新主题时，Django都会将这个属性自动设置为当前日期和时间
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
