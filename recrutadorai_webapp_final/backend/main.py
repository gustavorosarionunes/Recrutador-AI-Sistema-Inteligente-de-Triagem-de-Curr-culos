from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os, shutil
from utils import extract_text_from_file
from ai_utils import analyze_candidates

UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "./uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="RecrutadorAI Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    saved = []
    for f in files:
        file_path = os.path.join(UPLOAD_DIR, f.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(f.file, buffer)
        saved.append({"original": f.filename, "saved_as": f.filename})
    return {"saved_files": saved}

class AnalyzeRequest(BaseModel):
    job_description: str

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    files = [f for f in os.listdir(UPLOAD_DIR) if os.path.isfile(os.path.join(UPLOAD_DIR, f))]
    candidates = []

    for fn in files:
        path = os.path.join(UPLOAD_DIR, fn)
        try:
            text = extract_text_from_file(path)
        except Exception:
            text = ""
        candidates.append({"filename": fn, "text": text})

    results = analyze_candidates(req.job_description, candidates)
    return {"ranking": results}
