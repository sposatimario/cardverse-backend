from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Permette a Chrome (Flutter Web) di chiamare il backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CARDS = [
    {"name": "Charizard", "game": "Pokemon", "price": 120},
    {"name": "Luffy", "game": "One Piece", "price": 45},
]


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/cards")
def get_cards():
    return CARDS


@app.post("/scan")
async def scan_card(file: UploadFile = File(...)):
    """
    Scanner FASE 1:
    riceve un'immagine e restituisce una carta "finta" (sempre Charizard).
    Serve solo per testare upload e risposta.
    """
    content = await file.read()
    size = len(content)

    return {
        "ok": True,
        "filename": file.filename,
        "bytes": size,
        "result": {
            "name": "Charizard",
            "game": "Pokemon",
            "price": 120,
            "confidence": 0.80,
        },
    }
