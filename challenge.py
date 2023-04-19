import json

result = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: 
        result.append("BIGBANG")
    elif i % 3 == 0:
        result.append("BIG")
    elif i % 5 == 0:
        result.append("BANG")
    else:
        result.append(str(i))

print(result)
with open("output.json", "w") as outfile:
    json.dump(result, outfile)