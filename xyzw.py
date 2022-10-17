for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not((y<=x) or (z<=w) and not z == 0):
                    print(x, y, z, w)