from django.db import models
# Create your models here.

class BaseModel():
    def to_dict(self):
        data = self.__dict__.copy()
        data.pop('_state')
        return data


class Student(models.Model, BaseModel):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知')
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="qq")
    phone = models.CharField(max_length=128, verbose_name="电话")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'<Student: {self.name}>'

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"

class Teacher(models.Model, BaseModel):
    age = models.IntegerField(blank=True, null=True)
    subject = models.CharField(blank=True, null=True, max_length=128)
    name = models.CharField(blank=True, null=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'teacher'
