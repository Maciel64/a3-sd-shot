from fastapi import FastAPI, UploadFile
from app.services.face_service import FaceService
from numpy import array as np

app = FastAPI()

@app.post("/embeed")
async def embeed(photo: UploadFile):
    service = FaceService()

    contents = await photo.read() 

    embeedings = await service.generate_embedding(contents)

    if not embeedings: 
        return { "success": False, "message": "Nenhum rosto encontrado" } 
    
    return { "success": True, "embedding": embeedings }