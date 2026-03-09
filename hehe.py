
def pointmaker(topleft,bottomright):
    points = []
    count = 0 
    dif = ((bottomright[0]-topleft[0])//2, (bottomright[1]-topleft[1])//2)
    for i in range(topleft[0], bottomright[0]+1, dif[0]):
        for j in range(topleft[1], bottomright[1]+1, dif[1]):
            
            
            points.append((i,j))
     
    return points



cords = pointmaker((797, 627), (1144, 972))

print(cords)
