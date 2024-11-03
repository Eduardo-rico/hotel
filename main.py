from fastapi import FastAPI
from views.api import router

app = FastAPI()

# Registrar el router con las rutas de la API
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
