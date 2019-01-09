with open('zadanie_4_triangle_big.txt', 'r') as f:
    tr = f.readlines()

triangle = []

t2 = []

for item in tr:
    triangle.append(list(map(int, item.split())))

    t2.append(list(map(str, item.split())))

for i in reversed(range(len(triangle) - 1)):

    for j in range(len(triangle[i])):

        if int(triangle[i + 1][j]) > int(triangle[i + 1][j + 1]):

            t2[i][j] = str(t2[i + 1][j]) + ',' + str(triangle[i][j])

            triangle[i][j] = triangle[i][j] + triangle[i + 1][j]

        else:

            t2[i][j] = str(t2[i + 1][j + 1]) + ',' + str(triangle[i][j])

            triangle[i][j] = triangle[i][j] + triangle[i + 1][j + 1]

print("Najwieksza suma to", triangle[0])

print("Elementy na sciezce najwiekszej sumy to:")

print(t2[0])