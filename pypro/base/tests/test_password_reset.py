import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains, assert_not_contains


def test_botao_alterar_senha_presente(resp_home_usuario_logado):
    assert_contains(resp_home_usuario_logado, reverse('password_change'))


def test_botao_alterar_senha_sem_usuario_nao_presente(resp_home_sem_usuario_logado):
    assert_not_contains(resp_home_sem_usuario_logado, reverse('password_change'))


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


def test_senha_atual_invalida(client_com_usuario_logado, usuario):
    resp = client_com_usuario_logado.post(
        reverse('password_change'), {
            'old_password': usuario.senha_plana + '1',
            'new_password1': f'{usuario.senha_plana}nova',
            'new_password2': f'{usuario.senha_plana}nova'
        }
    )
    assert_contains(resp, 'A senha antiga foi digitada incorretamente. Por favor, informe-a novamente.')


def test_senha_nova_diferentes(client_com_usuario_logado, usuario):
    resp = client_com_usuario_logado.post(
        reverse('password_change'), {
            'old_password': usuario.senha_plana,
            'new_password1': f'{usuario.senha_plana}1',
            'new_password2': f'{usuario.senha_plana}2'
        }
    )
    assert_contains(resp, 'Os dois campos de senha não correspondem.')


def test_senha_nova_parecida_com_nome(client_com_usuario_logado, usuario):
    resp = client_com_usuario_logado.post(
        reverse('password_change'), {
            'old_password': usuario.senha_plana,
            'new_password1': f'{usuario.first_name}',
            'new_password2': f'{usuario.first_name}'
        }
    )
    assert_contains(resp, 'A senha é muito parecida com primeiro nome')


def test_senha_nova_com_menos_de_oito_caracteres(client_com_usuario_logado, usuario):
    resp = client_com_usuario_logado.post(
        reverse('password_change'), {
            'old_password': usuario.senha_plana,
            'new_password1': '$3nh412',
            'new_password2': '$3nh412'
        }
    )
    assert_contains(resp, 'Esta senha é muito curta. Ela precisa conter pelo menos 8 caracteres.')


def test_senha_nova_comum(client_com_usuario_logado, usuario):
    resp = client_com_usuario_logado.post(
        reverse('password_change'), {
            'old_password': usuario.senha_plana,
            'new_password1': 'admin',
            'new_password2': 'admin'
        }
    )
    assert_contains(resp, 'Esta senha é muito comum.')


def test_senha_somente_com_numeros(client_com_usuario_logado, usuario):
    resp = client_com_usuario_logado.post(
        reverse('password_change'), {
            'old_password': usuario.senha_plana,
            'new_password1': '147852963',
            'new_password2': '147852963'
        }
    )
    assert_contains(resp, 'Esta senha é inteiramente numérica.')


def test_senha_valida(client_com_usuario_logado, usuario):
    resp = client_com_usuario_logado.post(
        reverse('password_change'), {
            'old_password': usuario.senha_plana,
            'new_password1': f'{usuario.senha_plana}valida',
            'new_password2': f'{usuario.senha_plana}valida'
        }
    )
    assert resp.status_code == 302
    assert resp.url == reverse('password_change_done')
