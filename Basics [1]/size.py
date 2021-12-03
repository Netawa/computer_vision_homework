file = open('figure6.txt')
mm_length = int(file.readline()) #Получение размера
file.readline()
big_net = file.readlines() #Получение сетки
file.close()

for i in range(len(big_net)): #разбить всю сетку на отдельные клетки
    big_net[i] = big_net[i].split()

close_x = len(big_net[0])
far_x = 0

if "1" in big_net:
    for i in big_net:
        if "1" in i:
            for j in range(len(i)):
                if i[j] == "1":
                    if j < close_x:
                        close_x = j
                    if j > far_x:
                        far_x = j
else:
    answer = "0"
                    
pix_length = far_x - close_x + 1

answer = mm_length/pix_length
print(answer)

