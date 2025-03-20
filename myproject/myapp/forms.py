from django import forms
from django.core.exceptions import ValidationError

from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名：", required=True, error_messages={'required': "请输入你的名字"})
    password = forms.CharField(label="用户密码：", required=True, error_messages={'required': "请输入你的密码"},
                               widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        # 判断用户名是否存在
        if not Users.objects.filter(username=username).exists():
            raise ValidationError('用户不存在，请注册')
        return username

    # 验证密码
    def clean_password(self):
        uname = self.cleaned_data['username']
        password = self.cleaned_data['password']
        # 判断密码是否正确
        user = Users.objects.get(username=uname)
        if user.password != password:
            raise ValidationError('密码错误，请重新输入')
        return password


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名称：", max_length=18)
    password = forms.CharField(label="用户密码：", widget=forms.PasswordInput)
    age = forms.IntegerField(label="用户年龄：")
    email = forms.EmailField(label="用户邮件：")


# 创建class表示登录的表单，要关联Users实体类
class UserLoginForm(forms.ModelForm):
    # 创建内部类Meta，关联Model
    class Meta:
        # 1、指定关联的Model
        model = Users
        # 2、指定要生成的控件
        fields = ["username", "password"]
        # 3、指定每个控件对应的label
        labels = {
            "username": "用户名称",
            "password": "用户密码"
        }


class UserRegisterForm(forms.ModelForm):
    # 创建内部类Meta，关联Model
    class Meta:
        # 1、指定关联的Model
        model = Users
        # 2、指定要生成的控件
        fields = "__all__"
        # 3、指定每个控件对应的label
        labels = {
            "username": "用户名称",
            "password": "用户密码",
            "age": "用户年龄",
            "email": "用户邮箱"
        }


# 表示评论内容表单控件
# 评论标题  文本框
# 评论人邮件   type='Email'
# 题目  Select
# isSave  type="checkbox"
class RemarkForm(forms.Form):
    subject = forms.CharField(label="标题")
    email = forms.EmailField(label="邮箱")
    message = forms.CharField(label="内容", widget=forms.Textarea)
    topic_choice = (
        ("1", "好评"),
        ("2", "中评"),
        ("3", "差评")
    )
    topic = forms.ChoiceField(label="评价", choices=topic_choice)
    issave = forms.BooleanField(label="是否保存")


class StudentForm(forms.ModelForm):
    name = forms.CharField(label="用户名：", required=True, error_messages={'required': "请输入姓名"})
    sex = forms.ChoiceField(label="性别：", choices=Student.GENDER_CHOICES, widget=forms.RadioSelect)
    age = forms.IntegerField(label="年龄：", required=True, error_messages={'required': "请输入年龄"},
                             widget=forms.NumberInput(attrs={'min': 1, 'max': 100}))
    address = forms.CharField(label="地址：", required=False, error_messages={'required': "请输入地址"},
                              widget=forms.TextInput(attrs={'placeholder': '请输入地址'}))
    enter_date = forms.DateField(label="入学日期：", required=False, error_messages={'required': "请输入入学日期"},
                                 widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])
    # 班级 多选
    class_choice = (
        ("1", "1班"),
        ("2", "2班"),
        ("3", "3班"),
        ("4", "4班"),
        ("5", "5班"),
        ("6", "6班"),
    )
    class_list = forms.MultipleChoiceField(label="班级：", choices=class_choice, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = ['name', 'sex', 'age', 'address', 'enter_date']
