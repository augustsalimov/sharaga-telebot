import secrets

RUSSIA = "РА СИ Я!"
RUSSIA_R = ["Россия пишется с большой буквы, бл*ть!"]
MSU = "МГУ сосать!"
NEED_TWO = ["НУЖНО ДВА", "НУЖЕН КУБОК УЕФА!"]
EIGHT = ["800", "555", "35", "35", "лучше позвонить, чем у кого-то занимать"]
ANT = ["Муравью хуй приделать"]
LATE = ["Если никуда не ходить, то и не опоздаешь"]
WITH_YOU = ["Всегда мысленно с тобой"]

TOUGH_ANS_STICK = "CAACAgIAAxkBAAIEbGPsmjrvbsLhpNSBlmOhVj97d03YAAJRKgACNSYhSwdD9VCnilA3LgQ"
TOUGH_ANS_2_STICK= "CAACAgIAAxkBAAIEb2PsnAk73h_fWcMDBRhNaMyONVIyAAIPJgACLLcgS3pH8IACDH8-LgQ"
TOUGH_ANSWERS = [TOUGH_ANS_STICK, TOUGH_ANS_2_STICK]
SIT_STICK = "CAACAgIAAxkBAAIEWGPsjBKjYVTBvcuYLuwG_lRuSgJpAAJQKwACrhkQSzfd4v8zMHNjLgQ"

PHRASES = {
    "РОССИЯ": RUSSIA,
    "Russia": RUSSIA,
    "Россия": RUSSIA,
    "РА СИ Я": RUSSIA,
    "расия": RUSSIA_R,
    "россия": RUSSIA_R,
    "мгу": MSU,
    "мгу сосать": MSU,
    "Нужен гол": NEED_TWO,
    "нужен гол": NEED_TWO,
    "8": EIGHT,
    "Что делать": ANT,
    "что делать": ANT,
    "опоздаю": LATE,
    "Опоздаю": LATE,
    "кто где": WITH_YOU,
    "Кто где": WITH_YOU,
}

STICKS = {
    "сижу": SIT_STICK,
    "Сижу": SIT_STICK,
    "хач": secrets.choice(TOUGH_ANSWERS),
    "чурка": secrets.choice(TOUGH_ANSWERS)
}