from django.contrib import admin
from .models import Submission, Attempt


class AttemptInline(admin.TabularInline):
    model = Attempt
    extra = 0
    readonly_fields = ("part",)


class SubmissionAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    fieldsets = (
        (None, {
            'fields': (('user', 'problem', 'ip'), )
        }),
        ('Source', {
            'classes': ('collapse', ),
            'fields': ('preamble',)
        })
    )
    inlines = [AttemptInline]
    list_display = ('timestamp', 'user', 'course', 'problem_set', 'problem')
    list_filter = ('problem__problem_set__course',)
    search_fields = ['user__username', 'problem__title', 'problem__problem_set__title']

    def course(self, obj):
        return obj.problem.problem_set.course
    course.admin_order_field = 'problem__problem_set__course'

    def problem_set(self, obj):
        return obj.problem.problem_set
    problem_set.admin_order_field = 'problem__problem_set'

admin.site.register(Submission, SubmissionAdmin)
