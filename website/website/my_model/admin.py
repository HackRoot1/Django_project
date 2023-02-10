from django.contrib import admin
from my_model.models import MyModel
# Register your models here.

class UserModel(admin.ModelAdmin):
    list_display = ('classes', 'class_name','semester', 'subjects','subject_link')


admin.site.register(MyModel, UserModel)