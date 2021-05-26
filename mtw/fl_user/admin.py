from django.contrib import admin
from fl_user.models import Job_status
from django.contrib import admin
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('doctor_name','date_submitted','assign_first_level_user','is_asigned','transcription_completed', 'QA_passed')
    search_fields = ('doctor_name',)
    readonly_fields=()

    ordering = ('date_submitted',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Job_status, CustomUserAdmin)