#Anthony Guzman         1503239
import requests
import json
import mysql.connector
from mysql.connector import Error
from datetime import date

#create a connection with mysql connection
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' ocurred")

    return connection
#defined connection with query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' ocurred")
        #defined input data 
def insert_temp(input_data):
    sql_query = "INSERT INTO hwk2_results(city, date, temp, feels_like, temp_min, temp_max, pressure, humidity) VALUES "
    sql_query += "('{}', '{}', {}, {}, {}, {}, {}, {})".format(input_data["name"], date.today(), input_data["main"]["temp"], input_data["main"]["feels_like"], input_data["main"]["temp_min"], input_data["main"]["temp_max"], input_data["main"]["pressure"], input_data["main"]["humidity"])
#created connection with personal sql database
    connection = create_connection("cis3368-db.ccczem4tqygs.us-east-1.rds.amazonaws.com", "anthonycis3368", "hostname123", "mydb")
    execute_query(connection, sql_query)
#Will request the user to input the city
city_entry = input('Enter the city that should be retrieved: ')

#requested path to import the weather data for each city
API_key = "fa48ba92ab3b34aa6c0ffb4ded0db708"
request_path ="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_entry, API_key)
response = requests.get(request_path)
json_result = json.loads(response.text)

# will print the temperature, feels like, temp max, and temp max 
print("temp: {}\nfeels_like: {}\ntemp_min: {}\ntemp_max: {}\n".format(json_result["main"]["temp"],json_result["main"]["feels_like"],json_result["main"]["temp_min"],json_result["main"]["temp_max"]))
#created a menu for different options to view specific data such as obtaining temperature, humidity, and pressure
flag=True
menu = {}
menu['1']="Store temp data" 
menu['2']="View humidity data"
menu['3']="Display pressure data"
menu['4']="View humidity and pressure data"
menu['5']="Exit"
while flag: 
    options=menu.keys()

    for entry in options: 
        print(entry, menu[entry])
#If options will allow the user input a certain number and it will output a specific value
    menu_entry = input()

    if menu_entry == "1":
        insert_temp(json_result)
        print("Successful select another option.")
    elif  menu_entry == "2":
        print("humidity: {}".format(json_result["main"]["humidity"]))
    elif  menu_entry == "3":
        print("Pressure: {}".format(json_result["main"]["pressure"]))
    elif  menu_entry == "4":
        print("Humidity: {}\r\nPressure: {}".format(json_result["main"]["humidity"], json_result["main"]["pressure"] ))
    elif  menu_entry == "5":
        flag=False
    else:
        print("Enter valid Value")
