# BlogDjango

Blog desenvolvido durante o Curso de Python 3 do Básico Ao Avançado (com projetos reais) presente na Udemy, utilizando o framework Django.


## Instalação

Instale Django, Pillow, Summernote e MySqlClient com o pip

```bash
  pip install django pillow mysqlclient django-summernote
```
Se ocorrer erro na instalação do MySqlClient verificar com instalar nesse link: https://pypi.org/project/mysqlclient/

## Rode as migrações

```bash
  python manage.py migrate
```

## Para criar usuário administrador

```bash
  python manage.py createsuperuser
```
## Para rodar

```bash
  python manage.py runserver
```
## Para postar
Entre na área administrativa e clique para 'ADICIONAR POST'
