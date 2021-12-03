file = open('img1.txt')
img1_length = int(file.readline()) #Получение размера
file.readline()
img1 = file.readlines() #Получение сетки
file.close()

file = open('img2.txt')
img2_length = int(file.readline())
file.readline()
img2 = file.readlines()
file.close()

close_x1 = len(img1[0])
close_y1 = len(img1)

for i in range(len(img1)):
    if "1" in img1[i]:
        for j in range(len(img1[i])):
            if img1[i][j] == "1":
                if j < close_x1:
                    close_x1 = j
                if i < close_y1:
                    close_y1 = i

close_x2 = len(img2[0])
close_y2 = len(img2)

for i in range(len(img2)):
    if "1" in img2[i]:
        for j in range(len(img2[i])):
            if img2[i][j] == "1":
                if j < close_x2:
                    close_x2 = j
                if i < close_y2:
                    close_y2 = i

dif_x = abs(close_x1 - close_x2)
dif_y = abs(close_y1 - close_y2)
print(dif_x, dif_y)
