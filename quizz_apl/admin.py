from django.contrib import admin

# Register your models here.
from django.contrib import admin
from quizz_apl.models import Quiz,Answer,Question

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answer, AuthorAdmin)