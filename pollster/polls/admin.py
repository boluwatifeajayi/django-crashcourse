from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Pollster admin"
admin.site.site_title = "Pollster admin area"
admin.site.index_title = "welcome to pollster admin aerea"

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    feildsets = [(None, {'feilds': ['question_text']}),
    ('Date Information', {'feilds': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

# Register your models here.

admin.site.register(Question, QuestionAdmin)
