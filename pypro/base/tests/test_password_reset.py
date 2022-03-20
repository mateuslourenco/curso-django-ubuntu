import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp_sem_usuario_logado(client):
    return client.get(reverse('password_change'))


@pytest.fixture
def resp(client_com_usuario_logado):
    return client_com_usuario_logado.get(reverse('password_change'))


def test_status_code_sem_usuario_logado(resp_sem_usuario_logado):
    assert resp_sem_usuario_logado.status_code == 302
    assert resp_sem_usuario_logado.url == f'{reverse("login")}?next=/contas/password_change/'


def test_status_code(resp):
    assert resp.status_code == 200


def test_campos_para_troca_presente(resp):
    assert_contains(resp, '<h1>Alterar senha</h1>')
    assert_contains(resp, 'name="old_password" ')
    assert_contains(resp, 'name="new_password1" ')
    assert_contains(resp, 'name="new_password2" ')
