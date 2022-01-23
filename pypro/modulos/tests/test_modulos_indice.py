import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains
from model_mommy import mommy

from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(mommy.make(Aula, 3, modulo=modulo))
    return aulas


@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice',))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200
