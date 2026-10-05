from fastapi import FastAPI, Depends, HTTPException # Traigo FastAPI de la librería que instale
from schemas import CompanyCreate, CompanyRead # Traigo las clases de schemas
from database import engine, get_db
from models import Base, Company
from sqlalchemy.orm import Session
from sqlalchemy import func

app = FastAPI() # Creo el objeto app de la clase FastAPI
Base.metadata.create_all(engine)

# Creo una ruta para saber si la API esta encendida
@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}

@app.post("/companies", response_model=CompanyRead)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    existing = db.query(Company).filter(func.lower(Company.name) == company.name.lower()).first() #Busca si ya existe   
    if existing:
        raise HTTPException(status_code=409, detail="Company already exists")
    new_company = Company(name=company.name, website=company.website, industry=company.industry) #En el cuaderno de python
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company 
@app.get("/companies", response_model=list[CompanyRead])
def list_companies( db: Session = Depends(get_db)):
    return db.query(Company).all()



