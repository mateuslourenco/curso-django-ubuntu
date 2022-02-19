# Django
Código desenvolvido no módulo de Django do [Site Python Pro](https://www.python.pro.br)

Projeto disponível em https://pythondjangomu.herokuapp.com/

[![Django CI](https://github.com/mateuslourenco/curso-django-ubuntu/actions/workflows/django.yml/badge.svg)](https://github.com/mateuslourenco/curso-django-ubuntu/actions/workflows/django.yml)
[![Updates](https://pyup.io/repos/github/mateuslourenco/django/shield.svg)](https://pyup.io/repos/github/mateuslourenco/django/)
[![Python 3](https://pyup.io/repos/github/mateuslourenco/django/python-3-shield.svg)](https://pyup.io/repos/github/mateuslourenco/django/)
[![codecov](https://codecov.io/gh/mateuslourenco/django/branch/main/graph/badge.svg?token=XGBKVRNKJQ)](https://codecov.io/gh/mateuslourenco/django)


## Como rodar o projeto

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
pipenv sync --dev
cp contrib/env-sample .env
docker-compose up
python manage.py migrate
python manage.py runserver
```
