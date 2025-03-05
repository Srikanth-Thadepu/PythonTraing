import csv

data = [
    ['Name', 'Age', 'Gender', 'Department', 'Salary'],
    ['Srikanth', '21', 'M', 'Developer', '33000'],
    ['Shashwath', '21', 'M', 'Analyst', '30000'],
    ['Jaya Prakash', '22', 'M', 'R&D', '35000'],
    ['Mia', '20', 'F', 'Developer', '33000'],
    ['Dani', '19', 'F', 'Analyst', '30000']
]

file_name = "EmpData.csv"

with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f'CSV file {file_name} created')