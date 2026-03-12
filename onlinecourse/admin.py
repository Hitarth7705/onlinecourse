from django.contrib import admin
from .models import Course, Lesson, Enrollment, Question, Choice, Submission
from django.contrib.auth.models import User
from .models import Instructor, Learner

admin.site.register(Instructor)
admin.site.register(Learner)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson', 'grade')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = [LessonInline] if 'LessonInline' in globals() else []


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
