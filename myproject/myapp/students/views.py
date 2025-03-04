import json

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin

from ..models import Student
from ..utils.json_utils import DateEncoder
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html")

@xframe_options_sameorigin
def get_students_page(request):
    students = Student.objects.all()
    if request.GET.get('name'):
        students = students.objects.filter(name__icontains=request.GET.get('name'))
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
    if end_date is not None:  # 结束日期
        students = students.filter(enter_date__lte=end_date)

    data_count = students.count()
    page_num = request.GET.get('pageNum', 1)  # 获取页码，默认为1
    page_size = request.GET.get('pageSize', 2)  # 获取每页显示的条数，默认为10
    print("当前索引:{} 当前大小:{}".format(page_num, page_size))
    print("所有记录:{} 数据总条数:{}".format(students, data_count))

    # 使用Django内置的Paginator类对查询集进行分页
    paginator = Paginator(students, page_size)
    # 尝试获取指定页码的页面对象
    try:
        # 如果请求的页码存在，则获取该页数据
        page_obj = paginator.page(page_num)
    except EmptyPage:
        # 如果请求的页码不存在（或者超过了总页数），则返回第一页数据
        page_obj = paginator.page(1)
    except InvalidPage:
        # 如果请求的页码无效，则返回第一页数据
        page_obj = paginator.page(1)
    # 序列化数据
    # data_list = list(data.values())  # 或者使用 serializers.serialize('json', data)
    data_list = list(page_obj.object_list.values(
        'id', 'name', 'age', 'sex', 'address', 'enter_date'
    ))

    # 创建一个响应数据字典，包含分页数据和分页相关信息
    response_data = {
        'code': 0,  # 0通常表示请求处理成功，具体编码规则根据项目约定
        'msg': 'success',  # 明确的成功消息文本
        'data': data_list,  # 当前页实际的业务数据
        'count': paginator.count,  # 总记录数，即数据库中符合条件的所有记录的数量
        'current_page': page_obj.number,  # 当前请求的页码
        'per_page': page_size,  # 每页显示的记录数
        'total_pages': paginator.num_pages,  # 总页数，由总记录数除以每页记录数得出
    }

    # 将响应数据封装成JsonResponse返回给前端
    return JsonResponse(response_data)


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
