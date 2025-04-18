import requests
import pandas as pd
import time


def getData(network_id, city, country, position):
   # url = f'https://api.citybik.es/v2/networks/{network_id}'
    url = f'https://api.citybik.es/v2/networks/{network_id}'



    # Appel API
    response = requests.get(url)
    data = response.json()

    stations = data['network']['stations']
    # Conversion en DataFrame
    df = pd.DataFrame(stations)

    # Sélection des colonnes utiles
    #columns = ['name', 'latitude', 'longitude', 'free_bikes', 'empty_slots', 'timestamp']
    columns = ['name', 'free_bikes', 'empty_slots']
    df = df[columns]

    if city == 'Berlina':  
      df['city'] = 'Berlin'
    else:
      df['city'] = city
    
    df['country'] = country
    df['position'] = position

    df.to_csv("./getting/_"+country+"_"+city+str(position)+".csv", index=False)


code = [
    ['bicing', 'Barcelona', 'Spain'],
    ['valenbisi', 'Valencia', 'Spain'],
    ['sevici', 'Sevilla', 'Spain'],

    ['blue-bikes', 'Boston', 'Usa'],
    ['capital-bikeshare', 'Washington', 'Usa'],
    ['divvy', 'Chicago', 'Usa'],
    	
    ['citi-bike-nyc', 'New York', 'Usa'],

    ['callabike-berlin','Berlin','Germany'],
    ['nextbike-berlin','Berlina','Germany'],

    ['dublinbikes','Dublin','Ireland'],

    ['oslo-bysykkel','Oslo','Norway'],

    ['santander-cycles','London','United Kingdom'],

    ['velib','Paris','France'],
    ['velov','Lyon','France'],

    ['bixi-montreal','Montréal','Canada'],
    ['bixi-toronto','Toronto','Canada'],

    ['villo','Bruxelles','Belgium'],
]




for i in range(17):
    print(i)
    for param in code: 
        getData(param[0], param[1], param[2], i)
   

    time.sleep(44)

