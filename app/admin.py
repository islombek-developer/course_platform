from django.contrib import admin
from .models import Comment, Course, Lesson, LikeVideo, Teacher, Program

@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('title', 'created', 'course')
    list_display_links = ('title',)
    list_editable = ('course',)
    list_filter = ('course',)
    search_fields = ('title',)

@admin.register(Program)
class AdminProgram(admin.ModelAdmin):
    list_display = ('name',)  
    list_display_links = ('name',)

@admin.register(Teacher)
class Adminteacher(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'program')
    list_display_links = ('first_name',)
    list_editable = ('program',)
    list_filter = ('program',)
    search_fields = ('first_name',)

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('program', 'price', 'author')
    list_display_links = ('price',)
    search_fields = ('program',)

admin.site.register(LikeVideo)
