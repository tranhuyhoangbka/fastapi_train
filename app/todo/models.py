from ast import alias
from typing import Optional
import uuid
from pydantic import BaseModel, Field

class TaskModel(BaseModel):
  id: str = Field(default_factory=uuid.uuid4(), alias="_id")
  name: str = Field(...)
  completed: bool = False
  
  # default class
  class Config:
    allow_population_by_field_name = True
    # display as default value of params on doc
    schema_extra = {
      "example":{
        "name": "Learn FARM stack",
        "completed": False
      }
    }

class UpdateTaskModel(BaseModel):
  name: Optional[str]
  completed: Optional[bool]
  
  class Config:
    allow_population_by_field_name = True
    # display as default value of params on doc
    schema_extra = {
      "example":{
        "name": "Learn FARM stack",
        "completed": True
      }
    }