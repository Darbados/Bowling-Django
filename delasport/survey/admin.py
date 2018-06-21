from django.contrib import admin
from models import Survey


class SurveyAdmin(admin.ModelAdmin):
    model = Survey

    class Meta:
        list_display = ('status', 'created_at')


admin.site.register(Survey, SurveyAdmin)

