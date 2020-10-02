# -*- coding: UTF-8 -*-
import pandas 
import math
import os
import timeit
import numpy 

###### READ DATA########
import pandas,os, timeit
t1 = timeit.default_timer()
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
########## END READ DATA ########

min_x_h=min(hot_coords1) #
min_y_h=min(hot_coords2) #
min_x_r=min(rest_coords1) #
min_y_r=min(rest_coords2) #

max_x_h=max(hot_coords1) #
max_y_h=max(hot_coords2) #
max_x_r=max(rest_coords1) #
max_y_r=max(rest_coords2) #

#check
print(min_y_r,max_y_r,min_x_r,max_x_r)
print('-----------------------------------------')
print(min_y_h,max_y_h,min_x_h,max_x_h)
#end check

#determine grid outer coordinates
x_min=min(min_x_r,float(min_x_h))
y_min=min(min_y_r,float(min_y_h))
x_max=max(max_x_r,float(max_x_h))
y_max=max(max_y_r,float(max_y_h))
print('GRID OUTER COORDINATES(x_min, y_min, x_max, y_max): \n%s\n%s\n%s\n%s\n') %(x_min, y_min, x_max, y_max)

###### define grids #######
step_x = (x_max - x_min)/500 
step_y = (y_max - y_min)/500

grid_boundaries = []
grid_names=[]

for i in xrange(0,500):
    lower_boundary_x = x_min +step_x*i
    upper_boundary_x = x_min +step_x*(i + 1)
    grid_boundaries.append([])
    grid_names.append([])
    for j in range(0,500):
        lower_boundary_y = y_min +step_y*j
        upper_boundary_y = y_min +step_y*(j + 1)
        grid_boundaries[i].append([lower_boundary_x,lower_boundary_y,upper_boundary_x,upper_boundary_y])
        grid_names[i].append([i,j])    
        
#place hotels in grids
hotel_gridlist=[]

for i in xrange(0,25461):
    found='no'
    for k in xrange(0,500):
        if found=='yes':
            break
        for j in xrange(0,500):
            if (hotel_np_coordinates[i][0] >= grid_boundaries[j][k][0]) and (hotel_np_coordinates[i][1] >= grid_boundaries[j][k][1]) and (hotel_np_coordinates[i][0] <= grid_boundaries[j][k][2]) and (hotel_np_coordinates[i][1] <= grid_boundaries[j][k][3]):
                hotel_gridlist.append([i,j,k])
                found='yes'
                break

#place restaurants in grids
restaurant_gridlist=[]
for i in xrange(0,14369):
    found='no'
    for k in xrange(0,500):
        if found=='yes':
            break
        for j in xrange(0,500):
            if (restaurant_np_coordinates[i][0] >= grid_boundaries[j][k][0]) and (restaurant_np_coordinates[i][1] >= grid_boundaries[j][k][1]) and (restaurant_np_coordinates[i][0] <= grid_boundaries[j][k][2]) and (restaurant_np_coordinates[i][1] <= grid_boundaries[j][k][3]):
                restaurant_gridlist.append([i,j,k])
                found='yes'
                break
            
################# GET NEIGHBOR CELLS ######
def find_neighbors(m, i, j, dist=1):
    neighbors = []
    i_min = max(0, i-dist)
    i_max = i+dist+1
    j_min = max(0, j-dist)
    j_max = j+dist+1
    for row in m[i_min:i_max]:
        neighbors.append(row[j_min:j_max])
    return neighbors
#######################################
def find_restaurants(i):
    a,b,c=hotel_gridlist[i] #store coordinates of restaurant[i] at variables b,c
    cells=find_neighbors(grid_names, b,c)
    #handle what "find_neighbors" returns
    a1=None
    a2=None
    a3=None
    b1=None
    b2=None
    b3=None
    c1=None
    c2=None
    c3=None
    if len(cells[0])==2:
        a1,b1=cells[0]
    if len(cells[0])==3:
        a1,b1,c1=cells[0]      
    if len(cells[1])==2:
        a2,b2=cells[1]
    if len(cells[1])==3:
        a2,b2,c2=cells[1] 
    if len(cells)>2:    
        if len(cells[2])==2:
            a3,b3=cells[2]
        if len(cells[2])==3:
            a3,b3,c3=cells[2]
        
    list_of_cells=[]
    
    if a1 is not None:
        list_of_cells.append(a1)
    if a2 is not None:
        list_of_cells.append(a2)
    if a3 is not None:
        list_of_cells.append(a3)
    if b1 is not None:
        list_of_cells.append(b1)
    if b2 is not None:
        list_of_cells.append(b2)
    if b3 is not None:
        list_of_cells.append(b3)
    if c1 is not None:
        list_of_cells.append(c1)
    if c2 is not None:
        list_of_cells.append(c2)
    if c3 is not None:
        list_of_cells.append(c3)
    #end handle what "find_neighbors" returns
    
    all_restaurants=[]
    for x in list_of_cells:
        a,b=x
        for y in range(0,len(restaurant_gridlist)):
            c1,a1,b1=restaurant_gridlist[y]
            if a1==a and b1==b:
                all_restaurants.append(c1)
    return all_restaurants
            
############### FIND NEARBY RESTAURANTS ############# 
###### and time the process ########       
#t1 = timeit.default_timer()
nearby_restaurants=[]
for i in xrange(0,len(hotel_gridlist)):
    temp=find_restaurants(i)
    nearby_restaurants.append(temp)
