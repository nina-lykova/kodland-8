import telebot 
from config import token
from logic import Pokemon, Wizard, Fighter, randint

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        img_url = pokemon.show_img()
        bot.send_photo(message.chat.id, photo=img_url)

        if message.from_user.username not in Pokemon.pokemons.keys():
            chance = randint(1,3)
            if chance == 1:
                pokemon = Pokemon(message.from_user.username)
            elif chance == 2:
                pokemon = Wizard(message.from_user.username)
            elif chance == 3:
                pokemon = Fighter(message.from_user.username)
        
    else:
        bot.reply_to(message, "Покемон уже создан")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        attacker_username = message.from_user.username
        defender_username = message.reply_to_message.from_user.username

        attacker = Pokemon.pokemons.get(attacker_username)
        defender = Pokemon.pokemons.get(defender_username)

        if attacker and defender:
            print(f"Атакующий: {attacker.pokemon_trainer}, HP: {attacker.hp}, Сила: {attacker.power}")
            print(f"Защищающийся: {defender.pokemon_trainer}, HP: {defender.hp}, Сила: {defender.power}")

            result = attacker.attack(defender)
            bot.send_message(message.chat.id, result)

        else:
            bot.send_message(message.chat.id, "Нельзя атаковать самого себя или такого покемона не существует.")
    else:
        bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщение покемона!")

bot.infinity_polling(none_stop=True)

