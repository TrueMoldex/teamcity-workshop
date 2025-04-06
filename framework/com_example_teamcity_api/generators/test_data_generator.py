import random
import string
from typing import get_type_hints, Union, get_origin, get_args, Type

from pydantic import BaseModel

# Ваш базовый класс для Pydantic моделей (если он называется BaseModelPD)
# Если вы используете pydantic.BaseModel напрямую, замените BaseModelPD на BaseModel.
from framework.com_example_teamcity_api.models.base_model import BaseModelPD


def generate_random_string(length=8) -> str:
    """Генерация случайной строки из букв (a-z, A-Z)."""
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def generate_random_digits(length=8) -> str:
    """Генерация строки, состоящей только из цифр."""
    digits = string.digits
    return "".join(random.choice(digits) for _ in range(length))


def generate_random_project_id(length=6) -> str:
    """
    Генерация корректного идентификатора проекта:
    ID должен начинаться с латинской буквы, далее могут идти буквы, цифры и подчёркивания.
    """
    letters = string.ascii_letters
    valid_chars = string.ascii_letters + string.digits + "_"
    first = random.choice(letters)
    rest = "".join(random.choice(valid_chars) for _ in range(length - 1))
    return first + rest


def generate_instance(cls: Type[BaseModelPD], overrides: dict = None) -> BaseModelPD:
    """
    Рекурсивно создаёт экземпляр Pydantic-модели `cls`, заполняя поля случайными значениями.
    Если для поля передан override, используется его значение.

    Особенности:
    - Для модели User: поле "id" генерируется как строка из цифр.
    - Для модели Project: поле "id" генерируется как корректный проектный ID.
    - Для полей с типом List[...] если элемент является Pydantic-моделью, генерируется список с одним элементом.
    """
    if overrides is None:
        overrides = {}

    field_values = {}
    type_hints = get_type_hints(cls)

    for field_name, field_type in cls.__annotations__.items():
        # Если значение переопределено, используем его.
        if field_name in overrides:
            field_values[field_name] = overrides[field_name]
            continue

        # Особая логика для поля "id"
        if field_name == "id":
            if cls.__name__ == "Project":
                field_values[field_name] = generate_random_project_id()
                continue
            if cls.__name__ == "User":
                field_values[field_name] = generate_random_digits()
                continue
            # Для остальных моделей, если id — строка, генерируем случайную строку.
            if "str" in str(field_type):
                field_values[field_name] = generate_random_string()
                continue

        # Для поля "name" — используем значение по умолчанию.
        if field_name == "name" and field_type is str:
            field_values[field_name] = "default_name"
            continue

        # Если модель Role, задаём значения по умолчанию для roleId и scope.
        if cls.__name__ == "Role":
            if field_name == "roleId":
                field_values[field_name] = "SYSTEM_ADMIN"
                continue
            if field_name == "scope":
                field_values[field_name] = "g"
                continue

        # Если поле имеет тип List[...] или Optional[List[...]]
        origin = get_origin(field_type)
        if origin == list:
            item_type = get_args(field_type)[0]
            # Если элемент является Pydantic-моделью, генерируем один элемент.
            if isinstance(item_type, type) and issubclass(item_type, BaseModelPD):
                field_values[field_name] = [generate_instance(item_type)]
            else:
                field_values[field_name] = []
            continue

        # Если поле является вложенной Pydantic-моделью
        if isinstance(field_type, type) and issubclass(field_type, BaseModelPD):
            field_values[field_name] = generate_instance(field_type)
            continue

        # Если поле является Optional[...] (но не List), и содержит str, генерируем строку.
        if get_origin(field_type) is Union and type(None) in field_type.__args__:
            if str in field_type.__args__:
                field_values[field_name] = generate_random_string()
            else:
                field_values[field_name] = None
            continue

        # Если поле — просто str
        if field_type is str:
            field_values[field_name] = generate_random_string()
            continue

        # Если поле — целое число
        if field_type is int:
            field_values[field_name] = random.randint(1, 999)
            continue

        # Если ничего не подошло — оставляем None (Pydantic может использовать дефолт, если он указан в модели)
        field_values[field_name] = None

    return cls(**field_values)
