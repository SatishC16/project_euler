multiples = []

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)
        
print(sum(multiples))

num = 0

for i in range (0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        num += i

print(num)
