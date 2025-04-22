from django.contrib import admin
from chamadaApp.models import Cliente, Categoria, Telefone, Plano

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Telefone)
admin.site.register(Plano)