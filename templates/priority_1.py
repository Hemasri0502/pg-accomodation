import heapq
from templates.db_code import PGASDB
from templates.input import Input
from geopy.geocoders import Nominatim
import ctypes

def get_lat_lng(place):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(place)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude



class heap() :

    def __init__(self) :
        self.create_array()

    def create_array(self):
        self._size = 1
        self._cap = 20
        self._heap = (self._cap*ctypes.py_object)()
        self._heap[0]=None

        return self._heap

    def print(self):
        return self._heap[:self._size]

    def len(self) :
        return self._size

    def left_child(self,item):
        for i in range(1,self._size+1):
            if self._heap[i]==item:
                return self._heap[2*i]
            else:
                pass

    def right_child(self,item):
        for i in range(1,self._size+1):
            if self._heap[i]==item:
                return self._heap[2*i+1]
            else:
                continue

    def insert(self,item):
        if self._size == self._cap:
            self._resize(self._cap*2)
        self._heap[self._size]=item
        self._upheap()
        self._size+=1

        return self._heap[:self._size]
    
    def insert_budget(self,item):
        if self._size == self._cap:
            self._resize(self._cap*2)
        self._heap[self._size]=item
        self._upheap_budget()
        self._size+=1

        return self._heap[:self._size]
    


    def _upheap(self):
        for i in range(self._size,0,-1):
            if i//2 > 0:
                if self._heap[i][2]>self._heap[i//2][2]:
                    continue
                else:
                    self._heap[i][2],self._heap[i//2][2]=self._heap[i//2][2],self._heap[i][2]

        return self._heap
    
    def _upheap_budget(self):
        for i in range(self._size,0,-1):
            if i//2 > 0:
                if self._heap[i][1]>self._heap[i//2][1]:
                    continue
                else:
                    self._heap[i][1],self._heap[i//2][1]=self._heap[i//2][1],self._heap[i][1]

        return self._heap

    def min(self):
        return self._heap[1]

    def delete(self):
        a=self._heap[1]
        self._heap[1]=self._heap[self._size-1]
        self._size-=1
        self._downheap()
        
        return a

    def _downheap(self):
        for i in range(1,self._size+1):
            if 2*i[2]<self._size:
                small=min(self._heap[2*i[2]],self._heap[2*i[2]+1])
                if self._heap[i[2]]<self._heap[2*i[2]] and self._heap[i[2]]<self._heap[(2*i[2])+1]:
                    continue
                else:
                    if small==self._heap[2*i[2]]:
                        self._heap[i[2]],self._heap[2*i[2]]=self._heap[2*i[2]],self._heap[i[2]]
                    else:
                        self._heap[i[2]],self._heap[2*i[2]+1]=self._heap[2*i[2]+1],self._heap[i[2]]
                
        return self._heap[:self._size]

    def heapify(self,inp):
        self.create_array()
        for i in inp:
            self.insert(i)
        inp=self._heap

        return inp[:self._size]


    def sort(self,inp=[]):
        if inp==[]:
            inp=self._heap
        else:
            self.create_array() 
            for i in inp:
                self.insert(i)
            inp=self._heap
        self._heapsort=(self._size*ctypes.py_object)()
        self._sortsize=0
        for i in range(1,self._size):
            # add the min value to the heap sort
            ele=self._heap[1]
            self._heapsort[i-1]=ele
            self._sortsize+=1
           # make the last element as the first element
            self._heap[1]=self._heap[self._size-1]
            self._size-=1
            # heapify the modified heap
            self._downheap()
        
        return self._heapsort[:self._sortsize]
            
    def _resize(self,cap):
        new_heap=(cap*ctypes.py_object)()
        for i in range(self._size):
            new_heap[i]=self._heap[i]

        self._heap=new_heap
        self._cap=cap



# target='kelambakkam'
# target_latitude,target_longitude= get_lat_lng(target)
# print(target_latitude)

# pgasdb = PGASDB('localhost', 'root', '', 'pgasdb')
# output_records = pgasdb.calculate_distance(target_latitude, target_longitude)
# pgasdb.close_connection()
# print(output_records)

# def result():
   
#     h=heap()
#     for i in output_records:
#         res=h.insert(i)
#     return res[1]


# def result_budget():

#     h2=heap()
#     for i in output_records:
#         res_budget=h2.insert_budget(i)
#     return res_budget[1]
