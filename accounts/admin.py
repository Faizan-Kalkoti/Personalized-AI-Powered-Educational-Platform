from django.contrib import admin

# Register your models here.
from accounts.models import Teacher, Student, OTPverification


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(OTPverification)
# Register your models here.