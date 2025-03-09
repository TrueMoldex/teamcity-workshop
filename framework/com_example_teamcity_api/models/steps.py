from dataclasses import field
from typing import List
from attr import dataclass

from framework.com_example_teamcity_api.models.base_model import BaseModel
from framework.com_example_teamcity_api.models.step import Step


@dataclass
class Steps(BaseModel):
    step: List[Step] = field(default_factory=list)
    count: int = field(default=0, metadata={"random": True})
