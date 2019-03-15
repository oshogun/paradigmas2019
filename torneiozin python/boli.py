receita = [2, 3, 5]
ingredients = input().split()
for i in range(0, 3):
    ingredients[i] = int(ingredients[i])

totalcaeks = int(ingredients[0] / receita[0])
for i in range(1, 3):
    diff = int(ingredients[i] / receita[i])
    if diff < totalcaeks:
        totalcaeks = diff

print(str(totalcaeks))
    