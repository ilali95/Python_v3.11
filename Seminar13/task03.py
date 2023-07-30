# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class BaseException(Exception):
    pass

class LevelError(BaseException):
    pass

class AccessError(BaseException):
    pass