from random import randint
import requests
from datetime import datetime, timedelta


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, feed_interval, hp_range=(100, 1000), power_range=(100, 1000)):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        
        self.hp_range = hp_range
        self.power_range = power_range

        self.hp = randint(*self.hp_range)
        self.power = randint(*self.power_range)
        self.feed_interval = feed_interval

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  
            return (data['sprites']["other"]['official-artwork']["front_default"])
        else:
            return "https://i.pinimg.com/originals/b9/c7/c5/b9c7c50da1fc0b8c97b9c75eee2603a2.png"
        
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, сила: {self.power}, хп: {self.hp} "
    
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    # Метод атаки
    def atack(self, enemy):
        if isinstance(enemy, Wizard):
            shans = shans.randint(1,5)
            if shans == 1:
                return f"У волшебника @{enemy.pokemon_trainer} что-то пошло не так... Ничего не произошло!"
        
        elif enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
              
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    
    
    #Метод кормления
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"



class Wizard(Pokemon):
    def attack(self):
        pass
    def feed(self, feed_interval=10, hp_increase=10):  # Уменьшенный интервал кормления
        return super().feed(feed_interval=feed_interval, hp_increase=hp_increase)

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(100,1000)
        self.power += super_power
        result = super().attack(enemy)
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    
    def feed(self, feed_interval=20, hp_increase=15):  # Увеличенное увеличение HP
        return super().feed(feed_interval=feed_interval, hp_increase=hp_increase)
        


