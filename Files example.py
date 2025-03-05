with open("Sample File.txt",'w') as file:
    file.write("Hello, World!")

with open("Sample File.txt",'r') as file:
    content=file.read()
    print(content)

with open("Sample File.txt","r") as file:
    for line in file:
        print(line.strip())

import csv

# Writing to a CSV file
with open("Sample File.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])

# Reading from a CSV file
with open("Sample File.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)