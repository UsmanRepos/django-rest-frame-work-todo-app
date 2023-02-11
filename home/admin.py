from django.contrib import admin
from home.models import BaseModel, Todo, Time

admin.site.register(BaseModel)
admin.site.register(Todo)
admin.site.register(Time)


