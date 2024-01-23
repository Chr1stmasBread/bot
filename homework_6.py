import telebot
import time
from info_quizz import *
bot = telebot.TeleBot(TOKEN)
users_data = {

}
def dead(message):
    dead_s = ".\screen_1\dead.jpg"
    with open(dead_s, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(2)
    bot.send_message(message.chat.id, "Если Вы хотите попрбовать еще раз, напишите /start")
def win(message):
    win_s = ".\screen_1\win.jpg"
    with open(win_s, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(2)
    bot.send_message(message.chat.id, "Если Вы хотите попрбовать еще раз, напишите /start")
@bot.message_handler(commands=['start'])
def start(message):
    users_data[message.chat.id] = {
        'deistvie': None,
        'ammo': None,
    }
    bot.send_message(message.chat.id, "Привет, вам предстоит пройти текстовый квиз!")
    start_quizz(message)
def start_quizz(message):
    bot.send_message(message.chat.id,
        "Вы оказались на необитаемом острове.")
    island_s = ".\screen_1\island.jpg"
    with open(island_s, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id,"У вас есть несколько действий\n"
        "1. Отправиться изучать остров\n"
        "2. Идти в лес\n"
        "3. Остаться на месте"
                     )
    bot.register_next_step_handler(message, test) # ожидание ввода пользователя и после переход к следующему шагу


def test(message):
    if message.text in ['1', '2', '3']: # вывод результата
        if message.text == '1':
            users_data[message.chat.id] = 1
            test_1(message)
        elif message.text == '2':
            users_data[message.chat.id] = 2
            test_2(message)
        else:
            users_data[message.chat.id] = 3
            test_3(message)
    else: # если не корректен ввод просим ввести заново
        bot.send_message(message.chat.id, "Введите 1, 2 или 3!")
        bot.register_next_step_handler(message, test)
def test_1(message):
    bot.send_message(message.chat.id, "Вы отправились изучать остров")
    bot.send_message(message.chat.id, "Пока вы изучали остров, вы нашли поселение дикарей-канибалов.")
    back_s_1 = ".\screen_1\canibal.jpg"
    with open(back_s_1, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Вы пришли в шок.")
    time.sleep(2)
    bot.send_message(message.chat.id, "Вы решаете убежать от этого места, но вас замечают пару жителей этого поселения.")
    time.sleep(5)
    bot.send_message(message.chat.id, "Спустя какое-то время вы уже мертвы, а вам обедают дикари.")
    dead(message)

def test_2(message):
    bot.send_message(message.chat.id, "Вы идете в лес")
    bot.send_message(message.chat.id, "Пока Вы ходили по лесу, Вы нашли поселение дикарей-канибалов.")
    back_s_2 = ".\screen_1\canibal.jpg"
    with open(back_s_2, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Вы пришли в шок.")
    time.sleep(2)
    bot.send_message(message.chat.id, "Вы решаетесь убежать от этого места, но вас замечают пару жителей этого поселения.")
    time.sleep(5)
    bot.send_message(message.chat.id, "Спустя какое-то время вы уже мертвы, а вам обедают дикари.")
    dead(message)
def test_3(message):
    bot.send_message(message.chat.id, "Вы решили остаться на месте, где вы и очнулись.")
    later = ".\screen_1\moment_later.jpeg"
    time.sleep(1)
    with open(later, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(1)
    bot.send_message(message.chat.id, "Вы освоились, построили небольшой домик на окраине острова, выживаете.")
    back_s_3_1 = ".\screen_1\if_3_1.jpg"
    with open(back_s_3_1, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Спустя несколько лет, Вы видите его КОРАБЛЬ, который идет недалеко от Вашего острова, что вы будете делать?\n"
                                      "1. Попытаетесь доплыть сами.\n"
                                      "2. Добежите до возвышенности острова, и попытаетесь привлечь внимаение\n"
                                      "3. Поймете что у вас есть шанс на спасение в будущем, и начнете строить плот")
    bot.register_next_step_handler(message, test_3_if)
def test_3_if(message):
    if message.text in ['1', '2', '3']:
        if message.text == '1':
            test_3_1(message)
        elif message.text == '2':
            test_3_2(message)
        else:
            test_3_3(message)
    else:
        bot.send_message(message.chat.id, "Введите 1, 2 или 3!")
        bot.register_next_step_handler(message, test_3_if)
def test_3_1(message):
    bot.send_message(message.chat.id, "Вы решаетесь доплыть до корабля своими силами.")
    swim = ".\screen_1\swim_to_cargo.jpg"
    with open(swim, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Вам не хватает сил, и вы отключаетесь прямо в воде.")
    dead(message)
def test_3_2(message):
    bot.send_message(message.chat.id, "Вы решаетесь добежать до возвышенности острова, и попытаетесь привлечь внимаение")
    run = ".\screen_1\!run.jpg"
    with open(run, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Пока Вы бежали, Вы заметили дикарей-канибалов, Вы решили остановиться и изучить их, они были похожи на людей, но разговаривали на непонятном вам языке, Вы начили их изучать и назвали их 'Шорики'.")
    bot.send_message(message.chat.id, "Спустя несколько лет изучений, Вы изучили их настолько досканально что знали о них Все, и решили проводить над ними опыты, у себя в доме.")
    bot.send_message(message.chat.id, "Вам наскучили, эти 'изучения', и Вы решили проверить их способности по охоте на людей. Но где же вам взять людей? *Продолжение следует ...*")
    continue_s = ".\screen_1\continued.jpeg"
    with open(continue_s, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Если Вы хотите попрбовать еще раз, напишите /start")

def test_3_3(message):
    bot.send_message(message.chat.id, "Вы решаетесь подождать еще некоторое время, и пока вы ждете, вы строите плот.")
    raw = ".\screen_1\!raw.jpg"
    with open(raw, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Спустя несколько лет ожиданий, Вы решаете поплыть в неизвестном направлении на построеном Вами плоту, берете с собой запасы еды, воды.")
    swim_raw = ".\screen_1\swim_with_raw.jpg"
    with open(swim_raw, 'rb') as f:
        bot.send_photo(message.chat.id, f)
    bot.send_message(message.chat.id, "Спустя несколько лет ожиданий, Вас находит мимо проходящий корабль, и подбирает вас.")
    win(message)
bot.polling()