from django.contrib import admin
from .models import Job,Category,Aplly

# Register your models here.
admin.site.site_header = "BOARD Admin"
admin.site.site_title = "BOARD Admin Portal"
admin.site.index_title = "Welcome to BOARD Researcher Portal"
class ApllyAdmin(admin.ModelAdmin):
    list_display = ['name','job','created_at']

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Aplly,ApllyAdmin)

