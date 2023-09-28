from typing import Optional
from pydantic import BaseModel


class Anime(BaseModel):
    id: Optional[int] = None
    nome: str
    Quantidade_episodios:int
    tipo: str