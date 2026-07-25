from pydantic import BaseModel,Field

class HouseData(BaseModel):
    MedInc: float = Field(gt=0, description="Median income in the area")
    HouseAge: float = Field(ge=0, description="Median age of the houses in the area")
    AveRooms: float = Field(ge=0, description="Average number of rooms in the houses")
    AveBedrms: float = Field(ge=0, description="Average number of bedrooms in the houses")
    Population: float = Field(ge=0, description="Total population in the area")
    AveOccup: float = Field(ge=0, description="Average number of occupants in the houses")
    Latitude: float = Field(ge=32, le=42, description="Latitude of the area")
    Longitude: float = Field(ge=-125, le=-114, description="Longitude of the area")