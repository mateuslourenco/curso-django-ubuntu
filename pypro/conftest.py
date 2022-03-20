import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_modelo = baker.make(django_user_model, first_name='Foo lano')
    return usuario_modelo


@pytest.fixture
def client_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_home_usuario_logado(db, client_com_usuario_logado):
    return client_com_usuario_logado.get(reverse('base:home'))


@pytest.fixture
def resp_home_sem_usuario_logado(db, client):
    return client.get(reverse('base:home'))
