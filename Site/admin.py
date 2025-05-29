from django.contrib import admin

from Site.models import Aluquel, Cliente, FaleConosco, MotivoContato

# Register your models here.
admin.site.register(MotivoContato)
admin.site.register(FaleConosco)
admin.site.register(Aluquel)
admin.site.register(Cliente)