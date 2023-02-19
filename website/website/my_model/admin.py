from django.contrib import admin
from my_model.models import MyModel, classData, semData
# Register your models here.

class UserModel(admin.ModelAdmin):
    list_display = ('classes', 'class_name','semester', 'subjects','subject_link')

class ClassData(admin.ModelAdmin):
    list_display = ('classes')

class SemData(admin.ModelAdmin):
    list_display = ('sem')


admin.site.register(MyModel, UserModel)