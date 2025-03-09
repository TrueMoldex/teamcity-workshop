from dataclasses import fields, is_dataclass

from typing import Type, TypeVar, List, Any, Dict

from framework.com_example_teamcity_api.generators.random_data import RandomData
from framework.com_example_teamcity_api.models.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class TestDataGenerator:

    @staticmethod
    def generate(model_class: Type[T], generated_models: Dict[Type[BaseModel], BaseModel] = None, *parameters) -> T:
        if generated_models is None:
            generated_models = {}

        instance = model_class()
        param_iter = iter(parameters)

        for field_info in fields(instance):
            meta = field_info.metadata
            field_name = field_info.name
            field_type = field_info.type

            # Если поле уже сгенерировано ранее, переиспользуем его
            if field_type in generated_models:
                setattr(instance, field_name, generated_models[field_type])
                continue

            # Optional — поле пропускаем
            if meta.get("optional"):
                continue

            # Parameterizable — берём значение из параметров, если есть
            elif meta.get("parameterizable"):
                value = next(param_iter, None)
                if value is not None:
                    setattr(instance, field_name, value)

            # Random — генерируем случайные данные
            elif meta.get("random"):
                if field_type == str:
                    setattr(instance, field_name, RandomData.get_string())
                elif field_type == int:
                    setattr(instance, field_name, RandomData.get_int())

            # Если поле наследник BaseModel — рекурсивно генерируем его
            elif is_dataclass(field_type) and issubclass(field_type, BaseModel):
                nested_instance = TestDataGenerator.generate(field_type, generated_models)
                setattr(instance, field_name, nested_instance)
                generated_models[field_type] = nested_instance

            # Если поле — список других моделей, создаём список с одним элементом
            elif (getattr(field_type, "__origin__", None) is list and
                  is_dataclass(field_type.__args__[0]) and
                  issubclass(field_type.__args__[0], BaseModel)):
                nested_type = field_type.__args__[0]
                nested_instance = TestDataGenerator.generate(nested_type, generated_models)
                setattr(instance, field_name, [nested_instance])
                generated_models[nested_type] = nested_instance

        param_iter = iter(parameters)
        for field_info in fields(instance):
            meta = field_info.metadata
            field_name = field_info.name
            if meta.get("parameterizable"):
                value = next(param_iter, None)
                if value is not None:
                    setattr(instance, field_name, value)
        return instance
