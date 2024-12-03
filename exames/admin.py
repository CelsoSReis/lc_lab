from django.contrib import admin
from .models import TiposExames, PedidosExames, SolicitacaoExame, AcessoMedico

# Register your models here.(area Admin)
admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)
admin.site.register(AcessoMedico)