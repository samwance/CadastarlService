from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class QueryCreate(BaseModel):
    cadastral_number: str = Field(..., json_schema_extra={"example": "77:01:0004012:2"})
    latitude: float = Field(..., json_schema_extra={"example": 55.755826})
    longitude: float = Field(..., json_schema_extra={"example": 37.6173})


class QueryResponse(BaseModel):
    id: int
    cadastral_number: str
    latitude: float
    longitude: float
    result: bool

    model_config = ConfigDict(from_attributes=True)
