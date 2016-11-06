from pip._vendor import requests

from form.RamoForm import RamoForm


def cadastra(ramo_atividade):
    form = RamoForm(ramo_atividade)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        status = form.cleaned_data['status_ativacao']

        data = monta_json(nome, descricao, status)

        try:
            form = requests.post('http://localhost:3000/ramoAtividade', json=data)
        except requests.exceptions.ConnectionError: # verificar se funciona
            form = "Erro ao tentar conctar com WebService"
    else:
        form = "Campos de Ramo de Atividade nao preenchido corretamente"

    return form


def atualiza(ramo_atividade, pk):
    form = RamoForm(ramo_atividade, pk)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        status = form.cleaned_data['status_ativacao']

        data = monta_json(nome, descricao, status)

        try:
            form = requests.put('http://localhost:3000/ramoAtividade/'+pk, json=data)

        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"
    else:
        form = "Campos de Ramo de Atividade nao preenchidos corretamente"

    return form


def lista():
    ramos = requests.get('http://localhost:3000/ramoAtividade').json()
    return ramos


def ramo_por_id(pk):
    ramo = requests.get('http://localhost:3000/ramoAtividade/'+pk).json()
    return ramo

def monta_json(nome, descricao, status):
    data = {'nome': nome, 'descricao': descricao, 'status_ativacao': status}
    return data

