import csv

state = input("Enter State: ")
state = state.lower()

with open('house.csv', 'r') as f:
    reader = csv.reader(f)
    data_list = list(reader)

i = 0
while i <= 435:
    if data_list[i][1] == state:
        print("-"*20)
        print('Name: ' + data_list[i][17])
        print('Contact: ' + data_list[i][48])
        print('Facebook: ' + data_list[i][49])
        print('Twitter: ' + data_list[i][51])
        print('Photo: ' + data_list[i][52])
        print("-"*20)
    i += 1
