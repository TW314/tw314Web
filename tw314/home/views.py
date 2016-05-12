from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {})


def cadastro_usuario(request):
    return render(request, 'home/admin/cadastrar_usuario.html', {})


def admin_principal(request):
    return render(request, 'home/admin/admin_principal.html', {})


def suporte_princpal(request):
    return render(request, 'home/suporte/suporte_principal.html', {})




def relatorio(request):
    return render(request, 'home/admin/relatorio.html', {})

def cadastro_admin(request):
    return render(request, 'home/suporte/cadastro_admin.html', {})


def demo_chart(request):
    return render(request, 'home/demo_chart.html', {})


