from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 646180231}
    return render(request, 'aperitivos/video.html', context={'video': video})
