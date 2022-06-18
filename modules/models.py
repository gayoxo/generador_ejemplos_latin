from pydantic import BaseModel

class Verb_data(BaseModel):
    verbo: str
    caso1: str
    argumento1: str
    caso2: str
    argumento2: str
    caso3: str
    argumento3: str
    valencias: str

