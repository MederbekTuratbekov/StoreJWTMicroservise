from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed


class RemoteUser:
    """
    Простой объект вместо модели User.
    Хранит только то, что реально есть в JWT payload: id.
    Не ходит в локальную БД, потому что локальной таблицы
    пользователей в этом сервисе нет и не должно быть.
    """
    def __init__(self, user_id):
        self.id = user_id
        self.pk = user_id
        self.is_authenticated = True


class RemoteJWTAuthentication(JWTAuthentication):
    """
    Проверяет подпись и срок токена как обычно (через SIGNING_KEY),
    но НЕ ищет пользователя в локальной БД (get_user убран).
    Вместо этого достаёт user_id прямо из payload токена.
    """
    def get_user(self, validated_token):
        user_id = validated_token.get('user_id')
        if user_id is None:
            raise InvalidToken('Токен не содержит user_id')
        return RemoteUser(user_id)
