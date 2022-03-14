



a_list = [(i,j) for i in range(0,5) for j in range(0,5) if i%2 == 0 if j%2 == 0]
print(a_list)




a_list = []
for i in range(0,5):
    for j in range(0,5):
        if i%2 == 0:
            if j%2 == 0:
                a_list.append((i,j))
print(a_list)
