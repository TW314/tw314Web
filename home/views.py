from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template.context import RequestContext

import json

from pip._vendor import requests
from .forms import *
from .models import *


# Index
def index(request):
    return render(request, 'home/index.html', {})


# Login
def login(request):
    return render(request, 'home/login.html', {})


# Admin

# Principal
def admin_principal(request):
    return render(request, 'home/admin/admin_principal.html', {})


# Cadastro de Usuario
def admin_cadastro_usuario(request):
    if request.method == "POST":
        form = UsuFormAdmin(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            status_ativacao = form.cleaned_data['status_ativacao']
            data_inativacao = form.cleaned_data['data_inativacao']
            data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao, 'data_inativacao': data_inativacao, 'perfilId': 3, 'empresaId': 1}
            form = requests.post('http://localhost:3000/usuario', json=data)

    else:
        form = UsuFormAdmin()

    fun = requests.get('http://localhost:3000/usuario/perfil/3').json()

    return render(request, 'home/admin/admin_cadastro_funcionario.html',
                  {'fun': fun, 'form': form})


# Relatorio
def admin_relatorio(request):
    return render(request, 'home/admin/admin_relatorio.html', {})


# Cadastro de Servico
def admin_cadastro_servico(request):
    return render(request, 'home/admin/admin_insere_servico.html', {})


# Contatar suporte
def admin_suporte(request):
    return render(request, 'home/admin/admin_contatar_suporte.html', {})


# Sobre
def admin_sobre(request):
    return render(request, 'home/admin/admin_sobre.html', {})


# Suporte

# Principal
def suporte_princpal(request):
    return render(request, 'home/suporte/suporte_principal.html', {})


# Cadastro de Estabelecimento
def suporte_cadastro_estabelecimento(request):
    # Cadastro
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            nome_fantasia = form.cleaned_data['nome_fantasia']
            razao_social = form.cleaned_data['razao_social']
            numero_cnpj = form.cleaned_data['numero_cnpj']
            logradouro = form.cleaned_data['logradouro']
            numero_logradouro = form.cleaned_data['numero_logradouro']
            cidade = form.cleaned_data['cidade']
            uf = form.cleaned_data['uf']
            cep = form.cleaned_data['cep']
            pais = form.cleaned_data['pais']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            nome_responsavel = form.cleaned_data['nome_responsavel']
            cargo_responsavel = form.cleaned_data['cargo_responsavel']
            cpf_responsavel = form.cleaned_data['cpf_responsavel']
            data_abertura = form.cleaned_data['data_abertura']
            data_inativacao = form.cleaned_data['data_inativacao']
            status_ativacao = form.cleaned_data['status_ativacao']
            ramo_atividade = form.cleaned_data['ramo_atividade']
            data={'nome_fantasia': nome_fantasia, 'razao_social': razao_social, 'numero_cnpj': numero_cnpj, 'logradoro': logradouro, 'numero_logradouro': numero_logradouro, 'cidade': cidade, 'uf': uf, 'cep': cep, 'pais': pais, 'telefone': telefone, 'email': email, 'nome_responsavel': nome_responsavel, 'cargo_responsavel': cargo_responsavel, 'cpf_responsavel': cpf_responsavel, 'data_abertura': data_abertura, 'data_inativacao': data_inativacao, 'status_ativacao': status_ativacao, 'ramoAtividadeId': ramo_atividade }
            form = requests.post('http://localhost:3000/empresa', json=data)


    else:
        form = EmpForm()

    # LISTAR EMPRESAS
    ramos = requests.get('http://localhost:3000/ramoAtividade').json()
    empresas = requests.get('http://localhost:3000/empresa').json()

    return render(request, 'home/suporte/suporte_cadastro_estabelecimento.html',
                  {'empresas': empresas, 'ramos': ramos, 'form': form})


def suporte_editar_estabelecimento(request, pk):
    # Editar
    empresas = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        form = EmpForm(request.POST, instance=empresas)
        if form.is_valid():
            empresas = form
            empresas.save()
            return redirect('/suporte/cadastro_estabelecimento')

    ramos = RamoAtividade.objects.filter(status=1)
    return render(request, 'home/suporte/suporte_editar_estabelecimento.html', {'empresas': empresas, 'ramos': ramos})


def suporte_listar_empresas(request):
    # Lista
    # listagem de status ordenado por nome
    list_empresa = Empresa.objects.order_by('nome_fantasia')
    paginator = Paginator(list_empresa, 5)  # 5 dados por pagina

    page = request.GET.get('page')

    try:
        empresas = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        empresas = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        empresas = paginator.page(paginator.num_pages)

    return empresas


# Cadastro de Servico no suporte
def suporte_cadastro_servico(request):
    # Cadastro
    if request.method == "POST":
        form = SvcForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            sigla = form.cleaned_data['sigla']
            status_ativacao = form.cleaned_data['status_ativacao']
            data = {'nome': nome, 'descricao': descricao, 'sigla': sigla,
                    'status_ativacao': status_ativacao}
            form = requests.post('http://localhost:3000/servico/', json=data)
    else:
        form = SvcForm()

    servicos = requests.get('http://localhost:3000/servico/').json()
    ram = requests.get('http://localhost:3000/ramoAtividade').json()

    return render(request, 'home/suporte/suporte_cadastro_servico.html',
                  {'servicos': servicos, 'ram': ram, 'form': form})


