import os
# Limita o número de threads que as bibliotecas matemáticas do Python (e ONNX) podem usar, 
# para evitar o consumo abusivo de RAM na máquina do Render
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import numpy as np
from insightface.app import FaceAnalysis
import cv2

# Usa 'buffalo_sc' (Super Compact) que consome ainda menos memória, e carrega APENAS os
# modelos estritamente necessários (detecção de rosto e reconhecimento), 
# deixando de carregar módulos como gênero/idade, landmarks 3D, etc.
app = FaceAnalysis(
    name="buffalo_sc", 
    allowed_modules=['detection', 'recognition'], 
    providers=['CPUExecutionProvider']
)
# det_size=(640, 640) ajuda a fixar/limitar a memória utilizada na hora de validar a imagem
app.prepare(ctx_id=-1, det_size=(640, 640))

class FaceService: 
  async def generate_embedding(self, image_bytes: bytes):
    
    nparr = np.frombuffer(image_bytes, np.uint8) 
    
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) 

    if img is None: 
      return None 
    
    faces = app.get(img) 
    
    if not faces: 
      return None 
    
    face = faces[0] 
    
    return face.embedding.tolist()
   