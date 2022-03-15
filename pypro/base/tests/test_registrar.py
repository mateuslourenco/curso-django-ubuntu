import pytest
from django.urls import reverse

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
