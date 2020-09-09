from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    #list_play :控制列表页面展示那些字段
    list_display = ('id','name','sex','profession','email','qq','phone','status','created_time')
    #list_filter : 配置页面过滤器，需要通过那些字段来过滤列表页，
    list_filter = ('sex','status','created_time')
    #search_fields: 配置搜索字段
    search_fields = ('name','profession')
    fieldsets = (
        (None,{
            'fields':(
                'name',
                ('sex','profession'),
                ('email','qq','phone'),
                'status'
            )
        }),

        )
admin.site.register(Student,StudentAdmin)