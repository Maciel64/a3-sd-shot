import numpy as np
from insightface.app import FaceAnalysis
import cv2

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

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
   