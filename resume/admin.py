from django.contrib import admin
from .models import *


admin.site.register(Profile)
admin.site.register(Work_Experience)
admin.site.register(Education)


class SkillsInline(admin.TabularInline):
    model = Skills

class SkillsAdmin(admin.ModelAdmin):
    inlines = [SkillsInline]


admin.site.register(Resume , SkillsAdmin)
admin.site.register(Skills)