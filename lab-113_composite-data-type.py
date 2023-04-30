#Working with Composite Data Types

#Creating a car inventory program
#Creating a car inventory program
import csv
import copy
vehicle={
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key,value in vehicle.items():
    print("{} : {}".format(key,value))
inventory = []
with open('car_fleet.csv') as car_data:
    #csv reader
    r = csv.reader(car_data, delimiter=',')
    lc = 0 #line count
    for row in r:
        if lc==0:
            print(f'Column names are: {",".join(row)}')
            lc+=1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model:{row[2]}')
            currentVehicle = copy.deepcopy(vehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            inventory.append(currentVehicle)
            lc+=1
        print(f'Processed {lc} lines.')
        
    for mycar in inventory:
        for key, value in mycar.items():
            print("{} : {}".format(key, value))
            print("-------")