import re

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    now = timezone.now().year
    if value > now:
        raise ValidationError(
            f'Указанный год - {value} не может быть больше {now}',
            params={'value': value}
        )


def validate_username(value):
    regex = re.compile(r'^[\w.@+-]')
    if value.upper() == 'ME':
        raise ValidationError(
            ('Имя пользователя не может быть <me>.'),
            params={'value': value},
        )
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', value) is None:
        raise ValidationError(
            (f'Не допустимые символы <{value}> в нике.'),
            params={'value': value},
        )
    if not regex.match(value):
        raise ValidationError('Имя содержит недопустимые символы!')
