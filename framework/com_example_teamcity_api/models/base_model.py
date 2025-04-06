from pydantic import BaseModel

class BaseModelPD(BaseModel):
    """Единый базовый класс, чтобы иметь метод to_dict()."""
    def to_dict(self):
        return self.dict()