from django.contrib import admin
from .models import Role, Users, Teacher, Payment, Enrollment, Category, Course, LessonProgress, Review, Lesson

admin.site.register(Role)
admin.site.register(Users)
admin.site.register(LessonProgress)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Payment)
admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Review)
# Register your models here.
