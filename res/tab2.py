data = [(10,6.92),(19.9,8.86),(29.8,11.47),(39.8,12.43)]

for (x,t) in data:
    v = round(x/t,2)
    d = v*(.05/x + .13/t)
    print(f"{t} {v} {round(d,2)}")
