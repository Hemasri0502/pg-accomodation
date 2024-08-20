from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_lat_lng(place):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(place)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        print(latitude,longitude)
        return latitude, longitude

class Input:

    def __init__(self,target,n,budget):

        self.target=target
        #self.target_lattitude,self.target_longitude=get_lat_lng(self.target)[0],get_lat_lng(self.target)[1]
        #print(self.target_lattitude,self.target_longitude)
        self.amenities=[]
        self.n=n
        self.budget=budget

    def amen_list(self):
        for i in range(self.n):
            amen=input("enter your amenities : ")
            self.amenities.append(amen)
        return self.amenities

    
