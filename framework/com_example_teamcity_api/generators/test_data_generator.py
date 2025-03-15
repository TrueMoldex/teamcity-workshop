import random
from dataclasses import fields, is_dataclass
from typing import Type, TypeVar, Dict

from framework.com_example_teamcity_api.generators.random_data import RandomData
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.build_type import BuildType
from framework.com_example_teamcity_api.models.project import Project
from framework.com_example_teamcity_api.models.test_data import TestData
from framework.com_example_teamcity_api.models.user import User

T = TypeVar("T", bound=BaseModel)


class TestDataGenerator:
    @staticmethod
    def generate(model_class: Type[T], override_dict=None,
                 generated_models: Dict[Type[BaseModel], BaseModel] = None) -> T:
        if override_dict is None:
            override_dict = {}
        if generated_models is None:
            generated_models = {}

        instance = model_class()

        # Если передан параметр-словарь, используем его для перезаписи полей
        override_dict = override_dict if isinstance(override_dict, dict) else {}

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

    @staticmethod
    def generate_test_data() -> 'TestData':
        """
        Генерирует объект TestData, рекурсивно создавая все поля,
        которые являются наследниками BaseModel.
        """
        try:
            generated_models = {}
            user = TestDataGenerator.generate(User, generated_models)
            project = TestDataGenerator.generate(Project, generated_models)
            build_type = TestDataGenerator.generate(BuildType, {"project": project})

            return TestData(user=user, project=project, build_type=build_type)
        except Exception as e:
            raise RuntimeError("Cannot generate test data") from e