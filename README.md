# Django
Código desenvolvido no módulo de Django do [Site Python Pro](https://www.python.pro.br)

Projeto disponível em https://pythondjangomu.herokuapp.com/

[![Django CI](https://github.com/mateuslourenco/curso-django-ubuntu/actions/workflows/django.yml/badge.svg)](https://github.com/mateuslourenco/curso-django-ubuntu/actions/workflows/django.yml)
[![Updates](https://pyup.io/repos/github/mateuslourenco/curso-django/shield.svg)](https://pyup.io/repos/github/mateuslourenco/curso-django/)
[![Python 3](https://pyup.io/repos/github/mateuslourenco/curso-django/python-3-shield.svg)](https://pyup.io/repos/github/mateuslourenco/curso-django/)
[![codecov](https://codecov.io/gh/mateuslourenco/curso-django/branch/main/graph/badge.svg?token=XGBKVRNKJQ)](https://codecov.io/gh/mateuslourenco/curso-django)

## Descrição
Neste projeto, foi desenvolvido uma plataforma de cursos online(SaaS), nesta plataforma, é possível cadastrar módulos do curso, indicando qual é o publíco alvo, uma descrição do módulo e adicionar as aulas disponíveis. As aulas aceitam vídeos cadastrados na plataforma vimeo.

O projeto seguiu as boas praticas da metodologia Twelve-Factor App.
 - Foi utilizado Git com feature branch, implementado processo de CI com GitHub Action e Heroku
 - Utilizado pipenv para isolar e declarar dependencias
 - Foi utilizado o python-decouple para desaclopar configurações e salvar no arquivo .env ou em variaves de ambiente
 - Foi utilizado sentry para monitorar erros
 - Os processos de linter, tests e builds foram separados 

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
pipenv sync -d
cp contrib/env-sample .env
docker-compose up -d
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

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