t2 = timeit.default_timer()
print "time taken for Grid Partition: ", (t2-t1) 


################### HAVERSINE FORMULA #########################
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
############################## END HAVERSINE ###############################	

############# METHOD 2: Search nearby grids and get rating (BASED ON #OF RESTAURANTS)
t1 = timeit.default_timer() #begin timer
counter=[]
try:
    a=int(raw_input('Input: Give radius around hotels (in kms)\n'))
except ValueError:
    print "Please give Integer"
radius=a 

for i in range(0,len(hotel_np_coordinates)):
	temp=0
	if len(nearby_restaurants[i])>0:
	   for j in range(0,len(nearby_restaurants[i])):
	       a=nearby_restaurants[i][j]
	       current_restaurant=restaurant_np_coordinates[a]
	       distance=Haversine(hotel_np_coordinates[i], current_restaurant).km
	       if distance<radius:
	           temp+=1
	       if j+1==len(nearby_restaurants[i]):
	           counter.append(temp)
	if len(nearby_restaurants[i])==0:
	    counter.append(temp)	
t2 = timeit.default_timer() #end timer
whatever=t2-t1
print (whatever)

##### METHOD 3
distances=[]
try:
    a=int(raw_input('Input: Give k for nearest restaurants\n'))
except ValueError:
    print "Please give Integer"
n=a #k nearest
t1 = timeit.default_timer()
for i in xrange(0,len(hotel_np_coordinates)):
  distances.append([])
  temp=[]
  if len(nearby_restaurants[i])>=n:
    for j in xrange(0,len(nearby_restaurants[i])):
      current_restaurant=restaurant_np_coordinates[j]    
      distance=Haversine(hotel_np_coordinates[i], current_restaurant).km    
      temp.append(distance)
    temp=sort(temp)
    temp=temp[:n]
  distances[i].append(temp)    
	#else:
	    #for j in xrange(0,len(restaurant_np_coordinates)):
	        #distance=Haversine(hotel_np_coordinates[i], restaurant_np_coordinates[j]).km
	        #distances.append(distance)
t2 = timeit.default_timer()
print "time taken to rate Hotels for Minimum distance: ", (t2-t1)


############## QUESTION 3 ##########
#FIND NEARBY HOTELS FUNCTION
def find_hotels(i):
    a,b,c=hotel_gridlist[i] #store coordinates of restaurant[i] at variables b,c
    cells=find_neighbors(grid_names, b,c)
    #handle what "find_neighbors" returns
    a1=None
    a2=None
    a3=None
    b1=None
    b2=None
    b3=None
    c1=None
    c2=None
    c3=None
    if len(cells[0])==2:
        a1,b1=cells[0]
    if len(cells[0])==3:
        a1,b1,c1=cells[0]      
    if len(cells[1])==2:
        a2,b2=cells[1]
    if len(cells[1])==3:
        a2,b2,c2=cells[1] 
    if len(cells)>2:    
        if len(cells[2])==2:
            a3,b3=cells[2]
        if len(cells[2])==3:
            a3,b3,c3=cells[2]
        
    list_of_cells=[]
    
    if a1 is not None:
        list_of_cells.append(a1)
    if a2 is not None:
        list_of_cells.append(a2)
    if a3 is not None:
        list_of_cells.append(a3)
    if b1 is not None:
        list_of_cells.append(b1)
    if b2 is not None:
        list_of_cells.append(b2)
    if b3 is not None:
        list_of_cells.append(b3)
    if c1 is not None:
        list_of_cells.append(c1)
    if c2 is not None:
        list_of_cells.append(c2)
    if c3 is not None:
        list_of_cells.append(c3)
    #end handle what "find_neighbors" returns
    
    all_hotels=[]
    for x in list_of_cells:
        a,b=x
        for y in range(0,len(hotel_gridlist)):
            c1,a1,b1=hotel_gridlist[y]
            if a1==a and b1==b:
                all_hotels.append(c1)
    return all_hotels

try:
    a=int(raw_input('Input: Give radius around hotels (in kms)\n'))
except ValueError:
    print "Please give Integer"
radius=a 
#FIND PAIRS
t1 = timeit.default_timer()
pairs=[]
nearby_hotels=[]
for i in range(0,len(hotel_np_coordinates)):
    near_hotels=find_hotels(i)
    nearby_hotels.append(near_hotels)
    if len(near_hotels)>0:
        for x in range(0,len(near_hotels)):
            temp=near_hotels[x]
            current_hotel=hotel_np_coordinates[temp]
            distance=Haversine(hotel_np_coordinates[i], current_hotel).km
            if distance<=radius*2:
                pairs.append([i,x])

t2 = timeit.default_timer()
print "time taken to find hotel pairs: ", (t2-t1)
            
#FIND NUMBER OF RESTAURANTS AROUND EACH HOTEL
counter=[]

for i in range(0,len(hotel_np_coordinates)):
  temp=0
  if len(nearby_restaurants[i])>0:
    for j in range(0,len(nearby_restaurants[i])):
      a=nearby_restaurants[i][j]
      current_restaurant=restaurant_np_coordinates[a]
      distance=Haversine(hotel_np_coordinates[i], current_restaurant).km
      if distance<radius:
        temp+=1
      if j+1==len(nearby_restaurants[i]):
        counter.append(temp)
  if len(nearby_restaurants[i])==0:
    counter.append(0)

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


