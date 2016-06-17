from datetime import date

from django.db import models
from django.utils import timezone


class Status(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=80)
    razao_social = models.CharField(max_length=80)
    nr_cnpj = models.CharField(max_length=14)
    logradouro = models.CharField(max_length=255)
    nr_logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    pais = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    nome_responsavel = models.CharField(max_length=80)
    cargo_responsavel = models.CharField(max_length=45)
    cpf_responsavel = models.CharField(max_length=11)
    data_abertura = models.DateField(default=date.today)
    data_ativacao = models.DateField(default=date.today)
    data_inativacao = models.DateField().null

    ramo_atividade_id = models.ForeignKey('RamoAtividade', on_delete=models.CASCADE)
    status_id = models.ForeignKey('Status', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title


class RamoAtividade(models.Model):
    nome = models.CharField(max_length=45)
    ramo_atividade_id = models.ForeignKey('RamoAtividade', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title


class Usuario(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    login = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    data_ativacao = models.DateField(default=date.today)
    data_inativacao = models.DateField().null

    ramo_atividade_id = models.ForeignKey('RamoAtividade', on_delete=models.CASCADE)
    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    perfil_id = models.ForeignKey('Perfil', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title


class Perfil(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField()

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title


class Servico(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.TextField()
    ramo_atividade_id = models.ForeignKey('RamoAtividade', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title


class Chamado(models.Model):
    data_abertura = models.DateField(default=date.today)
    data_atualizacao = models.DateField().null
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()

    status_id = models.ForeignKey('Status', on_delete=models.CASCADE)
    usuario_id_abertura = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    usuario_id_resposta = models.ForeignKey('Usuario', on_delete=models.CASCADE).null

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title


class RelacionamentoEmpresaServico:
    ramo_atividade_id = models.ForeignKey('RamoAtividade', on_delete=models.CASCADE).primary_key
    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE).primary_key


class Ticket(models.Model):
    nr_ticket = models.IntegerField()
    data_hora_emissao = models.DateTimeField(default=timezone.now)
    cd_acesso = models.CharField(max_length=8)

    empresa_id = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    servico_id = models.ForeignKey('Servico', on_delete=models.CASCADE, max_length=2)

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title


class Atendimento(models.Model):
    data_hora_inicio = models.DateTimeField(default=timezone.now)
    data_hora_fim = models.DateTimeField(default=timezone.now).null

    ticket_id = models.ForeignKey('Ticket', on_delete=models.CASCADE).primary_key

    status_id = models.ForeignKey('Status', on_delete=models.CASCADE)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now"""
        self.save()

    def __str__(self):
        return self.title
