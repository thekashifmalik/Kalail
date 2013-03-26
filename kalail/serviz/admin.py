from django.contrib import admin

from .models import ModuleType, Module, Cache, ServiceType, Service, Server


admin.site.register(ModuleType)
admin.site.register(Module)
admin.site.register(Cache)
admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(Server)
