import os
from dotenv import load_dotenv

load_dotenv()

# Напрямую устанавливаем токен для тестирования
BOT_TOKEN = "8421451341:AAF7N5Gat580Gjhy4SVL-PObVqNDLLBr0os"

# Эмодзи для игры
HORSE_EMOJI = "🍌"
BAMBOO_EMOJI = "🎋"
TREE_EMOJI = "🌳"
BUSH_EMOJI = "🌿"
ROCK_EMOJI = "🪨"
INFO_EMOJI = "ℹ️"

# Тексты сообщений
WELCOME_MESSAGE = f"Здравствуйте! {HORSE_EMOJI} Добро пожаловать в Banana Game!\nВыберите действие:"
CHOOSE_GAME_MESSAGE = "Выберите игру!"
FIND_HORSE_MESSAGE = f"Где спрятался банан? {HORSE_EMOJI} Выбирайте:"
HORSE_FOUND_MESSAGE = f"{HORSE_EMOJI} Вы нашли банан! {BAMBOO_EMOJI}"
HORSE_NOT_FOUND_MESSAGE = "😔 Нет, банана тут нет. Он был в"

ABOUT_BOT_MESSAGE = f"{INFO_EMOJI} Banana Game — это лёгкий бот с мини-играми про банан! Найдите свой банан!"


