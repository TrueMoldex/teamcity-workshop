from collections import defaultdict
from typing import Optional, Dict, Set

from framework.com_example_teamcity_api.enum.endpoit import Endpoint
from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.requests.uncheck.unchecked_base import (
    UncheckedBase,
)
from framework.com_example_teamcity_api.spec.specification import Specification


class TestDataStorage:
    _instance: Optional["TestDataStorage"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestDataStorage, cls).__new__(cls)
            cls._instance._created_entities_map: Dict[Endpoint, Set[str]] = defaultdict(
                set
            )
        return cls._instance

    def add_created_entity(self, endpoint: Endpoint, model: BaseModel):
        """Добавляет сущность, которая была создана, во внутреннюю карту созданных сущностей."""
        entity_id = self._get_entity_id_or_locator(model)
        if entity_id:
            self._created_entities_map[endpoint].add(entity_id)

    def _get_entity_id_or_locator(self, model: BaseModel) -> Optional[str]:
        """Безопасно получает id или locator из объекта модели."""
        for field_name in ("id", "locator"):
            if hasattr(model, field_name):
                return str(getattr(model, field_name, None))
        raise ValueError("Cannot get id or locator of entity")

    def delete_created_entities(self):
        """Удаляет все созданные сущности."""
        for endpoint, ids in self._created_entities_map.items():
            unchecked_base = UncheckedBase(
                *Specification.super_user_auth_spec(), endpoint
            )
            for entity_id in ids:
                unchecked_base.delete(entity_id)
        self._created_entities_map.clear()
