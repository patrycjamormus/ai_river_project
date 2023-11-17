from math import cos, sin, radians

results = []

STARTING_POINT = {"x": 0, "y": 0}


def calculate_coord(st_point: dict, angle: float, radius: float=100) -> dict:
    x = st_point["x"] + sin(radians(angle)) * radius
    y = st_point["y"] + cos(radians(angle)) * radius
    print(f'punkt {x}, {y}')
    return {"x": x, "y": y}


# data basic structure

for no in range(361):
    point = calculate_coord(st_point=STARTING_POINT,angle=no)
    # print(no)
    item = {"id": no, "azimuth": no, "coordinates": f'POINT({point["x"]} {point["y"]})', "year": 2020}
    results.append(item)

# print(results)
