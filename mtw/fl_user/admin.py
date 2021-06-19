from django.contrib import admin
from fl_user.models import Job_status
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('Doctor_user','date_submitted','assign_first_level_user','is_asigned','transcription_completed', 'QA_passed')
    search_fields = ('Doctor_user',)
    readonly_fields=()

    ordering = ('date_submitted',)
    filter_horizontal = ()
    list_filter = ('date_submitted',)
    fieldsets = ()

    change_list_template = 'admin/fl_user/job_status_change_list.html'

admin.site.register(Job_status, CustomUserAdmin)
