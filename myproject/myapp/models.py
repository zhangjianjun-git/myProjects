# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# 定义登录用户模型
class Users(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=50, unique=True)
    password = models.CharField(verbose_name='密码', max_length=128)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='是否激活', default=True)
    is_admin = models.BooleanField(verbose_name='是否管理员', default=False)
    date_joined = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)

    # 定义元类,指定数据表名称
    class Meta:
        db_table = 't_user'  # 指定数据表名称
        verbose_name = "用户信息"  # 指定页面显示应用名称
        verbose_name_plural = "用户信息"  # 指定页面显示应用名称,全量指定

    def __str__(self):
        return self.username


# 定义班级模型
class Class(models.Model):
    name = models.CharField(verbose_name='班级名称', max_length=50)  # 班级名称
    grade = models.CharField(verbose_name='年级', max_length=50)  # 年级
    # remarks = models.TextField(verbose_name='备注', blank=True)  # 备注
    # remarks = RichTextField(verbose_name='备注', blank=True)  # 备注
    remarks = RichTextUploadingField(verbose_name='备注', blank=True,config_name='default')
    teacher = models.ManyToManyField('Teacher',verbose_name='老师')
    # 定义元类,指定数据表名称
    class Meta:
        db_table = 't_class'  # 指定数据表名称
        verbose_name = "班级信息"  # 指定页面显示应用名称
        verbose_name_plural = "班级信息"  # 指定页面显示应用名称,全量指定
    # 定义一个返回的名称,默认返回self
    def __str__(self):
        return self.name

# 定义课程模型
class Course(models.Model):
    name = models.CharField(verbose_name='课程名称', max_length=50)
    teacher = models.ForeignKey('Teacher', verbose_name='教师', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='课程价格', max_digits=10, decimal_places=2)
    remarks = RichTextUploadingField(verbose_name='备注', blank=True)
    # 定义元类,指定数据表名称
    class Meta:
        db_table = 't_course'  # 指定数据表名称
        verbose_name = "课程信息"  # 指定页面显示应用名称
        verbose_name_plural = "课程信息"  # 指定页面显示应用名称,全量指定
        # ordering = ['price']  # 指定排序字段

    def __str__(self):
            return self.name


# 定义老师模型
class Teacher(models.Model):
    name = models.CharField(verbose_name='教师姓名', max_length=50)
    GENDER_CHOICES = (
        ('', '请选择性别'),
        ('male', '男'),
        ('female', '女'),
    )
    sex = models.CharField(verbose_name='性别', max_length=10, choices=GENDER_CHOICES)  # 添加 choices 参数
    age = models.IntegerField(verbose_name='年龄', validators=[MinValueValidator(20), MaxValueValidator(100)])
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    remarks = RichTextUploadingField(verbose_name='备注', blank=True)
    # 定义元类,指定数据表名称
    class Meta:
        db_table = 't_teacher'  # 指定数据表名称
        verbose_name = "教师信息"  # 指定页面显示应用名称
        verbose_name_plural = "教师信息"  # 指定页面显示应用名称,全量指定
        # ordering = ['age']  # 指定排序字段

    def __str__(self):
        return self.name

# 定义学生模型
class Student(models.Model):
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    # 定义性别选项
    GENDER_CHOICES = (
        # ('', '请选择性别'),
        ('male', '男'),
        ('female', '女'),
    )

    sex = models.CharField(verbose_name='性别', max_length=10, choices=GENDER_CHOICES)  # 添加 choices 参数
    age = models.IntegerField(verbose_name='年龄', validators=[MinValueValidator(6), MaxValueValidator(20)])
    image = models.ImageField(upload_to='images/', verbose_name='照片', blank=True)
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    enter_date = models.DateField(null=True, blank=True, verbose_name='入学时间')
    remarks = RichTextField(verbose_name='备注', blank=True)
    # 关联班级
    sclass = models.ForeignKey("Class",on_delete=models.CASCADE,blank=True,null=True,verbose_name='班级')

    # 定义元类,指定数据表名称
    class Meta:
        db_table = 't_student'  # 指定数据表名称
        verbose_name = "学生信息"  # 指定页面显示应用名称
        verbose_name_plural = "学生信息"  # 指定页面显示应用名称,全量指定
        # ordering = ['age']  # 指定排序字段

    # 定义一个返回的名称,默认返回self
    def __str__(self):
        return self.name


# 定义学生班级关系模型
class StudentClass(models.Model):
    student = models.ForeignKey('Student', verbose_name='学生', on_delete=models.CASCADE)
    student_class = models.ForeignKey('Class', verbose_name='班级', on_delete=models.CASCADE)
    remarks = RichTextField(verbose_name='备注', blank=True)

    # 定义元类,指定数据表名称
    class Meta:
        db_table = 't_student_class'  # 指定数据表名称
        verbose_name = "学生班级关系"  # 指定页面显示应用名称
        verbose_name_plural = "学生班级关系"  # 指定页面显示应用名称,全量指定
        unique_together = ('student', 'student_class')  # 指定联合唯一索引


# 定义学生选课关系模型
class StudentCourse(models.Model):
    student = models.ForeignKey('Student', verbose_name='学生', on_delete=models.CASCADE)  # 学生
    course = models.ForeignKey('Course', verbose_name='课程', on_delete=models.CASCADE)  # 课程
    score = models.DecimalField(verbose_name='成绩', max_digits=10, decimal_places=2, null=True, blank=True)  # 成绩
    remarks = RichTextField(verbose_name='备注', blank=True)

    # 定义元类,指定数据表名称
    class Meta:
        db_table = 't_student_course'  # 指定数据表名称
        verbose_name = "学生选课关系"  # 指定页面显示应用名称
        verbose_name_plural = "学生选课关系"  # 指定页面显示应用名称,全量指定
        unique_together = ('student', 'course')  # 指定联合唯一索引

# 菜单模型
class Menu(models.Model):
    name = models.CharField(max_length=30, verbose_name='菜单名称')
    url = models.CharField(max_length=100, verbose_name='菜单URL')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='父菜单')
    order = models.IntegerField(verbose_name='排序', default=0)

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.name
