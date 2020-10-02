import pandas 
import math
import os
import timeit
import numpy 

class Haversine:
    '''
    use the haversine class to calculate the distance between
    two lon/lat coordnate pairs.
    output distance available in kilometers, meters, miles, and feet.
    example usage: Haversine([lon1,lat1],[lon2,lat2]).feet
    
    '''
    def __init__(self,coord1,coord2):
        lon1,lat1=coord1
        lon2,lat2=coord2
        
        R=6371000                               # radius of Earth in meters
        phi_1=math.radians(lat1)
        phi_2=math.radians(lat2)

        delta_phi=math.radians(lat2-lat1)
        delta_lambda=math.radians(lon2-lon1)

        a=math.sin(delta_phi/2.0)**2+\
           math.cos(phi_1)*math.cos(phi_2)*\
           math.sin(delta_lambda/2.0)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        
        self.meters=R*c                         # output distance in meters
        self.km=self.meters/1000.0              # output distance in kilometers
        self.miles=self.meters*0.000621371      # output distance in miles
        self.feet=self.miles*5280               # output distance in feet

if __name__ == "__Haversine__":
    main()
    
    
os.chdir('/home/alex/Desktop/vlaxou')
hotels = pandas.read_csv('hotel_coordinates.txt')
hot_coords = hotels.iloc[:,0:2] #PANDA DF COORDINATES, HOTELS
hotel_np_coordinates=hot_coords.values #NUMPY ARRAY COORDINATES, HOTELS
hot_coords1 = hotels.iloc[:,0]
hot_coords1 = hot_coords1.values #LONGITUDE,HOTELS,NUMPY ARRAY
hot_coords2 = hotels.iloc[:,1]
hot_coords2 = hot_coords2.values #LATITUDE, HOTELS, NUMPY ARRAY

restos = pandas.read_csv('restaurant_coordinates.txt')
rest_coords = restos.iloc[:,0:2] #PANDA DF COORDINATES, RESTAUANTS
restaurant_np_coordinates=rest_coords.values #NUMPY ARRAY COORDINATES, RESTAURANTS
rest_coords1 = rest_coords.iloc[:,0]
rest_coords1 = rest_coords1.values #LONGITUDE, RESTAURANTS, NUMPY ARRAY
rest_coords2 = rest_coords.iloc[:,1]
rest_coords2 = rest_coords2.values #LATITUDE, RESTAURANTS, NUMPY ARRAY    

####################### QUESTION 1 #################   
counter=[]
try:
    a=int(raw_input('Input: Give radius around hotels (in kms)\n'))
except ValueError:
    print "Please give Integer"
radius=a 
unchecked_restaurants=restaurant_np_coordinates
to_delete=[]

t1 = timeit.default_timer()
for i in range(0,len(hotel_np_coordinates)):
    counter.append(0)
    if len(to_delete)>0:
        unchecked_restaurants=numpy.delete(unchecked_restaurants, to_delete, axis=0)    
    to_delete=[]
    for j in range(0,len(unchecked_restaurants)):
        distance=Haversine(hotel_np_coordinates[i], unchecked_restaurants[j]).km
        if distance<radius:
            counter[i]=counter[i]+1
            to_delete.append(j)
t2 = timeit.default_timer()
print ("Total time taken:")
print (t2-t1) 	
print ("Restaurants included in hotel radius:")
print (sum(counter))


####################### QUESTION 2 ################# 
closest=[] #here we store the closest restaurants for each hotel
try:
    a=int(raw_input('Input: Give k for nearest restaurants\n'))
except ValueError:
    print "Please give Integer"
amount=a #k nearest
unchecked_restaurants=restaurant_np_coordinates
to_delete=[]

t1 = timeit.default_timer()
for i in range(0,len(hotel_np_coordinates)):
    if len(to_delete)>0:
        unchecked_restaurants=numpy.delete(unchecked_restaurants, to_delete, axis=0)    
    to_delete=[]
    closest.append([])
    temp=[]
    for j in range(0,len(unchecked_restaurants)):
        distance=Haversine(hotel_np_coordinates[i], unchecked_restaurants[j]).km
        temp.append(distance)
    
    to_delete=numpy.argsort(temp) #find positions in array, of sorted elements
    temp2=numpy.sort(temp) # sort the array
    to_delete=to_delete[:amount] #take the top k elements of array(restaurants) in order to remove them
    temp2=temp2[:amount] # take the k nearest 
    closest[i]=temp2

    if len(unchecked_restaurants)==0:
        break

t2 = timeit.default_timer()
print ("Total time taken:")
print (t2-t1) 


############## QUESTION 3 ##########
try:
    a=int(raw_input('Input: Give radius around hotels (in kms)\n'))
except ValueError:
    print "Please give Integer"
radius=a 
#FIND PAIRS
t1 = timeit.default_timer()
pairs=[]
#to_delete=[]
copy=hotel_np_coordinates
a=numpy.arange(0,len(hotel_np_coordinates))
a=[[i] for i in a]
copy=numpy.append(hotel_np_coordinates,a, axis=1)
for i in range(0,len(hotel_np_coordinates)):
    copy=numpy.delete(copy, 0, axis=0)    
    for j in range(0,len(copy)):
        current_hotel=[copy[j,0],copy[j,1]]
        distance=Haversine(hotel_np_coordinates[i], current_hotel).km
        if distance<=2*radius:
            k=copy[j,2]
            temp=[i,k]
            temp=sort(temp)
            pairs.append(temp)
t2 = timeit.default_timer()
print "time taken to find hotel pairs: ", (t2-t1)  

####################### Q1 counter #################           
counter=[]

unchecked_restaurants=restaurant_np_coordinates
to_delete=[]


for i in range(0,len(hotel_np_coordinates)):
    counter.append(0)
    if len(to_delete)>0:
        unchecked_restaurants=numpy.delete(unchecked_restaurants, to_delete, axis=0)    
    to_delete=[]
    for j in range(0,len(unchecked_restaurants)):
        distance=Haversine(hotel_np_coordinates[i], unchecked_restaurants[j]).km
        if distance<radius:
            counter[i]=counter[i]+1
            to_delete.append(j)
 

#RATE THE PAIRS
rating=[]

for i in range(0,len(pairs)):
    a,b=pairs[i]
    temp=counter[int(a)]+counter[int(b)]
    rating.append(temp)

max_element=numpy.argmax(rating)
max_rating=rating[max_element]
best_pair=pairs[max_element]
t3 = timeit.default_timer()
print "time taken to answer question3: ", (t3-t1)		
print(max_rating,best_pair)               
names = hotels.iloc[:,2]                
names=names.values
a=best_pair[0]
b=best_pair[1]
c=names[int(a)]
d=names[int(b)]
print(c,d)




