from dataclasses import fields, is_dataclass
from framework.com_example_teamcity_api.generators.random_data import RandomData
from framework.com_example_teamcity_api.models.base_model import BaseModel
from typing import Type, TypeVar, Dict
import random

T = TypeVar("T", bound=BaseModel)


class TestDataGenerator:
    @staticmethod
    def generate(model_class: Type[T], generated_models: Dict[Type[BaseModel], BaseModel] = None, *parameters) -> T:
        if generated_models is None:
            generated_models = {}

        instance = model_class()

        # Если передан параметр-словарь, используем его для перезаписи полей
        override_dict = parameters[0] if parameters and isinstance(parameters[0], dict) else {}

        for field_info in fields(instance):
            meta = field_info.metadata
            field_name = field_info.name
            field_type = field_info.type

            # Если значение для этого поля передано явно, устанавливаем его и пропускаем генерацию
            if field_name in override_dict:
                setattr(instance, field_name, override_dict[field_name])
                continue

            # Если поле уже сгенерировано ранее, переиспользуем его
            if field_type in generated_models:
                setattr(instance, field_name, generated_models[field_type])
                continue

            # Optional – если помечено как optional, пропускаем
            if meta.get("optional"):
                continue

            # Parameterizable – если помечено, берём значение из параметров (если есть)

            # Random – генерируем случайные данные
            elif meta.get("random"):
                if field_type == str:
                    setattr(instance, field_name, RandomData.get_string())
                elif field_type == int:
                    setattr(instance, field_name, random.randint(0, 1000))
                else:
                    # Если тип не простой, можно оставить его без изменений
                    pass

            # Если поле — объект BaseModel, генерируем его рекурсивно
            elif is_dataclass(field_type) and issubclass(field_type, BaseModel):
                nested_instance = TestDataGenerator.generate(field_type, generated_models)
                setattr(instance, field_name, nested_instance)
                generated_models[field_type] = nested_instance

            # Если поле — список объектов BaseModel, создаём список из одного элемента
            elif (getattr(field_type, "__origin__", None) is list and
                  is_dataclass(field_type.__args__[0]) and
                  issubclass(field_type.__args__[0], BaseModel)):
                nested_type = field_type.__args__[0]
                nested_instance = TestDataGenerator.generate(nested_type, generated_models)
                setattr(instance, field_name, [nested_instance])
                generated_models[nested_type] = nested_instance

        return instance