from fastapi import FastAPI, HTTPException, status, Response
from models import Anime
import requests


animes = {
    1: {
        "nome": "Yu Yu Hakusho",
        "Quantidade_episodios": 112,
        "tipo": 'Shounen'

    },

    2: {
        "nome": "Naruto",
        "Quantidade_episodios": 500,
        "tipo": 'Shounen'
    },

    3: {
        "nome": "Meu Casamento Feliz",
        "Quantidade_episodios": 10,
        "tipo": 'Shoujo'
    },

    4: {
        "nome": "Wotakoi",
        "Quantidade_episodios": 11,
        "tipo": 'Josei'
    },
}

app = FastAPI()

@app.get('/')
async def inicio():
    return {'messege': 'Teste!'}


@app.get('/all-animes')
async def get_all():
    return {'Messege': animes}

@app.get('/animes/nome/{nome_anime}')
async def get_animes(nome: str):
    try:
        for i in animes:
            if animes[i]["nome"] == nome:
                nomeAnime = animes[i]
        return nomeAnime
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Assim como o One Piece, está pagina não foi encontrada")


@app.get('/animes/{anime_id}')
async def get_anime(anime_id: int):
    try:
        anime = animes[anime_id]
        # anime.update({"id": anime_id})
        return anime
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Assim como o One Piece, está pagina não foi encontrada")


@app.get('/animes')
async def post_anime(anime: Anime):
    if anime.id not in animes:
        animes[anime.id] = anime
        return anime
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com o iD: {anime.id}")


@app.post('/animes/adicionar')
async def post_anime(anime: Anime):
    anime_id = len(animes) + 1 
    if anime_id not in animes:
        animes[anime_id] = anime
        del anime.id
        return anime, Response(status_code=status.HTTP_201_CREATED) 
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'O anime com id {anime_id} já exixte!')


@app.put('/animes/update/{anime_id}')
async def put_anime(anime_id: int, anime: Anime):
    if anime_id in animes:
        del anime.id
        animes[anime_id] = anime
        return anime
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Assim como o One Piece, está pagina não foi encontrada')



@app.delete('/animes/{anime_id}')
async def delete_anime(anime_id: int):
    if anime_id in animes:
        del animes[anime_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Assim como o One Piece, está pagina não foi encontrada")


@app.get('/cats/')
async def get_CatsFacts():
    try:
        request = requests.get("https://cat-fact.herokuapp.com/facts/random")
        data = request.json()
        return {"Fato sobre gato": data["text"]}
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Não foi possível consumir a API')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8001, log_level="info", reload=True)