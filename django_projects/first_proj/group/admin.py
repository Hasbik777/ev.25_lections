from django.contrib import admin

from .models import Teacher, Student, Group, GroupStudents

# Register your models here.


admin.site.register(Teacher)
admin.site.register(Student)
# admin.site.register(Group)
admin.site.register(GroupStudents)


@admin.register(Group)
class Gruops(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count_of_students', 'list_of_students')

    def count_of_students(self, obj):
        # print(obj, '!!!!!!')
        qs = GroupStudents.objects.filter(group_id=obj.id)
        # print(qs, '!!!!!!!!!!!!!!!')
        return qs.count()

    def list_of_students(self, obj):
        qs = GroupStudents.objects.filter(group_id=obj.id)
        res = []
        for x in qs:
            x = str(x)
            index = x.index(' -> ')
            res.append(x[:index])
        return res

