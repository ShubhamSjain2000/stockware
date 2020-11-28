from django.contrib import admin
from .models import Indices
from .models import Traders
from .models import Holdings
from .models import Scripts
from .models import GlobalIndices
from .models import Researches

# Register your models her
class UserAdmin(admin.ModelAdmin):
    list_display=('name','price')
admin.site.register(Indices)
admin.site.register(Traders)
admin.site.register(Holdings)

admin.site.register(Scripts)
admin.site.register(GlobalIndices)
admin.site.register(Researches)