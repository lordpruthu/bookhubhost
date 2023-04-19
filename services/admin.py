from django.contrib import admin
from .models import Services
from .models import PDFFile
from .models import Form

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['subject','book','author']

admin.site.register(Services,ServicesAdmin)

class PDFFileAdmin(admin.ModelAdmin):
    list_display = ['file','filename','title']

admin.site.register(PDFFile,PDFFileAdmin)

class FormAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Subject','Message')

admin.site.register(Form,FormAdmin)
