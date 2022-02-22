from django import template

register = template.Library()


@register.filter(name='plural_comments')
def plural_comments(amount_comments):
    try:
        amount_comments = int(amount_comments)

        if amount_comments == 0:
            return f'Nenhum comentário'
        elif amount_comments == 1:
            return f'{amount_comments} comentário'
        else:
            return f'{amount_comments} comentários'
    except:
        return f'{amount_comments} comentário(s)'
