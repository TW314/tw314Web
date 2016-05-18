from django.shortcuts import render


#Index
def index(request):
    return render(request, 'home/index.html', {})

#Login
def login(request):
    return render(request, 'home/login.html', {})


#Admin
def admin_principal(request):
    return render(request, 'home/admin/admin_principal.html', {})


def cadastro_usuario(request):
    return render(request, 'home/admin/cadastrar_usuario.html', {})


def relatorio(request):
    return render(request, 'home/admin/relatorio.html', {})


def cadastro_servico(request):
    return render(request, 'home/admin/cadastro_servico.html', {})

def contatar_suporte(request):
    return render(request, 'home/admin/contatar_suporte.html', {})


#Suporte
def suporte_princpal(request):
    return render(request, 'home/suporte/suporte_principal.html', {})


def cadastro_admin(request):
    return render(request, 'home/suporte/cadastro_admin.html', {})


def cadastro_estabelecimento(request):
    return render(request, 'home/suporte/cadastro_estabelecimento.html', {})


def suporte_atendimento (request):
    return  render(request, 'home/suporte/suporte_atendimento.html', {})


#???
def demo_chart(request):
    return render(request, 'home/demo_chart.html', {})


#Funcionario
def funcionario_principal(request):
    return render(request, "home/funcionario/funcionario_principal.html", {})


#Sobre
def sobre(request):
    return  render(request, 'home/funcionario/sobre.html', {})


