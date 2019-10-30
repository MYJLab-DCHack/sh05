import numpy as np
import math
data = [
       {
           "name": "bori",
           "distance": math.sqrt(20),
           "x": 0.0,
           "y":9.0
           },
       {
           "name": "saka",
           "distance": math.sqrt(17),
           "x": 1.0,
           "y": 1.0
           },
       {
           "name": "maru",
           "distance": math.sqrt(13),
           "x": 4.0,
           "y": 2.0 },
       {
           "name": "sho",
           "distance": math.sqrt(20),
           "x": 6.0,
           "y": 7.0
           }
       ]


def getLocation(users, devide_unit, width):
    if len(users) == 0:
        return None
    elif len(users) == 1:
        return users[0].x, users[0].y
    elif len(users) == 2:
        x_mid = (users[0].x + users[1].x) / 2
        y_mid = (users[0].y + users[1].y) / 2
        return x_mid, y_mid

    xs = [user["x"] for user in users]
    ys = [user["y"] for user in users]
    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)
 
    mesh = np.zeros((math.ceil((y_max - y_min) / devide_unit), math.ceil((x_max - x_min) / devide_unit)))
    for user in users:
        mapdata = []
        for i in np.arange(y_min, y_max, devide_unit):
            row = []
            for j in np.arange(x_min, x_max, devide_unit):
                if abs((j-user["x"])**2 + (i-user["y"])**2 - user["distance"]**2) < width:
                    row.append(1)
                else: 
                    row.append(0)
            mapdata.append(row)
        tmp_mesh = np.array(mapdata)
        mesh += tmp_mesh
    xax = [i + x_min for i in np.arange(x_min, x_max, devide_unit)]
    yax = [0] + [i + y_min for i in np.arange(y_min, y_max, devide_unit)]
    xaxis = np.zeros((1, len(xax)))
    yaxis = np.zeros((1, len(yax)))
    xaxis[:] = xax
    yaxis[:] = yax
    del xax, yax
    xmesh = np.vstack((xaxis, mesh))
    xymesh = np.hstack((yaxis.T, xmesh))
    print(xymesh)
    loc = np.unravel_index(np.argmax(mesh), mesh.shape)
    return loc[1] * devide_unit + x_min, loc[0] * devide_unit + y_min




#　標準出力でぜんぶみえるようにする
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=200)

# メッシュの細かさ、1なら整数
devide_unit = 0.2
# 誤差の想定大きくなればなるほどアバウトになる
# 1 ~ 5とかで試す
width = 3

x, y = getLocation(data, devide_unit, width)
print("現在地は {}, {} です".format(x, y))
