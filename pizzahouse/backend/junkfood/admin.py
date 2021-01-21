from django.contrib import admin
from . models import Categories
from . models import Menus
from . models import Profiles
from . models import Supplements

# Register your models here.

admin.site.register(Categories)
admin.site.register(Menus)
admin.site.register(Profiles)
admin.site.register(Supplements)



