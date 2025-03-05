import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='department'
        )
        print('MySQL connected successfully')
        return connection
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
        return None  # Return None if connection fails

def create_table(connection):
    cursor = connection.cursor()
    try:
        query = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255), 
            age INT, 
            salary INT
        );"""
        cursor.execute(query)
        print('Table created successfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()

def inserting_data(connection):
    cursor = connection.cursor()
    try:
        query = """INSERT INTO EMPLOYEE(name, age, salary) VALUES(%s, %s, %s)"""
        data = [
            ("Alice", 25, 5000),
            ("Bob", 30, 7000),
            ("Charlie", 28, 6000),
            ("David", 35, 8000),
            ("Emma", 22, 4000),
            ("Frank", 40, 9000),
            ("Grace", 27, 5500),
            ("Hannah", 33, 7500),
            ("Ian", 29, 6200),
            ("Jack", 26, 5800)
        ]
        
        cursor.executemany(query, data)
        connection.commit()
        print('Data inserted successfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()

def select_all_data(connection):
    cursor = connection.cursor()
    try:
        query = """SELECT * FROM EMPLOYEE;"""
        cursor.execute(query)
        result = cursor.fetchall()
        print("\nAll Employee Data:")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
    finally:
        cursor.close()

def updating_data(connection):
    cursor = connection.cursor()
    try:
        query = """UPDATE EMPLOYEE SET salary = 7500 WHERE name = "Charlie";"""
        cursor.execute(query)
        connection.commit()
        
        if cursor.rowcount == 0:
            print("No matching employee found!")
        else:
            print('Updated Charlie’s salary to 7500 successfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()

def deleting_data(connection):
    cursor = connection.cursor()
    try:
        query = """DELETE FROM EMPLOYEE WHERE name = "Emma";"""
        cursor.execute(query)
        connection.commit()
        
        if cursor.rowcount == 0:
            print("No matching employee found!")
        else:
            print('Deleted employee Emma successfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()

def sort_data(connection):
    cursor = connection.cursor()
    try:
        query = """SELECT * FROM EMPLOYEE ORDER BY salary DESC;"""
        cursor.execute(query)
        result = cursor.fetchall()
        print("\nSorted Employee Data (by Salary Descending):")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
    finally:
        cursor.close()

def query_with_filter(connection):
    cursor = connection.cursor()
    try:
        query = """SELECT * FROM EMPLOYEE WHERE salary > 6000;"""
        cursor.execute(query)
        result = cursor.fetchall()
        print("\nEmployees with Salary > 6000:")
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
    finally:
        cursor.close()

def drop_table(connection):
    cursor = connection.cursor()
    try:
        query = """DROP TABLE IF EXISTS EMPLOYEE;"""
        cursor.execute(query)
        connection.commit()
        print('Table dropped successfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()

def drop_database(connection):
    cursor = connection.cursor()
    try:
        query = """DROP DATABASE IF EXISTS department;"""
        cursor.execute(query)
        connection.commit()
        print('Database dropped successfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()

def main():
    connection = connect_db()
    if not connection:
        return None
    
    create_table(connection)
    inserting_data(connection)
    select_all_data(connection)
    updating_data(connection)
    deleting_data(connection)
    sort_data(connection)
    query_with_filter(connection)
    # drop_table(connection)  # Uncomment to drop table
    # drop_database(connection)  # Uncomment to drop database

    connection.close()
    print('MySQL connection closed')

main()
