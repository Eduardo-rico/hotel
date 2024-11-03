from fastapi import FastAPI  # type: ignore
from views.api import router
import os

app = FastAPI()

# Registrar el router con las rutas de la API
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

