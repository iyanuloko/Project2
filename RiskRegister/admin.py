from django.contrib import admin
from .models import RiskRegister, Category, Severity, RSev

class RiskRegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_dept', 'date', 'category', 'roles', 'responderID', 'severity',
                    'action_taken_explanation', 'created_at']
    list_filter = ['id', 'user', 'user__department', 'date', 'category', 'roles', 'responderID', 'severity', 'action_taken_explanation']
    search_fields = ['user__department']
    def user_dept(self, obj):
        return obj.user.department


admin.site.register(RiskRegister, RiskRegisterAdmin)

admin.site.register(Category)

admin.site.register(Severity)

admin.site.register(RSev)
