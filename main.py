results = []

#data basic structure

for no in range(361):
    #print(no)
    item = {"id": no, "azimuth":no, "coordinates": "point(x,y)", "year":2020}
    results.append(item)

print(results)
