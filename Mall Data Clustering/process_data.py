#*************************Imports***************

#**********************Script Commands************

#Reading the data from .csv file
file = open("Mall_Customers.csv", "r")
data = []
while True :
    data_line = file.readline().split(",")
    data_line[-1] = data_line[-1][:-1]

    if(data_line[0] == '') :
        break
    
    if(data_line[1] == 'Male') :
        data_line[1] = 0
    else :
        data_line[1] = 1

    data.append(data_line)

file.close() 

#Writing data to text file
inputs_file = open("data.txt", "w+")
for data_line in data :
    for ipt in data_line :
        inputs_file.write(f"{ipt},")
    inputs_file.write('\n')

inputs_file.close()