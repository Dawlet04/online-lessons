from django.contrib import admin
from .models import Roles, Users, Teachers, Payment, Enrollments, Categories, Courses,Lessons, Lesson_progress, Review

admin.site.register(Roles)
admin.site.register(Users)
admin.site.register(Lesson_progress)
admin.site.register(Lessons)
admin.site.register(Enrollments)
admin.site.register(Payment)
admin.site.register(Teachers)
admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(Review)
# Register your models here.
