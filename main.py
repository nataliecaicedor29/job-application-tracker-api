from fastapi import FastAPI # Traigo FastAPI de la librería que instale

app = FastAPI() # Creo el objeto app de la clase FastAPI

# Creo una ruta para saber si la API esta encendida
@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}
    

