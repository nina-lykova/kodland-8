from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, hp_range=(100, 1000), power_range=(100, 1000)):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        
        self.hp_range = hp_range
        self.power_range = power_range

        self.hp = randint(*self.hp_range)
        self.power = randint(*self.power_range)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            img_url =  (data["sprites"]["other"]["dream_world"]["front_default"])
            return print(f"URL картинки: {img_url}")
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

class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(100,1000)
        self.power += super_power
        result = super().attack(enemy)
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
        


