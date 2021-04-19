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
    
def get_movie_info(movie_id):
    data = get_json(f'/movie/{movie_id}', language='pt-BR', append_to_response='credits')
    
    if not data:
        return
    
    credits = data['credits']
    
    return {
        'title': data['title'], 
        'original_title': data['original_title'],
        'release_year': data['release_date'].split('-')[0],
        'director': [member['name'] for member in credits['crew'] 
                        if member['job'] == 'Director'][0],
        'cast': [member['name'] for member in credits['cast']][:10],
        'poster': f'https://image.tmdb.org/t/p/w154{data["poster_path"]}'
    }
