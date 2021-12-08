from .config import SPOTIFY_SECRET_KEY, SPOTIFY_CLIENT_ID

# MAKE PANDAS DATAFRAME INTO A JSON DICTIONARY FOR PASSING
def CSVToDataFrame(csv, datetime=False):
    """Creates a DataFrame from csv file passed as a variable.
    
    Assumes 'df' is a pandas dataframe
    """
    import pandas as pd

    if datetime:
      df = pd.read_csv(csv, parse_dates=['date'])
    else:
        df = pd.read_csv(csv)
    return df


# CONVERT DF INTO JSON DICT
def MakeDataFrameJson(df):
    """Creates an in-memory json.
    
    Assumes 'df' is a pandas dataframe
    """
    import json
    json_data = json.loads(json.dumps(df))
    return json_data


# MAKE MODEL FUNCTION CSV COMPATIBLE FOR DB COPY

def MakeModelCSV(data):
    """Creates an in-memory csv.
    
    Assumes 'data' is a list of dictionaries
    with native python types
    """
    from io import StringIO
    import pandas as pd

    mem_csv = StringIO()
    pd.DataFrame(data).to_csv(mem_csv, index=False)
    mem_csv.seek(0)
    return mem_csv


# IMPORT CSV WITH DB COPY

def ImportCSV(csv, model):
    """Saves copy of csv to database.
    """
    from contextlib import closing

    with closing(csv) as csv_io:
        model.objects.from_csv(csv_io)


# EXPORT DB TABLE TO CSV

def TableExportCSV(model, name):
    """Exports copy of database table to csv.

    Arguments:
    model: function => pass a model function to export from database.
    name: str => csv name 
    """
    model.objects.to_csv(f'./{name}.csv')


# ADD IMGUR IMAGE API CALL METHOD

#################################################################
# SERIALIZER METHODS



#################################################################
# MUSIC METHODS

# GET INFO
def GetSpotipyInfo(title='Bangarang', artist='Skrillex'):
    
    import spotipy
    import sys
    from spotipy.oauth2 import SpotifyClientCredentials

    import urllib.request
    import json 

    client_id = SPOTIFY_CLIENT_ID
    client_secret = SPOTIFY_SECRET_KEY

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)

    # INTIALIZE SPOTIPY
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = spotify.search(q="artist:" + artist + " track:" + title, type="track")

    items = results['tracks']['items']

    # print(items[0]['album']['images'][0]['url'])
    # print(items[0]['album']['id'])

    # PASS IMAGE / DATA TO MUS MODEL
    
    print(items[0]['album']['id'])

    if len(sys.argv) > 1:
        tid = sys.argv[1]
    else:
        tid = items[0]['album']['id']

    features = spotify.audio_features(tracks=[tid])

    print(json.dumps(features, indent=4))

    data = {
        
        'title': items[0]['album']['name'],
        'artist': artist,
        'data': results,
        'items': items,
        'title_uri': items[0]['album']['id'],
        'image': items[0]['album']['images'][1]['url'],
        'artist_image': items[0]['album']['images'][0]['url'],
        'features': features,
        # 'preview': items[0]['album']['preview_url'],
    }
    
    return data


def GetAudioAnalysis(track_id):
    pass


#################################################################
# VBT METHODS