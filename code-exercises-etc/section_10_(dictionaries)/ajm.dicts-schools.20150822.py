## Exercise from ./dict_exercise.py
schools = {
    "geometry": {
        "coordinates": [
            -81.50572799999999, 
            39.21675500000001
        ], 
        "type": "Point"
    }, 
    "properties": {
        "address": "300 Campus Drive, Parkersburg, WV 26104", 
        "marker-color": "#3F3040", 
        "marker-symbol": "circle", 
        "name": "West Virginia University at Parkersburg"
    }, 
    "type": "Feature"
}

print schools.get('type')
print schools.get('properties').get('address')
print schools.get('geometry').get('coordinates')[1]
