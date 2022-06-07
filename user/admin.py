from django.contrib import admin
from .models import *



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username',  'email']
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user',  'approve']


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Withdraw)
admin.site.register(Otp)
admin.site.register(Tran)

admin.site.register(Payment,PaymentAdmin)