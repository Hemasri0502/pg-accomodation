
import mysql.connector
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from templates.input import Input

class PGASDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        self.geolocator = Nominatim(user_agent="my-app")

    def get_latitude_longitude(self, place):
        location = self.geolocator.geocode(place)
        if location is None:
            return None, None
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude

    def calculate_distance(self, target_latitude, target_longitude):
        query = "SELECT CityName,RPmonth, furnished,AC,Laundry,PGTitle FROM tblpg"
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        output_records = []

        for result in results:
            city, budget, furnished, Ac, Laundry,pgname= result
            latitude, longitude = self.get_latitude_longitude(city)
            stored_location = (latitude, longitude)
            distance = geodesic((target_latitude, target_longitude), stored_location).miles
            record = [[furnished, Ac, Laundry],int(budget), distance,pgname]
            output_records.append(record)

        return output_records

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Example usage
'''host = "localhost"
user = "root"
password = ""
database = "pgasdb"
target_latitude = 37.7749
target_longitude = -122.4194

pgasdb = PGASDB('localhost', 'root', '', 'pgasdb')
output_records = pgasdb.calculate_distance(target_latitude, target_longitude)
pgasdb.close_connection()

for record in output_records:
    budget, amenities, distance = record
    furnished, Ac, Laundry = amenities
    print("Budget:", budget)
    print("Furnished:", furnished)
    print('AC:', Ac)
    print('Laundry:', Laundry)
    print("Distance (in miles):", distance)
    print()

print("Output Records:")
print(output_records)'''











