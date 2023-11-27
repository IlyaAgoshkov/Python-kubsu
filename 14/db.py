import sqlite3
from typing import Dict, List
import random
"""Тема таблиц вина"""
# lxml строим xml из sql
# а ещё тоже самое в джанго


def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('db.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            con.commit()
        return res
    return wrapper


@sqlite_connection
@sqlite_connection
def init_db(con: sqlite3.Connection):
    """Создаем таблицы для магазина по продаже автомобилей"""
    cur = con.cursor()

    # Таблица производителей автомобилей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CarManufacturers (
            ManufacturerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ManufacturerName TEXT
        );""")

    # Таблица моделей автомобилей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CarModels (
            ModelID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ModelName TEXT,
            ManufacturerID INTEGER NOT NULL,
            FOREIGN KEY (ManufacturerID) REFERENCES CarManufacturers(ManufacturerID)
        );""")

    # Таблица автомобилей в наличии
    cur.execute("""
        CREATE TABLE IF NOT EXISTS AvailableCars (
            CarID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ModelID INTEGER NOT NULL,
            Color TEXT,
            Price REAL,
            FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID)
        );""")

    # Таблица заказов автомобилей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CarOrders (
            OrderID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CustomerName TEXT,
            CarID INTEGER NOT NULL,
            OrderDate DATE,
            FOREIGN KEY (CarID) REFERENCES AvailableCars(CarID)
        );""")

    # Таблица водителей, привозящих автомобили
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Drivers (
            DriverID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            DriverName TEXT
        );""")

    # Таблица поставок автомобилей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CarDeliveries (
            DeliveryID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CarID INTEGER NOT NULL,
            DriverID INTEGER NOT NULL,
            DeliveryDate DATE,
            FOREIGN KEY (CarID) REFERENCES AvailableCars(CarID),
            FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
        );""")

    # Таблица сервисных работ по автомобилям
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CarService (
            ServiceID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CarID INTEGER NOT NULL,
            ServiceType TEXT,
            ServiceDate DATE,
            Cost REAL,
            FOREIGN KEY (CarID) REFERENCES AvailableCars(CarID)
        );""")

    # Таблица клиентов
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CustomerName TEXT
        );""")

    # Таблица продаж автомобилей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CarSales (
            SaleID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CustomerID INTEGER NOT NULL,
            CarID INTEGER NOT NULL,
            SaleDate DATE,
            SalePrice REAL,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
            FOREIGN KEY (CarID) REFERENCES AvailableCars(CarID)
        );""")

    # Таблица страховок автомобилей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS CarInsurance (
            InsuranceID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CarID INTEGER NOT NULL,
            InsuranceType TEXT,
            InsuranceDate DATE,
            Cost REAL,
            FOREIGN KEY (CarID) REFERENCES AvailableCars(CarID)
        );""")
    cur.execute("INSERT INTO CarManufacturers (ManufacturerName) VALUES ('Toyota');")
    cur.execute("INSERT INTO CarManufacturers (ManufacturerName) VALUES ('Ford');")
    # Добавьте других производителей по аналогии
    cur.execute("INSERT INTO CarModels (ModelName, ManufacturerID) VALUES ('Camry', 1);")
    cur.execute("INSERT INTO CarModels (ModelName, ManufacturerID) VALUES ('Corolla', 1);")
    cur.execute("INSERT INTO CarModels (ModelName, ManufacturerID) VALUES ('F-150', 2);")
    # Добавьте другие модели по аналогии
    cur.execute("INSERT INTO Drivers (DriverName) VALUES ('John Smith');")
    cur.execute("INSERT INTO Drivers (DriverName) VALUES ('Mary Johnson');")
    # Добавьте других водителей по аналогии
    cur.execute("INSERT INTO Customers (CustomerName) VALUES ('Alice Davis');")
    cur.execute("INSERT INTO Customers (CustomerName) VALUES ('Bob Wilson');")
    # Добавьте других клиентов по аналогии
    cur.execute(
        "INSERT INTO CarService (CarID, ServiceType, ServiceDate, Cost) VALUES (1, 'Oil Change', '2023-11-01', 50.0);")
    cur.execute(
        "INSERT INTO CarService (CarID, ServiceType, ServiceDate, Cost) VALUES (2, 'Tire Rotation', '2023-11-15', 30.0);")
    # Добавьте другие сервисные записи по аналогии
    cur.execute("INSERT INTO CarOrders (CustomerName, CarID, OrderDate) VALUES ('Alice Davis', 1, '2023-11-20');")
    cur.execute("INSERT INTO CarOrders (CustomerName, CarID, OrderDate) VALUES ('Bob Wilson', 2, '2023-11-25');")
    # Добавьте другие заказы по аналогии
    cur.execute("INSERT INTO CarDeliveries (CarID, DriverID, DeliveryDate) VALUES (1, 1, '2023-11-22');")
    cur.execute("INSERT INTO CarDeliveries (CarID, DriverID, DeliveryDate) VALUES (2, 2, '2023-11-28');")
    # Добавьте другие поставки по аналогии
    cur.execute("INSERT INTO CarSales (CustomerID, CarID, SaleDate, SalePrice) VALUES (1, 1, '2023-11-23', 26000.0);")
    cur.execute("INSERT INTO CarSales (CustomerID, CarID, SaleDate, SalePrice) VALUES (2, 2, '2023-11-30', 29000.0);")
    # Добавьте другие продажи по аналогии
    cur.execute(
        "INSERT INTO CarInsurance (CarID, InsuranceType, InsuranceDate, Cost) VALUES (1, 'Liability', '2023-11-24', 500.0);")
    cur.execute(
        "INSERT INTO CarInsurance (CarID, InsuranceType, InsuranceDate, Cost) VALUES (2, 'Full Coverage', '2023-12-01', 800.0);")
    # Добавьте другие страховки по аналогии
    cur.execute(
        "INSERT INTO CarInsurance (CarID, InsuranceType, InsuranceDate, Cost) VALUES (1, 'Liability', '2023-11-24', 500.0);")
    cur.execute(
        "INSERT INTO CarInsurance (CarID, InsuranceType, InsuranceDate, Cost) VALUES (2, 'Full Coverage', '2023-12-01', 800.0);")
    # Добавьте другие страховки по аналогии


def generate_random_data():
    colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Silver']
    prices = [20000, 25000, 30000, 35000, 40000]

    data = []
    for _ in range(1000):
        model_id = random.randint(1, 100)  # Предположим, что у вас есть 100 моделей
        color = random.choice(colors)
        price = random.choice(prices)
        data.append((model_id, color, price))

    return data
@sqlite_connection
def insert_records_available_cars(con: sqlite3.Connection):
    cur = con.cursor()
    data = generate_random_data()
    cur.executemany("""
        INSERT INTO AvailableCars (ModelID, Color, Price) VALUES (?, ?, ?);
    """, data)

@sqlite_connection
def get_available_cars(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT CarID, ModelID, Color, Price FROM AvailableCars;
    ''')
    return cur.fetchall()

# 1. Вставка нового производителя автомобилей
def insert_car_manufacturer(cursor, name):
    cursor.execute("INSERT INTO CarManufacturers (ManufacturerName) VALUES (?)", (name,))

# 2. Вставка новой модели автомобиля
def insert_car_model(cursor, name, manufacturer_id):
    cursor.execute("INSERT INTO CarModels (ModelName, ManufacturerID) VALUES (?, ?)", (name, manufacturer_id))

# 3. Вставка нового автомобиля в наличии
def insert_available_car(cursor, model_id, color, price):
    cursor.execute("INSERT INTO AvailableCars (ModelID, Color, Price) VALUES (?, ?, ?)", (model_id, color, price))

# 4. Вставка нового заказа на автомобиль
def insert_car_order(cursor, customer_name, car_id, order_date):
    cursor.execute("INSERT INTO CarOrders (CustomerName, CarID, OrderDate) VALUES (?, ?, ?)", (customer_name, car_id, order_date))

# 5. Вставка нового водителя, привезшего автомобиль
def insert_driver(cursor, name):
    cursor.execute("INSERT INTO Drivers (DriverName) VALUES (?)", (name,))

# 6. Вставка новой поставки автомобиля
def insert_car_delivery(cursor, car_id, driver_id, delivery_date):
    cursor.execute("INSERT INTO CarDeliveries (CarID, DriverID, DeliveryDate) VALUES (?, ?, ?)", (car_id, driver_id, delivery_date))

# 7. Вставка новой записи о сервисной работе на автомобиле
def insert_car_service(cursor, car_id, service_type, service_date, cost):
    cursor.execute("INSERT INTO CarService (CarID, ServiceType, ServiceDate, Cost) VALUES (?, ?, ?, ?)", (car_id, service_type, service_date, cost))

# 8. Вставка нового клиента
def insert_customer(cursor, name):
    cursor.execute("INSERT INTO Customers (CustomerName) VALUES (?)", (name,))

# 9. Вставка новой продажи автомобиля
def insert_car_sale(cursor, customer_id, car_id, sale_date, sale_price):
    cursor.execute("INSERT INTO CarSales (CustomerID, CarID, SaleDate, SalePrice) VALUES (?, ?, ?, ?)", (customer_id, car_id, sale_date, sale_price))

# 10. Вставка новой страховки на автомобиль
def insert_car_insurance(cursor, car_id, insurance_type, insurance_date, cost):
    cursor.execute("INSERT INTO CarInsurance (CarID, InsuranceType, InsuranceDate, Cost) VALUES (?, ?, ?, ?)", (car_id, insurance_type, insurance_date, cost))

# 11. Получение списка всех производителей автомобилей
def get_all_car_manufacturers(cursor):
    cursor.execute("SELECT * FROM CarManufacturers")
    return cursor.fetchall()

# 12. Получение списка всех моделей автомобилей
def get_all_car_models(cursor):
    cursor.execute("SELECT * FROM CarModels")
    return cursor.fetchall()

# 13. Получение списка всех доступных автомобилей
def get_all_available_cars(cursor):
    cursor.execute("SELECT * FROM AvailableCars")
    return cursor.fetchall()

# 14. Получение списка всех заказов на автомобили
def get_all_car_orders(cursor):
    cursor.execute("SELECT * FROM CarOrders")
    return cursor.fetchall()

# 15. Получение списка всех водителей
def get_all_drivers(cursor):
    cursor.execute("SELECT * FROM Drivers")
    return cursor.fetchall()

# 16. Получение списка всех поставок автомобилей
def get_all_car_deliveries(cursor):
    cursor.execute("SELECT * FROM CarDeliveries")
    return cursor.fetchall()

# 17. Получение списка всех записей о сервисных работах
def get_all_car_service_records(cursor):
    cursor.execute("SELECT * FROM CarService")
    return cursor.fetchall()

# 18. Получение списка всех клиентов
def get_all_customers(cursor):
    cursor.execute("SELECT * FROM Customers")
    return cursor.fetchall()

# 19. Получение списка всех продаж автомобилей
def get_all_car_sales(cursor):
    cursor.execute("SELECT * FROM CarSales")
    return cursor.fetchall()

# 20. Получение списка всех страховок на автомобили
def get_all_car_insurances(cursor):
    cursor.execute("SELECT * FROM CarInsurance")
    return cursor.fetchall()

# 21. Обновление информации о производителе автомобилей
def update_car_manufacturer(cursor, manufacturer_id, new_name):
    cursor.execute("UPDATE CarManufacturers SET ManufacturerName = ? WHERE ManufacturerID = ?", (new_name, manufacturer_id))

# 22. Обновление информации о модели автомобиля
def update_car_model(cursor, model_id, new_name, new_manufacturer_id):
    cursor.execute("UPDATE CarModels SET ModelName = ?, ManufacturerID = ? WHERE ModelID = ?", (new_name, new_manufacturer_id, model_id))

# 23. Обновление информации о доступном автомобиле
def update_available_car(cursor, car_id, new_color, new_price):
    cursor.execute("UPDATE AvailableCars SET Color = ?, Price = ? WHERE CarID = ?", (new_color, new_price, car_id))

# 24. Обновление информации о заказе на автомобиль
def update_car_order(cursor, order_id, new_customer_name, new_car_id, new_order_date):
    cursor.execute("UPDATE CarOrders SET CustomerName = ?, CarID = ?, OrderDate = ? WHERE OrderID = ?", (new_customer_name, new_car_id, new_order_date, order_id))

# 25. Обновление информации о водителе
def update_driver(cursor, driver_id, new_name):
    cursor.execute("UPDATE Drivers SET DriverName = ? WHERE DriverID = ?", (new_name, driver_id))

# 26. Обновление информации о поставке автомобиля
def update_car_delivery(cursor, delivery_id, new_car_id, new_driver_id, new_delivery_date):
    cursor.execute("UPDATE CarDeliveries SET CarID = ?, DriverID = ?, DeliveryDate = ? WHERE DeliveryID = ?", (new_car_id, new_driver_id, new_delivery_date, delivery_id))

# 27. Обновление информации о сервисной работе на автомобиле
def update_car_service_record(cursor, service_id, new_car_id, new_service_type, new_service_date, new_cost):
    cursor.execute("UPDATE CarService SET CarID = ?, ServiceType = ?, ServiceDate = ?, Cost = ? WHERE ServiceID = ?", (new_car_id, new_service_type, new_service_date, new_cost, service_id))

# 28. Обновление информации о клиенте
def update_customer(cursor, customer_id, new_name):
    cursor.execute("UPDATE Customers SET CustomerName = ? WHERE CustomerID = ?", (new_name, customer_id))

# 29. Обновление информации о продаже автомобиля
def update_car_sale(cursor, sale_id, new_customer_id, new_car_id, new_sale_date, new_sale_price):
    cursor.execute("UPDATE CarSales SET CustomerID = ?, CarID = ?, SaleDate = ?, SalePrice = ? WHERE SaleID = ?", (new_customer_id, new_car_id, new_sale_date, new_sale_price, sale_id))

# 30. Обновление информации о страховке на автомобиль
def update_car_insurance(cursor, insurance_id, new_car_id, new_insurance_type, new_insurance_date, new_cost):
    cursor.execute("UPDATE CarInsurance SET CarID = ?, InsuranceType = ?, InsuranceDate = ?, Cost = ? WHERE InsuranceID = ?", (new_car_id, new_insurance_type, new_insurance_date, new_cost, insurance_id))

# 31. Удаление производителя автомобилей
def delete_car_manufacturer(cursor, manufacturer_id):
    cursor.execute(
    cursor.execute
    ("DELETE FROM CarManufacturers WHERE ManufacturerID = ?", (manufacturer_id,)))

# 32. Удаление модели автомобиля
def delete_car_model(cursor, model_id):
    cursor.execute("DELETE FROM CarModels WHERE ModelID = ?", (model_id,))

# 33. Удаление доступного автомобиля
def delete_available_car(cursor, car_id):
    cursor.execute("DELETE FROM AvailableCars WHERE CarID = ?", (car_id,))

# 34. Удаление заказа на автомобиль
def delete_car_order(cursor, order_id):
    cursor.execute(
    cursor(
"DELETE FROM CarOrders WHERE OrderID = ?", (order_id,)))

# 35. Удаление водителя
def delete_driver(cursor, driver_id):
    cursor.execute("DELETE FROM Drivers WHERE DriverID = ?", (driver_id,))

# 36. Удаление поставки автомобиля
def delete_car_delivery(cursor, delivery_id):
    cursor.execute(
    cursor.execute
    ("DELETE FROM CarDeliveries WHERE DeliveryID = 1", (delivery_id,)))

# 37. Удаление записи о сервисной работе на автомобиле
def delete_car_service_record(cursor, service_id):
    cursor.execute("DELETE FROM CarService WHERE ServiceID = ?", (service_id,))

# 38. Удаление клиента
def delete_customer(cursor, customer_id):
    cursor.execute("DELETE FROM Customers WHERE CustomerID = ?", (customer_id,))

# 39. Удаление продажи автомобиля
def delete_car_sale(cursor, sale_id):
    cursor.execute("DELETE FROM CarSales WHERE SaleID = ?", (sale_id,))

# 40. Удаление страховки на автомобиль
def delete_car_insurance(cursor, insurance_id):
    cursor.execute("DELETE FROM CarInsurance WHERE InsuranceID = ?", (insurance_id,))

# 41. Получение списка всех моделей автомобилей, производимых определенным производителем
def get_models_by_manufacturer(cursor, manufacturer_id):
    cursor.execute("SELECT * FROM CarModels WHERE ManufacturerID = ?", (manufacturer_id,))
    return cursor.fetchall()

# 42. Получение списка всех доступных автомобилей определенной модели
def get_available_cars_by_model(cursor, model_id):
    cursor.execute("SELECT * FROM AvailableCars WHERE ModelID = ?", (model_id,))
    return cursor.fetchall()

# 43. Получение списка всех заказов на автомобиль, сделанных определенным клиентом
def get_orders_by_customer(cursor, customer_name):
    cursor.execute("SELECT * FROM CarOrders WHERE CustomerName = ?", (customer_name,))
    return cursor.fetchall()

# 44. Получение списка всех поставок автомобилей, сделанных определенным водителем
def get_deliveries_by_driver(cursor, driver_name, driver_id):
    cursor.execute(("SELECT * FROM CarDeliveries WHERE DriverID = 2", (driver_id,)))
    return cursor.fetchall()


# 45. Получение списка всех сервисных работ на автомобилях определенной модели
def get_service_records_by_model(cursor, model_id):
    cursor.execute("SELECT * FROM CarService WHERE CarID IN (SELECT CarID FROM AvailableCars WHERE ModelID = ?)", (model_id,))
    return cursor.fetchall()

# 46. Получение списка всех продаж автомобилей определенному клиенту
def get_sales_by_customer(cursor, customer_id):
    cursor.execute("SELECT * FROM CarSales WHERE CustomerID = ?", (customer_id,))
    return cursor.fetchall()

# 47. Получение списка всех страховок на автомобили определенного типа
def get_insurances_by_type(cursor, insurance_type):
    cursor.execute("SELECT * FROM CarInsurance WHERE InsuranceType = ?", (insurance_type,))
    return cursor.fetchall()

# 48. Получение списка всех заказов на автомобиль в определенную дату
def get_orders_by_date(cursor, order_date):
    cursor.execute("SELECT * FROM CarOrders WHERE OrderDate = ?", (order_date,))
    return cursor.fetchall()

# 49. Получение списка всех поставок автомобилей в определенную дату
def get_deliveries_by_date(cursor, delivery_date):
    cursor.execute("SELECT * FROM CarDeliveries WHERE DeliveryDate = ?", (delivery_date,))
    return cursor.fetchall()

# 50. Получение списка всех сервисных работ на автомобилях в определенную дату
def get_service_records_by_date(cursor, service_date):
    cursor.execute("SELECT * FROM CarService WHERE ServiceDate = ?", (service_date,))
    return cursor.fetchall()



if __name__ == '__main__':
    init_db()
    con = sqlite3.connect('car_dealership.db')
    cursor = con.cursor()
    insert_car_manufacturer(cursor, 'Toyota')
    # Выводим таблицы после вставки данных
    print("CarManufacturers:")
    print(get_all_car_manufacturers(cursor))

    print("\nCarModels:")
    print(get_all_car_models(cursor))

    print("\nAvailableCars:")
    print(get_all_available_cars(cursor))

    print("\nCarOrders:")
    print(get_all_car_orders(cursor))

    print("\nDrivers:")
    print(get_all_drivers(cursor))

    print("\nCarDeliveries:")
    print(get_all_car_deliveries(cursor))

    print("\nCarService:")
    print(get_all_car_service_records(cursor))

    print("\nCustomers:")
    print(get_all_customers(cursor))

    print("\nCarSales:")
    print(get_all_car_sales(cursor))

    print("\nCarInsurance:")
    print(get_all_car_insurances(cursor))
    available_cars = get_available_cars()
    # Закрываем соединение
    con.close()

    available_cars = get_available_cars()
    # for car in available_cars:
    #     print(f"CarID: {car[0]}, ModelID: {car[1]}, Color: {car[2]}, Price: {car[3]}")