# BlogDjango
Blog desenvolvido durante o Curso de Python 3 do Básico Ao Avançado (com projetos reais) presente na Udemy, utilizando o framework Django.

## Instalação
Instale Django, Pillow, Summernote, Crispy-Forms, Axes e MySqlClient com o pip
```bash
  pip install django pillow mysqlclient django-summernote django-crispy-forms django-axes
```
Se ocorrer erro na instalação do MySqlClient verificar com instalar nesse link: https://pypi.org/project/mysqlclient/

## Configuração reCAPTCHA
Crie sua chave reCAPTCHA v2 checkbox no https://www.google.com/recaptcha/admin/create e altere o valor em comments/forms.py e posts/templates/posts/post_details.html

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

## Para postar, editar, ocultar e excluir 
Entre na área administrativa
