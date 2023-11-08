import requests
body =  {
    "squareMeters": 32316,
    "numberOfRooms": 47,
    "hasYard": 0,
    "hasPool": 0,
    "floors": 6,
    "cityCode": 27939,
    "cityPartRange": 10,
    "numPrevOwners": 4,
    "made": 2012,
    "isNewBuilt": 0,
    "hasStormProtector": 1,
    "basement": 659,
    "attic": 7141,
    "garage": 359,
    "hasStorageRoom": 0,
    "hasGuestRoom": 3,
    "price": 3232561.2
  }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