def suporte_editar_servicos(request, pk):
    # Editar
    servicos = get_object_or_404(Servico, pk=pk)
    if request.method == "POST":
        form = SvcForm(request.POST, instance=servicos)
        if form.is_valid():
            servicos = form
            servicos.save()
            return redirect('/suporte/cadastro_servico')

    ramos = RamoAtividade.objects.filter(status=1)
    return render(request, 'home/suporte/suporte_editar_servicos.html', {'servicos': servicos, 'ramos': ramos})


def suporte_listar_servico(request):
    # Lista
    # listagem de servico ordenado por nome
    list_servico = Servico.objects.order_by('nome')
    paginator = Paginator(list_servico, 5)  # 5 dados por pagina

    page = request.GET.get('page')

    try:
        servico = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        servico = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        servico = paginator.page(paginator.num_pages)

    return servico


def suporte_cadastro_status(request):
    # Cadastro

    if request.method == "POST":
        form = StsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StsForm()

    status = suporte_listar_status(request)

    return render(request, 'home/suporte/suporte_cadastro_status.html',
                  {'status': status, 'form': form})


def suporte_listar_status(request):
    # Lista
    # listagem de status ordenado por nome
    list_status = Status.objects.order_by('nome')
    paginator = Paginator(list_status, 5)  # 5 dados por pagina

    page = request.GET.get('page')

    try:
        status = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        status = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        status = paginator.page(paginator.num_pages)

    return status


def suporte_editar_status(request, pk):
    # Editar
    status = get_object_or_404(Status, pk=pk)
    if request.method == "POST":
        form = StsForm(request.POST, instance=status)
        if form.is_valid():
            status = form
            status.save()
            return redirect('/suporte/status/')
    return render(request, 'home/suporte/suporte_editar_status.html', {'status': status})


def suporte_cadastro_ramo(request):
    # Cadastro
    if request.method == "POST":
        form = RamForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            status = form.cleaned_data['status_ativacao']
            data = {'nome': nome, 'descricao': descricao, 'status_ativacao': status}
            form = requests.post('http://localhost:3000/ramoAtividade', json=data)

    else:
        form = RamForm()

        ramos = requests.get('http://localhost:3000/ramoAtividade').json()

    return render(request, 'home/suporte/suporte_cadastro_ramo.html', {'form': form, 'ramos': ramos})


def suporte_editar_ramos(request, pk):
    # Editar
    ramos = get_object_or_404(RamoAtividade, pk=pk)
    if request.method == "POST":
        form = RamForm(request.POST, instance=ramos)
        if form.is_valid():
            ramos = form
            ramos.save()
            return redirect('/suporte/cadastro_ramos')
    return render(request, 'home/suporte/suporte_editar_ramos.html', {'ramos': ramos})


def suporte_listar_ramo(request):
    # Lista
    list_ramo = RamoAtividade.objects.order_by(
        'nome')  # listagem de ramo ordenado por nome
    paginator = Paginator(list_ramo, 5)  # 5 dados por pagina

    page = request.GET.get('page')

    try:
        ramos = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        ramos = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        ramos = paginator.page(paginator.num_pages)

    return ramos


def suporte_cadastro_usuario(request):
    # Cadastro

    if request.method == "POST":
        form = UsuFormSuporte(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            status_ativacao = form.cleaned_data['status_ativacao']
            data_inativacao = form.cleaned_data['data_inativacao']
            empresa = form.cleaned_data['empresa']
            data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao,
                    'data_inativacao': data_inativacao, 'empresaId': empresa, 'perfilId': 2}
            form = requests.post('http://localhost:3000/usuario', json=data)
    else:
        form = UsuFormSuporte()

    # listar usuarios
    admins = requests.get('http://localhost:3000/usuario/2').json()
    estabelecimentos = requests.get('http://localhost:3000/empresa').json()

    return render(request, 'home/suporte/suporte_cadastro_admin.html',
                  {'admins': admins, 'estabelecimentos': estabelecimentos, 'form': form})


def suporte_listar_usuario(request):
    """
    # Lista
    list_usuario = Usuario.objects.order_by('nome').exclude(perfil=1)  # listagem de ramo ordenado por nome
    paginator = Paginator(list_usuario, 5)  # 5 dados por pagina

    page = request.GET.get('page')

    try:
        usuario = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        usuario = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        usuario = paginator.page(paginator.num_pages)
    """
    """
    api = API('http://localhost:3000/consultaUsuariosPorPerfil/2')
    # lista = API.pessoas.get()
    list_admin = api.get('consultaUsuariosPorPerfil', 'id')

    return render_to_response('home/suporte/suporte_cadastro_admin.html', {'list_admin': list_admin}, context_instance=RequestContext(request))

    lista = user_admin(2)
    return render(request, 'home/suporte/suporte_cadastro_admin.html', lista)
    """


# Atendimento
def suporte_atendimento(request):
    return render(request, 'home/suporte/suporte_atendimento.html', {})


# ???
def demo_chart(request):
    return render(request, 'home/demo_chart.html', {})


# Funcionario

# Principal
def funcionario_principal(request):
    return render(request, "home/funcionario/funcionario_principal.html", {})


# Relatorio
def funcionario_relatorio(request):
    return render(request, 'home/funcionario/funcionario_relatorio.html', {})


# Sobre
def funcionario_sobre(request):
    return render(request, 'home/funcionario/funcionario_sobre.html', {})


# Contatar suporte
def funcionario_suporte(request):
    return render(request, 'home/funcionario/funcionario_contatar_suporte.html', {})
