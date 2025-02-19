class Animal:
    def __init__(self, name, animal_type, gender, food, habitat, classes, age=0): 
        self.__name = name
        self.__animal_type = animal_type
        self.__gender = gender
        self.__food = food
        self.__habitat = habitat
        self.__classes = classes
        self.__age = age

    def name(self):
        print(f"hello, I am {self.__name}")

    def gender(self):
        print(f"hello, I am {self.__gender}")

    def animal(self):
        print(f"I am a {self.__animal_type}")
    
    def age(self):
        print(f"I am {self.__age} years old")

    def food(self):
        print(f"I eat {self.__food}")

    def habitat(self):
        print(f"As a {self.__animal_type} I live in {self.__habitat}")

    def classes(self):
        print(f"We {self.__animal_type} are {self.__classes}")

    def talk(self):
        print("hi")

