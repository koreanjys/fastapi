from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "item": "Example!"
            }
        }
    }

class TodoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }
    }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = {
        "json_schema_extra": {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
    }