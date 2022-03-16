import pytest
from django.urls import reverse

from pypro.base.models import User
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('base:registrar'))


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('login'))


def test_botao_registrar_disponivel(resp_home):
    assert_contains(resp_home, 'Registre-se')


def test_link_registrar_disponivel(resp_home):
    assert_contains(resp_home, reverse('base:registrar'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_form_presente(resp):
    assert_contains(resp, '<form')


@pytest.fixture
def resp_com_novo_usuario(client, db, usuario):
    return client.post(reverse('base:registrar'),
                       {
                           'first_name': 'nome',
                           'email': 'email@email.com',
                           'password1': usuario.password,
                           'password2': usuario.password,
                        })


def test_registrar_redirect(resp_com_novo_usuario):
    assert resp_com_novo_usuario.status_code == 302
    assert resp_com_novo_usuario.url == reverse('base:home')


def test_usuario_criado_no_db(resp_com_novo_usuario):
    assert User.objects.filter(email="email@email.com")


@pytest.fixture
def usuario_criado_no_db(db, usuario):
    return User.objects.create(email='email@email.com', password='usuario.password')


@pytest.fixture
def resp_com_usuario_criado_ja_existente(client, db, usuario):
    return client.post(reverse('base:registrar'),
                       {
                           'first_name': 'nome',
                           'email': 'email@email.com',
                           'password1': usuario.password,
                           'password2': usuario.password,
                        })


def test_usuario_criado_ja_existente(usuario_criado_no_db, resp_com_usuario_criado_ja_existente):
    assert_contains(resp_com_usuario_criado_ja_existente, 'Usuário com este Endereço de email já existe.')


def test_usuario_logado_redirect(client_com_usuario_logado, resp):
    assert resp.status_code == 302
    assert resp.url == reverse('base:home')


@pytest.fixture
def resp_com_senha_invalida(client, db, usuario):
    return client.post(reverse('base:registrar'),
                       {
                           'email': usuario.email,
                           'password1': '1234',
                           'password2': '1234',
                        })


def test_senha_invalida(resp_com_senha_invalida):
    assert_contains(resp_com_senha_invalida, 'Esta senha')
