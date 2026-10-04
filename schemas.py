from pydantic import BaseModel, Field

class CompanyCreate(BaseModel):
    name: str = Field(min_length=1)
    website: str | None = None
    industry: str | None = None
class CompanyRead(BaseModel):
    id : int
    name : str 
    website : str | None = None
    industry : str | None = None
    
    
    
    
    


    