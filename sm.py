import os
import requests

api_token = os.getenv('THEMOVIEDB_API_KEY')

def get_json(path, **params):
    url = f'https://api.themoviedb.org/3/{path}'
    all_params = {'api_key': api_token} | params
    
    try:
        r = requests.get(url, params=all_params)
    except requests.exceptions.RequestException:
        print('Houve algum problema com a conexão.')
        return
    else:
        return r.json()
    
def get_movies_per_page(movie_name, page=1, quantity_per_page=20):
    data = get_json('search/movie', language='pt-BR', include_adult='false', page=page, query=movie_name)
    
    if not data:
        return
    
    if data['total_results']:
        movies = [
            [movie['title'], movie['original_title'], movie['id']]
            for movie in data['results'][:quantity_per_page]
        ]
        return movies
    else:
        print('Este filme não foi encontrado.')
        return
