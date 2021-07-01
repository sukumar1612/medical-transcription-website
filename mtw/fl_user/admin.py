from django.contrib import admin
from fl_user.models import Job_status
from login.models import User
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import ngettext
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('Doctor_user','date_submitted','duration','assign_first_level_user','is_asigned','transcription_completed', 'QA_passed', 'feedback_given')
    search_fields = ('Doctor_user__email','Doctor_user__fullname')
    readonly_fields=()

    ordering = ('date_submitted',)
    filter_horizontal = ()
    list_filter = ('date_submitted',)
    fieldsets = ()

    change_list_template = 'admin/fl_user/job_status_change_list.html'

    def assign_multiple_jobs_to_users(self, request, queryset):
        # print('hello world')
        # self.message_user(request, ngettext(
        #      '%d story was successfully marked as published.',
        #      '%d stories were successfully marked as published.',
        #     3,
        # ) % 3, messages.SUCCESS)

        if request.method == 'POST' and 'apply' in request.POST.dict().keys():
            request.POST.getlist('_selected_action')
            for i in request.POST.getlist('_selected_action'):
                j=Job_status.objects.get(job_id = int(i))
                j.assign_first_level_user = User.objects.get(email=request.POST.get('fl_user'))
                j.assign_second_level_user = User.objects.get(email=request.POST.get('sl_user'))
                j.is_asigned = True
                j.save()
            self.message_user(request,
                                  "Changed status on {} orders".format(len(request.POST.getlist('_selected_action'))))
            return HttpResponseRedirect(request.get_full_path())

        return render(request, 'admin/fl_user/assign_multiple_jobs_to_users_intermediate_page.html',
                      context={'jobs': queryset, 'fluser': User.objects.filter(user_designation='first level user'),
                               'sluser': User.objects.filter(user_designation='second level user')})

    actions = [assign_multiple_jobs_to_users]

admin.site.register(Job_status, CustomUserAdmin)
