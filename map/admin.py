from django.contrib import admin
from .models import insertddl
from .models import Test
from .models import insertgraph
from .models import insertgraph2

# Register your models here.
admin.site.register(insertddl)
admin.site.register(Test)
admin.site.register(insertgraph)
admin.site.register(insertgraph2)