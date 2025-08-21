import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime

from config import *

# Список возможных мест для панды
LOCATIONS = [
    (TREE_EMOJI, "tree"),
    (BUSH_EMOJI, "bush"),
    (ROCK_EMOJI, "rock")
]

def print_with_timestamp(message):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] {message}")

def get_main_keyboard():
    keyboard = [
        [KeyboardButton("🎮 Играть"), KeyboardButton(f"{INFO_EMOJI} О боте")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def start(update: Update, context: CallbackContext):
    reply_markup = get_main_keyboard()
    update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)
    print_with_timestamp(f"Пользователь {update.effective_user.first_name} начал игру")

def play_game(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton(f"{HORSE_EMOJI} Найдите банан"), KeyboardButton("⟸ Назад")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(CHOOSE_GAME_MESSAGE, reply_markup=reply_markup)
    print_with_timestamp(f"Пользователь {update.effective_user.first_name} выбрал игру")

def about_bot(update: Update, context: CallbackContext):
    reply_markup = get_main_keyboard()
    update.message.reply_text(ABOUT_BOT_MESSAGE, reply_markup=reply_markup)
    print_with_timestamp(f"Пользователь {update.effective_user.first_name} открыл информацию о боте")

def find_panda(update: Update, context: CallbackContext):
    # Выбираем случайное место для панды
    correct_location = random.choice(LOCATIONS)
    context.user_data['correct_location'] = correct_location

    # Создаем кнопки с локациями в один ряд
    keyboard = [
        [KeyboardButton(emoji) for emoji, _ in LOCATIONS]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(FIND_HORSE_MESSAGE, reply_markup=reply_markup)
    print_with_timestamp(f"Банан спрятался за {correct_location[0]}")

def handle_message(update: Update, context: CallbackContext):
    message_text = update.message.text
    
    if message_text == "🎮 Играть":
        play_game(update, context)
        return
        
    if message_text == f"{INFO_EMOJI} О боте":
        about_bot(update, context)
        return
        
    if message_text == f"{HORSE_EMOJI} Найдите банан":
        find_panda(update, context)
        return

    if message_text == "⟸ Назад":
        reply_markup = get_main_keyboard()
        update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)
        print_with_timestamp(f"Пользователь {update.effective_user.first_name} вернулся в главное меню")
        return
        
    # Проверяем, является ли сообщение эмодзи локации
    for emoji, location in LOCATIONS:
        if message_text == emoji:
            correct_location = context.user_data.get('correct_location')
            if not correct_location:
                return
                
            if (emoji, location) == correct_location:
                update.message.reply_text(HORSE_FOUND_MESSAGE, reply_markup=get_main_keyboard())
                print_with_timestamp(f"Пользователь {update.effective_user.first_name} нашёл банан!")
            else:
                update.message.reply_text(f"{HORSE_NOT_FOUND_MESSAGE} {correct_location[0]}", 
                                        reply_markup=get_main_keyboard())
                print_with_timestamp(f"Пользователь {update.effective_user.first_name} не нашёл банан")
            return

def main():
    print_with_timestamp("Запуск Banana бота...")
    print_with_timestamp("Подключение к Telegram API...")
    
    # Создаем updater с токеном
    updater = Updater(token=BOT_TOKEN, use_context=True)
    print_with_timestamp("Подключение успешно!")

    # Получаем dispatcher для регистрации обработчиков
    dp = updater.dispatcher

    # Добавляем обработчики
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print_with_timestamp("Бот Banana успешно запущен и готов к работе!")
    print_with_timestamp("Для остановки бота нажмите Ctrl+C")
    print("-" * 50)

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 