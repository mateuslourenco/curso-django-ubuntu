import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains
from model_bakery import baker


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_aperitivos_presente_no_menu(client, db):
    resp = client.get(reverse('base:home'))
    assert_contains(resp, f'{reverse("aperitivos:indice")}')
    assert_contains(resp, 'Aperitivos')


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_video(resp, videos):
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
