# Register your models here.
from django.contrib import admin

from django import forms
from .models import Student, Class, Teacher
from django.utils.html import format_html

admin.site.site_header = "学管理系统"
admin.site.site_title = "学管理系统"
admin.site.index_title = "欢迎使用学管理系统"

class StudentForm(forms.ModelForm):
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 6 or age > 20:
            raise forms.ValidationError('年龄必须在6到20岁之间')
        return age

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['sex'].choices = [('', '请选择')] + list(Student.GENDER_CHOICES)
        self.fields['sclass'].queryset = Class.objects.all()

# 定义一个Student的管理类
class StudentAdmin(admin.ModelAdmin):
    # 使用自定义的ModelForm
    form = StudentForm
    # 指定在列表视图中显示的字段
    list_display = ('name', 'sex', 'age', 'address', 'enter_date', 'sclass')

    list_per_page = 5  # 每页显示5条记录

    # 为班级字段添加一个自定义的显示名称
    def sclass_name(self, obj):
        return obj.sclass.name if obj.sclass else '未分配班级'

    # 定义一个自定义方法，用于显示图片
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '未上传图片'

    # 将自定义方法添加到list_display中
    list_display = ('name', 'sex', 'age', 'address', 'enter_date', 'sclass_name','display_image')

    # 添加搜索字段，允许用户通过这些字段搜索
    search_fields = ('name','sex', 'age', 'address', 'enter_date', 'sclass__name')  # 注意：使用双下划线来跨越关系字段

    # 添加list_filter，允许用户通过这些字段过滤
    #list_filter = ('name','sex', 'age', 'sclass', 'enter_date')  # 过滤条件可以是字段名或自定义过滤器

    # 设置自定义方法的显示名称
    sclass_name.short_description = '班级名称'
    display_image.short_description = '照片'

    # 重写formfield_for_foreignkey方法
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sclass":
            kwargs["empty_label"] = "请选择"
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # 自定义搜索方法（将性别中文名转换为代码进行搜索）
    def get_search_results(self, request, queryset, search_term):
        # 调用父类的get_search_results方法获取初始的查询集
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        # 检查搜索字段中是否包含'sex'并且搜索词是'男'
        if 'sex' in self.search_fields and search_term == '男':
            queryset = Student.objects.filter(sex='male')
            use_distinct = True
        elif 'sex' in self.search_fields and search_term == '女':
            queryset = Student.objects.filter(sex='female')
            use_distinct = True
        return queryset, use_distinct

class ClassAdmin(admin.ModelAdmin):
    filter_horizontal = ('teacher',)  # 使用filter_horizontal进行水平过滤
    # filter_vertical = ('teacher',)  # 使用filter_vertical进行垂直过滤
    list_per_page = 5  # 每页显示5条记录
    # 为teacher字段添加一个自定义的显示名称，因为teacher是一个外键，这里需要自定义一个方法来显示所有关联的老师
    def teacher_list(self, obj):
        return ", ".join([teacher.name for teacher in obj.teacher.all()])
    def buttons(self, obj):
        button_html = """<a class="changelink" href="/admin/myapp/class/%s/change/">编辑</a>""" % obj.id
        button_html += """&nbsp;&nbsp;<a class="deletelink" href="/admin/myapp/class/%s/delete/">删除</a>""" % obj.id
        return format_html(button_html,obj.id)

    buttons.short_description = "操作"
    # 指定在列表视图中显示的字段
    list_display = ('name', 'grade', 'teacher_list', 'buttons')
    buttons.short_description = "操作"
    # 设置自定义方法的显示名称
    teacher_list.short_description = '老师列表'

class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 5  # 每页显示5条记录
    list_display = ('name', 'sex', 'age', 'address')

    def buttons(self, obj):
        button_html = """<a class="changelink" href="/admin/myapp/teacher/%s/change/">编辑</a>""" % obj.id
        button_html += """&nbsp;&nbsp;<a class="deletelink" href="/admin/myapp/teacher/%s/delete/">删除</a>""" % obj.id
        return format_html(button_html,obj.id)

    buttons.short_description = "操作"
    list_display = ('name', 'sex', 'age', 'address', 'buttons')

# 注册模型和管理类
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)

# 使用装饰器来注册模型
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Student,StudentAdmin)
# class StudentAdmin(admin.ModelAdmin):
#     pass