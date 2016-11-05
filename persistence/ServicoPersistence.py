from pip._vendor import requests

from form.servico import ServicoForm


def cadastra(servico):

    form = ServicoForm(servico)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        ramo_atividade = form.cleaned_data['ramo_atividade']
        sigla = form.cleaned_data['sigla']
        status_ativacao = form.cleaned_data['status_ativacao']
        data = {'nome': nome, 'descricao': descricao, 'ramo_atividade': ramo_atividade, 'sigla': sigla,
                'status_ativacao': status_ativacao}
        form = requests.post('http://localhost:3000/servico/', json=data)
    else:
        form = "Campos de Serviço não preenchido corretamente"

    return form


def edita(servico, pk):
    pass


def lista():
    pass