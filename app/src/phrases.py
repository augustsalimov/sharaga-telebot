import secrets
from dataclasses import dataclass


RUSSIA = "РА СИ Я!"
MSU = "МГУ СОСАТЬ!"
RUSSIA_R = ["Россия пишется с большой буквы", "неуч..."]


RUSSIA_MSU = {
    "РОССИЯ": RUSSIA,
    "Russia": RUSSIA,
    "Россия": RUSSIA,
    "Россия!": RUSSIA,
    "РА СИ Я": RUSSIA,
    "расия": RUSSIA_R,
    "россия": RUSSIA_R,
    "мгу": MSU,
    "МГУ": MSU,
    "МГУ СОСАТЬ": MSU,
    "мгу сосать": MSU,
}


PHRASES = {
    "нужен гол": ["НУЖНО ДВА", "НУЖЕН КУБОК УЕФА!"],
    "8": ["800", "555", "35", "35", "лучше позвонить, чем у кого-то занимать"],
    "что делать": ["Муравью хуй приделать"],
    "опоздаю": ["Если никуда не ходить, то и не опоздаешь"],
    "кто где": ["Всегда мысленно с тобой"],
}


TOUGH_ANS_STICK = "CAACAgIAAxkBAAIEbGPsmjrvbsLhpNSBlmOhVj97d03YAAJRKgACNSYhSwdD9VCnilA3LgQ"
TOUGH_ANS_2_STICK= "CAACAgIAAxkBAAIEb2PsnAk73h_fWcMDBRhNaMyONVIyAAIPJgACLLcgS3pH8IACDH8-LgQ"
TOUGH_ANSWERS = [TOUGH_ANS_STICK, TOUGH_ANS_2_STICK]
SIT_STICK = "CAACAgIAAxkBAAIEWGPsjBKjYVTBvcuYLuwG_lRuSgJpAAJQKwACrhkQSzfd4v8zMHNjLgQ"


STICKS = {
    "рецепт": TOUGH_ANS_2_STICK,
    "сижу": SIT_STICK,
    "хач": secrets.choice(TOUGH_ANSWERS),
    "чурка": secrets.choice(TOUGH_ANSWERS)
}