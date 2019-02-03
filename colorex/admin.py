from django.contrib import admin
from colorex import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = (
        'user_name',
        'total_time_numeric',
        'level_1_time',
        'level_2_time',
        'level_3_time',
        'level_4_time',
        'level_5_time',
        'level_6_time',
        'level_7_time',
        'level_8_time',
        'level_9_time',
        'level_10_time'
    )
	#date_hierarchy = 'total_time_numeric'
	list_filter = ['user_name']
	search_fields = ['user_name']

admin.site.register(models.User, UserAdmin)