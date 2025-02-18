from django.conf import settings
from django.urls import include,re_path
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve
from .students import urls as students_urls
from .menu import urls as menu_urls
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('menus/', include(menu_urls)),
    path('register/', views.register_views),
    path('form_regiter/',views.regiter_form_views),
    path('login/', views.login_views),
    path('form_login/', views.login_form_views),
    path('login_auto/', views.login_auto_views),
    path('students/', include(students_urls)),
    # 上传media的文件可以被查看，这个很重要，更后边的一个bug有关
    path(r'media/(?P<path>.*)', serve,{'document_root': settings.MEDIA_ROOT}),
    # 添加ckeditor的url到项目中
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # 上传的图片是到media中，不是在static中 所以需要设置media可被访问
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
