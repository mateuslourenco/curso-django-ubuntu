# Django
Código desenvolvido no módulo de Django do [Site Python Pro](https://www.python.pro.br)

Projeto disponível em https://pythondjangomu.herokuapp.com/

[![Django CI](https://github.com/mateuslourenco/curso-django-ubuntu/actions/workflows/django.yml/badge.svg)](https://github.com/mateuslourenco/curso-django-ubuntu/actions/workflows/django.yml)
[![Updates](https://pyup.io/repos/github/mateuslourenco/django/shield.svg)](https://pyup.io/repos/github/mateuslourenco/django/)
[![Python 3](https://pyup.io/repos/github/mateuslourenco/django/python-3-shield.svg)](https://pyup.io/repos/github/mateuslourenco/django/)
[![codecov](https://codecov.io/gh/mateuslourenco/django/branch/main/graph/badge.svg?token=XGBKVRNKJQ)](https://codecov.io/gh/mateuslourenco/django)

## Descrição
Neste projeto, foi desenvolvido uma plataforma de cursos online, nesta plataforma, é possível cadastrar módulos do curso, indicando qual é o publíco alvo, uma descrição do módulo e adicionar as aulas disponíveis. As aulas aceitam vídeos cadastrados na plataforma vimeo

## Tecnologias usadas
- python
- django
- pytest-django
- python-decouple
- sentry
- pipenv
- django-debug-toolbar
- dj-database-url
- django-s3-folder-storage
- django-ordered-model
- flake8
- pytest-cov
- model-mommy
- postgres
- docker
- git
- github actions
- heroku
- pyup
- layoutit
- bootstrap v4.2.1 

## Como rodar o projeto localmente

- Clone esse repositório
- Instale o pipenv 
- Instale as dependencias
- Copie as variáveis de ambiante
- Inicie o banco de dados postgres com docker
- Rode as migrações

```
git clone https://github.com/mateuslourenco/django.git
cd django
python -m pip install pipenv
pipenv sync
cp contrib/env-sample .env
docker-compose up -d
pipenv run python manage.py migrate
pipenv run python manage.py runserver --insecure
```
Outra alternativa para rodar localmente, é atualizar a variável de ambiente DEBUG no arquivo .env para True

## Como adicionar um novo módulo

- Crie um super usuário
- Acesse a página de admin do django com o super usuário criado.
- Na parte de módulos, vá em adicionar módulo
- Informe o título, publico alvo e a descrição do módulo
```
pipenv run python manage.py createsuperuser
```

## Como adicionar uma aula ao módulo

- Acesse a página de admin do django
- Na parte de módulos, vá em adicionar aula
- Informe o titulo, selecione a qual módulo a aula pertence e informe o ID do vídeo no vimeo

