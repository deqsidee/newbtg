
# Token telegran bot
bot_token = '1495929256:AAE9ATwoKDXvaLil0t6OPD-X4jYEbWb3zdA' # токен бота
CHANNEL_ID = 1495929256 # id канала куда будет отсылаться информация, ид без -100 в начале (например: 124873248) - указать заместо нуля

# ID admin
admin_id = 744372152 # id админа - указать заместо нуля

bot_login = 'tg_ded_bot' # логин бота
ref_percent = 3 # Процент реферальной системы

QIWI_NUMBER = '+79606091245'    # номер киви
QIWI_TOKEN = '48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iP5pAXYnnT3H6vGQyYSAGLJJmwNoAJS6Fkttb7Nc6JpSTWhwAw8k7GRWy2dsPmjuZy8CMjp6SReNqbmBJFEH1xebBmb3piANk9yCEYSAr1a'            # токен киви

text_purchase = '❕ Вы выбрали: ' \
                '{name}\n\n' \
                '{info}\n\n' \
                '💠 Цена: {price} рублей\n' \
                '💠 Кол-во товара: {amount}' \


# инфа
info = '''❗️ Информация:\n'''

# Пополнение баланса
replenish_balance = '⚠️ Пополнение баланса\n\n' \
                    '🥝 Оплата киви: \n\n' \
                    '👉 Номер  {number}\n' \
                    '👉 Коментарий  {code}\n' \
                    '👉 Сумма  от 1 до 15000 рублей'

# Профиль
profile = '🧾 Профиль\n\n' \
          '❕ Ваш id - {id}\n' \
          '❕ Ваш логин - {login}\n' \
          '❕ Дата регистрации - {data}\n\n' \
          '💰 Ваш баланс - {balance} рублей'
