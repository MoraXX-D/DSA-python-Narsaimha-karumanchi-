row = int(input("Enter the number of row"))
col = int(input("Enter the number of coloumn"))

i =1 

while i <= row:
    j = 1
    while j <= col:
        print(j-i+1, end=' ')
        j += 1
    print("")
    i += 1 