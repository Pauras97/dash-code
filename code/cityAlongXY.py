def find_nearest_cities(x_list, y_list, cities, query_cities):
    xi = defaultdict(list)
    yi = defaultdict(list)
    cords = {}
    
    for x, y, c in zip(x_list, y_list, cities):
        xi[x].append((y, c))
        yi[y].append((x, c))
        cords[c] = (x,y)
    
    for xk in xi:
        xi[xk].sort()
    for yk in yi:
        yi[yk].sort()
    
    ans = []
    for q_city in query_cities:
        if q_city not in cords:
            ans.append(None)
            continue
        
        x, y = cords[q_city]
        nearest_city = get_nearest_city(xi, yi, x, y, q_city)
        ans.append(nearest_city)
    
    return ans

def get_nearest_city(xi, yi, x, y, q_city):
    mins = {
        'city': None,
        'dist': float('inf')
    }
    
    find_mins(0, len(xi[x])-1, xi[x], y, q_city, mins)
    find_mins(0, len(yi[y])-1, yi[y], x, q_city, mins)
    
    return mins['city']

def find_mins(left, right, searchAxes, axis, q_city, mins):
    while left <= right:
        mid = (left + right)//2
        mid_axis = searchAxes[mid][0]
        mid_city = searchAxes[mid][1]
        
        if mid_city == q_city:
            if mid > 0:
                mid_city = searchAxes[mid-1][1]
                mid_axis = searchAxes[mid-1][0]
                mid_dist = abs(axis - mid_axis)
                updateMinDist(mid_dist, mid_city, mins)
            if mid < len(searchAxes)-1:
                mid_city = searchAxes[mid+1][1]
                mid_axis = searchAxes[mid+1][0]
                mid_dist = abs(axis - mid_axis)
                updateMinDist(mid_dist, mid_city, mins)
        
        if mid_axis < axis:
            left = mid + 1
        else:
            right = mid - 1

def updateMinDist(dist, city, mins):
    if dist < mins['dist']:
        mins['dist'] = dist
        mins['city'] = city
    
    elif dist == mins['dist']:
        mins['city'] = min(city, mins['city'])
    

if __name__ == '__main__':
    cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs']
    xs = [0, 1, 2, 4, 5, 0, 1]
    ys = [1, 2, 5 ,3, 4, 2, 0]

    query_cities = ['axx', 'axy', 'abs']

    nearest_cities = find_nearest_cities(xs, ys, cities, query_cities)
    print(nearest_cities)


# Nearest Neighbour City

# A number of cities are arranged on a graph that has been divided up like an ordinary Cartesian plane. 
#Each city is located at an integral (x, y) coordinate intersection. City names and locations are given in the form of three arrays:
#c, x, and y, which are aligned by the index to provide the city name (c[i]), and its coordinates, (x[i], y[i]).
#Determine the name of the nearest city that shares either an x or a y coordinate with the queried city.
#If no other cities share an x or y coordinate, return 'NONE'. 
#If two cities have the same distance to the queried city, q[i], consider the one with an alphabetically shorter name (i.e. 'ab' < 'aba' < 'abb') as the closest choice.
#The distance is the Manhattan distance, the absolute difference in x plus the absolute difference in y.

# The time complexity for my solution is O(NlogK) for processing input + O(QlogK) for returning the result for all the given queries,
# where N is the number of cities, K is the max number of cities with same x or y coordinate and Q is the number of queries.

