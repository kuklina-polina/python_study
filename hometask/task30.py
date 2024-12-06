# user: Polina Kuklina
# date creation: 06.12.2024
print("_________________________________")
import psycopg2
import config
from abc import ABC, abstractmethod

#  1. Реализовать класс DB - синглтон. Экземляр класса(подключение) к PostgreSQL
#  должно быть единственным.
class DBConn:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn  = self.connect()

    def connect(self):
        try:

            return psycopg2.connect(
                user=self.user,
                password=self.passwd,
                host=self.host,
                port=self.port,
                database=self.db
            )

        except psycopg2.OperationalError as e:
            print("I am unable to connect to the database")
            print(e)
    def __str__(self):
        return f"Пользователь {self.user} подключен к {self.db}"

db = DBConn(config.host, config.port, config.user, config.passwd, config.db)
db2 = DBConn(config.host, config.port, "postgres", "postgres", config.db)

print("Разные пользователи передавались, но ... Синглтон справился, подключение одно")
print("db = " + str(db))
print("db2 = " + str(db2))
print(f"Являются ли подключения 1 и 2 одним объектом? {db is db2}")

print("_________________________________")
#  2. Реализовать  фабрику которая создает модели различных производителей

class Car:
    def __init__(self, brand, model):
        """Инициализируйте атрибуты brand и model"""
        self.brand = brand
        self.model = model

    @classmethod
    def make_lada(cls, model):
        "реализуйте метод для создания  автомобиля Lada"
        return cls("Lada", model)

    @classmethod
    def make_mercedes(cls, model):
        "реализуйте метод для создания  автомобиля Mercedes"
        return cls("Mercedes", model)

    @classmethod
    def make_toyota(cls, model):
        "реализуйте метод для создания создания Toyota"
        return cls("Toyota", model)

    def __repr__(self):
        "Реализуйте логику дандера"
        return f"И это аааааавтомобиль: бренда — {self.brand}, модель — {self.model}"

print(Car.make_lada("Granta"))
print(Car.make_mercedes("Granta"))
print(Car.make_toyota("Granta"))
print("_________________________________")

# 3. Реализовать для класса Car абстрактный класс который содержит aбстрактные методы sold, discount

class AbsClassCar(ABC):
    @abstractmethod
    def sold(self):
        """Автомобиль продан"""
        pass

    @abstractmethod
    def discount(self):
        """Скидка на автомобиль"""
        pass

class CombCar_Info(ABC, Car):
    car = None
    def __init__(self, brand, model):
        self.car = Car(brand, model)

    def sold(self):
        """Автомобиль продан"""
        print(f"Автомобиль {self.car.brand} {self.car.model} продан ")

    def discount(self):
        """Скидка на автомобиль"""
        print(f"На автомобиль {self.car.brand} {self.car.model} скидка 5%")

CombCar_Info.make_lada("Granta").discount()
CombCar_Info.make_mercedes("Granta").sold()
CombCar_Info.make_toyota("Granta").discount()
print("_________________________________")