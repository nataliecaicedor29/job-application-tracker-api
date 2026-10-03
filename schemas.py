from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    website: str | None = None
    industry: str | None = None
    
    
    
    
    


    