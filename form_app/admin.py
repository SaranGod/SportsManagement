from django.contrib import admin
from .models import Admin_model,Owner_model,player
from guardian.admin import GuardedModelAdmin

class ownerperm(GuardedModelAdmin):
    {}
admin.site.register(Admin_model)
admin.site.register(Owner_model,ownerperm)
admin.site.register(player)

# Register your models here.
