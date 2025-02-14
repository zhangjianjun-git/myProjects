from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import LoginForm, RegisterForm, UserLoginForm, UserRegisterForm
from .models import *


def index(request):
    print("hello world")
    return render(request, "index.html", locals())


def login_views(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", locals())
    else:
        uname = request.POST["username"]
        upwd = request.POST["password"]
        # 查找数据库中用户名为uname的用户。如果找不到对应的用户，会抛出DoesNotExist异常。
        try:
            user = Users.objects.get(username=uname)
        except Users.DoesNotExist as e:
            errmsg = "用户不存在"
            form = LoginForm()
            return render(request, 'index.html', {'form': form})
        if user:
            if user.password == upwd:
                return HttpResponse("验证通过")
            else:
                errmsg = "密码错误"
                form = LoginForm()
                return render(request, "index.html", locals())
        else:
            errmsg = "用户名错误"
            form = LoginForm()
            return render(request, "index.html", {'form': form})


def login_auto_views(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "index.html", {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            uname = data["username"]
            upwd = data["password"]
            user = Users.objects.filter(username=uname).first()
            return HttpResponse("验证通过")
        else:
            # 如果GET请求或表单不合法，显示表单
            return render(request, 'index.html', {'form': form})


def login_form_views(request):
    if request.method == "GET":
        form = UserLoginForm()
        return render(request, "login_form.html", locals())
    else:
        uname = request.POST["username"]
        password = request.POST["password"]
        try:
            user = Users.objects.get(username=uname)
        except:
            errmsg = "用户不存在"
            return redirect("../register/")

        if user:
            if user.password == password:
                return HttpResponse("验证通过")
            else:
                errmsg = "密码"
                form = UserLoginForm()
                return render(request, "login.html", locals())
        else:
            errmsg = "用户名错误"
            form = UserLoginForm()
            return render(request, "login.html", locals())


def register_views(request):
    if request.method == "GET":
        forms = RegisterForm()
        return render(request, "register.html", locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            uname = data["username"]
            upward = data["password"]
            age = data["age"]
            email = data["email"]
            user = Users.objects.filter(username=uname).first()
            if user:
                errmsg = "用户名已存在"
                return render(request, "register.html", locals())
            else:
                user = Users(username=uname, password=upward, age=age, email=email)
                user.save()
                # Users(**data).save()
                return HttpResponse("注册成功")


def regiter_form_views(request):
    if request.method == "GET":
        form = UserRegisterForm()
        return render(request, "register_form.html", locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            uname = data["username"]
            password = data["password"]
            age = data["age"]
            email = data["email"]
            user = Users.objects.filter(username=uname).first()
            if user:
                errmsg = "用户名已存在"
                return render(request, "register.html", locals())
            else:
                user = Users(username=uname, password=password, age=age, email=email)
                user.save()
                # Users(**data).save()
                return HttpResponse("注册成功")


# 学生管理系统视图函数
def student_list(request):
    student_queryset = models.Student.objects.all()
    return render(request, "student_list.html", {"student_queryset": student_queryset})


def student_detail(request, pk):
    student_obj = models.Student.objects.get(id=pk)
    return render(request, "student_detail.html", {"student_obj": student_obj})


# 定义一个函数，根据学生id删除学生信息
def student_delete(request, pk):
    student_obj = models.Student.objects.get(id=pk)
    student_obj.delete()  # 删除学生信息
    return HttpResponse("删除成功！")  # 返回一个删除成功的提示信息


# 定义一个函数，根据学生id修改学生信息
def student_update(request, pk):
    student_obj = models.Student.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        student_obj.name = name
        student_obj.age = age
        student_obj.gender = gender
        student_obj.save()  # 保存修改后的信息
        return HttpResponse("修改成功！")  # 返回一个修改成功的提示信息
    else:
        return render(request, "student_update.html", {"student_obj": student_obj})  # 跳转到修改页面


# 定义一个函数，添加学生信息
def student_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        student_obj = models.Student(name=name, age=age, gender=gender)

        student_obj.save()  # 保存新增的学生信息
        return HttpResponse("添加成功！")  # 返回一个添加成功的提示信息
    else:
        return render(request, "student_add.html")  # 跳转到添加页面
