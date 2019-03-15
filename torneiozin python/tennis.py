coordinates = input().split()
coordinates[0] = int(coordinates[0])
coordinates[1] = int(coordinates[1])

if coordinates[0] < 0 or coordinates[0] > 432 or coordinates[1] < 0 or coordinates[1] > 468:
    print("fora")
else:
    print("dentro")