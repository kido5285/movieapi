import requests
from flask import Flask, request, jsonify
from dotenv import dotenv_values
config = dotenv_values(".env")

app = Flask(__name__)


headers = {
    "Authorization": f"Bearer {config['bearer_token']}",
    "Content-Type": "application/json"  # Optional: Specify the content type
}

@app.route('/wp/admin')
def admin():
    if request.args.get('1BC63') == 'movie-popular' and request.args.get('Og4Re'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={request.args.get('Og4Re')}", headers=headers)
        return jsonify(apiResponse.json()), 200
    elif request.args.get('I2g9G') == 'movie-top-rated' and request.args.get('QYbSR'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={request.args.get('QYbSR')}", headers=headers)
        return jsonify(apiResponse.json()), 200
    elif request.args.get('fl18E') == 'movie-now-playing' and request.args.get('YZBDy'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/now_playing?language=en-US&page={request.args.get('YZBDy')}", headers=headers)
        return jsonify(apiResponse.json()), 200
    # with gens and exclude gens
    elif request.args.get('bUCtG') == 'movie-discover' and request.args.get('s0XEd') and request.args.get('2UjJE'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/movie?language=en-US&sort_by=popularity.desc&include_adult=true&include_video=false&page=1&with_genres={request.args.get('s0XEd')}&without_genres={request.args.get('2UjJE')}&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    elif request.args.get('bUCtG') == 'movie-discover' and request.args.get('s0XEd') == '' and request.args.get('2UjJE') == '':
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/movie?language=en-US&sort_by=popularity.desc&include_adult=true&include_video=false&page=1&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    #tv id
    elif request.args.get('CiGiN') == 'tv' and request.args.get('rjusm'):
        url1=f"https://api.themoviedb.org/3/find/{request.args.get('rjusm')}?external_source=imdb_id"
        apiResponse = {
            'res': requests.get(url1, headers=headers) ,
            'url': url1
            }
        return jsonify(apiResponse), 200
    # tv country
    elif request.args.get('cwzqU') == 'tv-discover' and request.args.get('dnrnF'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/tv?language=en-US&sort_by=popularity.desc&page=1&include_null_first_air_dates=false&with_original_language={request.args.get('dnrnF')}&with_watch_monetization_types=flatrate&with_status=0&with_type=0", headers=headers)
        return jsonify(apiResponse.json()), 200
    elif request.args.get('cwzqU') == 'tv-discover' and request.args.get('dnrnF') == '':
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/tv?language=en-US&sort_by=popularity.desc&page=1&include_null_first_air_dates=false&with_watch_monetization_types=flatrate&with_status=0&with_type=0", headers=headers)
        return jsonify(apiResponse.json()), 200
    # multisearch search page
    elif request.args.get('gmLZW') == 'multi' and request.args.get('GfRGV') and request.args.get('domAV'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/search/multi?language=en-US&query={request.args.get('GfRGV')}&page={request.args.get('domAV')}&include_adult=true", headers=headers)
        return jsonify(apiResponse.json()), 200 
    #movie discover page
    elif request.args.get('9Yj7O') == 'movie-discover' and request.args.get('NenGg'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/movie?language=en-US&sort_by=popularity.desc&include_adult=true&include_video=false&page={request.args.get('NenGg')}&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    # movie discover page and with genres
    elif request.args.get('6xqAd') == 'movie-discover' and request.args.get('XVQBn') and request.args.get('6kxsZ'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/movie?language=en-US&sort_by=popularity.desc&include_adult=true&include_video=false&page={request.args.get('XVQBn')}&with_genres={request.args.get('6kxsZ')}&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    #movie discover page and langcode
    elif request.args.get('BgB3z') == 'movie-discover' and request.args.get('GZ5IV') and request.args.get('X9Avg'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&include_adult=true&include_video=false&page={request.args.get('GZ5IV')}&with_original_language={request.args.get('X9Avg')}&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    # tv discover with page and with_genres
    elif request.args.get('ba6Yi') == 'tv-discover' and request.args.get('Ramm4') and request.args.get('SDAT0'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/tv?sort_by=popularity.desc&page={request.args.get('Ramm4')}&with_genres={request.args.get('SDAT0')}&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    #tv discover with page
    elif request.args.get('zgh0z') == 'tv-discover' and request.args.get('Hgz6x'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/tv?language=en-US&sort_by=popularity.desc&page={request.args.get('Hgz6x')}&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    #tv discover with page and langCode
    elif request.args.get('m0hLX') == 'tv-discover' and request.args.get('uq7cO') and request.args.get('VEtR2'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/discover/tv?sort_by=popularity.desc&page={request.args.get('uq7cO')}&with_original_language={request.args.get('VEtR2')}&with_watch_monetization_types=flatrate", headers=headers)
        return jsonify(apiResponse.json()), 200
    # movie similiar with id
    elif request.args.get('kEli7') == 'movie-similar' and request.args.get('yMzNE'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/{request.args.get('yMzNE')}/similar?language=en-US&page=1", headers=headers)
        return jsonify(apiResponse.json()), 200
    # movie with id
    elif request.args.get('YkYYt') == 'movie' and request.args.get('1Rc7F'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/{request.args.get('1Rc7F')}?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    # movie credits with id 
    elif request.args.get('mtBR7') == 'movie-credits' and request.args.get('PC6sL'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/{request.args.get('PC6sL')}/credits?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    # movie videos with id
    elif request.args.get('zFhPU') == 'movie-videos' and request.args.get('dSSeb'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/{request.args.get('dSSeb')}/videos?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    #tv similar with id
    elif request.args.get('vxaki') == 'tv-similar' and request.args.get('g4cMf'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/tv/{request.args.get('g4cMf')}/similar?language=en-US&page=11", headers=headers)
        return jsonify(apiResponse.json()), 200
    # tv season with only id <-- no specified season
    elif request.args.get('92B9s') == 'tv-season' and request.args.get('xd3da'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/tv/{request.args.get('xd3da')}/season/1?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    # tv credits with id
    elif request.args.get('IaNkp') == 'tv-credits' and request.args.get('DsdOv'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/tv/{request.args.get('DsdOv')}/credits?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    # tv videos with id
    elif request.args.get('v1C8s') == 'tv-videos' and request.args.get('DzzAO'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/tv/{request.args.get('DzzAO')}/videos?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    # movie external ids with id
    elif request.args.get('QxY40') == 'movie-external-ids' and request.args.get('zCt59'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/movie/{request.args.get('zCt59')}/external_ids?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    # tv external ids with id
    elif request.args.get('hl2Oh') == 'tv-external-ids' and request.args.get('Ho1ID'):
        apiResponse = requests.get(f"https://api.themoviedb.org/3/tv/{request.args.get('Ho1ID')}/external_ids?language=en-US", headers=headers)
        return jsonify(apiResponse.json()), 200
    else:
        return '', 404

@app.errorhandler(404)
def fourOfour(self):
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)