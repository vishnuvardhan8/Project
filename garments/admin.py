from django.contrib import admin
from garments.models import Formalshirt,Casualshirt,Tshirt,Trouser,Jean,Trackpant

class FormalshirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

class CasualshirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

class TshirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

class TrouserAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

class JeanAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

class TrackpantAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')


# Register your models here.

admin.site.register(Formalshirt,FormalshirtAdmin)
  
admin.site.register(Casualshirt,CasualshirtAdmin)

admin.site.register(Tshirt,TshirtAdmin)

admin.site.register(Trouser,TrouserAdmin)

admin.site.register(Jean,JeanAdmin)

admin.site.register(Trackpant,TrackpantAdmin)