from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student
from django.core.paginator import Paginator
from django.views.decorators.clickjacking import xframe_options_sameorigin


@xframe_options_sameorigin
def student_list(request):
    students = Student.objects.all()
    if request.GET.get('name'):
        students = students.filter(name__icontains=request.GET.get('name'))
    if request.GET.get('age'):
        students = students.filter(age=request.GET.get('age'))
    if request.GET.get('sex'):
        students = students.filter(sex=request.GET.get('sex'))

    enter_date_range = request.GET.get('enter_date_range', '')
    if enter_date_range:
        # 使用 ' - ' 分割字符串，获取开始日期和结束日期
        start_date, end_date = enter_date_range.split(' - ')
        # 这里 start_date 和 end_date 就是具体的日期字符串
        # 你可以根据需要将它们转换为日期对象或者其他格式
        # 例如：
        # start_date = datetime.strptime(start_date, '%Y-%m-%d')
        # end_date = datetime.strptime(end_date, '%Y-%m-%d')
    else:
        # 如果没有选择日期范围，则 start_date 和 end_date 为 None 或者默认值
        start_date = None
        end_date = None
    if start_date is not None:  # 起始日期
        students = students.filter(enter_date__gte=start_date)
    if end_date is not None:   # 结束日期
        students = students.filter(enter_date__lte=end_date)
    page = request.GET.get('page', 1)  # 获取页码，默认为1
    limit = request.GET.get('limit', 2)  # 获取每页显示的条数，默认为10
    paginator = Paginator(students, limit)
    page_obj = paginator.get_page(page)
    return render(request, 'students/student_list.html', {
        'students': page_obj,
        'total_students': paginator.count,
        'per_page': limit,
        'current_page': page_obj.number,
    })


# 定义一个函数，添加学生信息
def student_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        student_obj = Student(name=name, age=age, gender=gender)

        student_obj.save()  # 保存新增的学生信息
        return HttpResponse("添加成功！")  # 返回一个添加成功的提示信息
    else:
        return render(request, "student_add.html")


# 定义一个函数，根据学生id修改学生信息
def student_update(request, pk):
    student_obj = Student.objects.get(id=pk)
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


# 定义一个函数，根据学生id删除学生信息
def student_delete(request, pk):
    student_obj = Student.objects.get(id=pk)
    student_obj.delete()  # 删除学生信息
    return HttpResponse("删除成功！")  # 返回一个删除成功的提示信息


def student_detail(request, pk):
    student_obj = Student.objects.get(id=pk)
    return render(request, "student_detail.html", {"student_obj": student_obj})
