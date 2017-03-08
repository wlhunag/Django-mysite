from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('原文', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
