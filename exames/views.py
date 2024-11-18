from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TiposExames, PedidosExames, SolicitacaoExame
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants

@login_required
def solicitar_exames(request):
    #Lista exames no select para o usuário selecionar
    tipos_exames = TiposExames.objects.all()
    if request.method == "GET":
        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})
    elif request.method == "POST":
        # atributo "getlist" seleciona vários valores, "get" somente um valor
        exames_id = request.POST.getlist('exames')
        # verifica no banco de dados informações dos exames selecionados pelo usuário
        solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
        #preco_total = solicitacao_exames.aggregate(total=Sum('preco'))['total']
        ## Calcula valor total dos exames selecionados pelo usuário
        preco_total = 0
        for i in solicitacao_exames:
            #Condição soma preço só se estiver disponível
            if i.disponivel:
                preco_total += i.preco
        
        return render(request, 'solicitar_exames.html', {'solicitacao_exames': solicitacao_exames, 'preco_total': preco_total, 'tipos_exames': tipos_exames})
    
@login_required
def fechar_pedido(request):
    exames_id = request.POST.getlist('exames')
    #busca tipos de exames
    solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)
    #pedido de exame
    pedido_exame = PedidosExames(
        usuario = request.user,
        data = datetime.now()
    )
    #método save(), salva no banco de dados
    pedido_exame.save()

    for exame in solicitacao_exames:
        solicitacao_exames_temp = SolicitacaoExame(
            usuario=request.user,
            exame=exame,
            status="E"
        )
        solicitacao_exames_temp.save()
        pedido_exame.exames.add(solicitacao_exames_temp)
        
    pedido_exame.save()

    messages.add_message(request, constants.SUCCESS, 'Pedido de exame concluído com sucesso')
    return redirect('/exames/gerenciar_pedidos/')

@login_required
def gerenciar_pedidos(request):
    #Filtra todos os pedidos de exames do usuário logado
    pedidos_exames = PedidosExames.objects.filter(usuario=request.user)
    return render(request, 'gerenciar_pedidos.html', {'pedidos_exames': pedidos_exames})

##Cancelar pedidos
@login_required
def cancelar_pedido(request, pedido_id):
    pedido = PedidosExames.objects.get(id=pedido_id)

    if not pedido.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse pedido não é seu')
        return redirect('/exames/gerenciar_pedidos/')

    pedido.agendado = False
    pedido.save()
    messages.add_message(request, constants.SUCCESS, 'Pedido cancelado com sucesso')
    return redirect('/exames/gerenciar_pedidos/')

##Gerenciar exames

@login_required
def gerenciar_exames(request):
    exames = SolicitacaoExame.objects.filter(usuario=request.user)

    return render(request, 'gerenciar_exames.html', {'exames': exames})