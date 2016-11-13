def is_valid_coordinates(coordinates):
    coords = coordinates.split(',')
    if len(coords) == 2:
        for coord in coords:
            try:
                float(coord)
            except:
                return False
            if 'e' in coord.lower():
                return False
        lat, lng = float(coords[0]), float(coords[1])
        valid_lat = lat <= 90 and lat >= -90
        valid_lng = lng <= 180 and lng >= -180
        if valid_lat and valid_lng:
            return True
    return False

'''
import re

def is_valid_coordinates(coordinates):
    return bool(re.match("-?(\d|[1-8]\d|90)\.?\d*, -?(\d|[1-9]\d|1[0-7]\d|180)\.?\d*$", coordinates))
'''

'''
def is_valid_coordinates(coordinates):
    try:
        lat, lng = [abs(float(c)) for c in coordinates.split(',') if 'e' not in c]
    except ValueError:
        return False

    return lat <= 90 and lng <= 180
'''

if __name__ == '__main__':
    valid_coords = ["-23, 25",
                    "4, -3",
                    "24.53525235, 23.45235",
                    "04, -23.234235",
                    "43.91343345, 143"]
    for coord in valid_coords:
        print is_valid_coordinates(coord)


    invalid_coordinates = [ "23.234, - 23.4234",
                            "2342.43536, 34.324236",
                            "N23.43345, E32.6457",
                            "99.234, 12.324",
                            "6.325624, 43.34345.345",
                            "0, 1,2",
                            "0.342q0832, 1.2324",
                            "23.245, 1e1" ]
    for coord in invalid_coordinates:
        print is_valid_coordinates(coord)

