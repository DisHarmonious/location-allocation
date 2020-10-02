pairs=[]
copy=hotel_coordinates[i]
for i in range(0,len(hotel_coordinates)):
    for j in copy:
        if i!=j:
            distance=Haversine(hotel_coordinates[i], copy[j])
            if distance<=2*radius:
                temp=[i,j]
                temp=sort(temp)
                pairs.append([])
                pairs.append(temp)
                