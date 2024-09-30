input_data = open('input.txt', 'r') 

data = input_data.read() 
#--------------------------------------------------------------------
data = data.split()
N = int(data[0])
M = int(data[1])
K = int(data[2])
aut = str
aut = "0"


if N*M >= K:
    aut = "YES"
else:
    aut = "NO"

#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(str(aut))


# Закрываем открытые ранее файлы!
input_data.close() 
output_data.close()