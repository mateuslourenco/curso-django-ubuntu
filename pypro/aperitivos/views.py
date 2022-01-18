from django.shortcuts import render

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Vídeo Aperitivo: Motivação', vimeo_id='646180231'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='1234')
]
videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
