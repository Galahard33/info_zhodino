from django.contrib import admin

from .. import models

# Register your models here.
# To get django model: models.<ModelName>.DjangoModel

@admin.register(models.Test.DjangoModel)
class TestAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ScheduleBus.DjangoModel)
class ScheduleBusAdmin(admin.ModelAdmin):
    pass