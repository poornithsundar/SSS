"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from question.views import home_page,about_us_page,contact_page,login_page,exam_page,logout_page,index_page,countdown_page,quiz_page,signup,sub_page,result_page
from question.forms import LoginForm

urlpatterns = [
	path('',home_page,name='home'),
	path('home/',home_page,name='home'),
    path('index/',index_page,name='index'),
	path('about/',about_us_page,name='about'),
	path('contact/',contact_page,name='contact'),
    path('login/',login_page,{'authentication_form':LoginForm},name='login'),
    path('exam/',exam_page,name='exam'),
    path('quiz/',quiz_page,name='quiz'),
    path('admin/', admin.site.urls),
    path('logout/', logout_page, {'templete_name': 'logout.html'}, name='logout'),
    path('countdown/',countdown_page,name='countdown'),
    path('signup/',signup,name='signup'),
    path('add_data/', sub_page, name='sub'),
    path('result/', result_page, name='res'),
]
