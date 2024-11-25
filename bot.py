from aiogram import Bot, Dispatcher, executor, types
import a2s

bot = Bot(token='7813730370:AAEURqMT2soxlhGZcUyJYSEKEoPsi1el1Po')
dp = Dispatcher(bot=bot)

SERVER_IP = '5.182.26.211'
SERVER_PORT1 = 27016
# SERVER_PORT2 = 27015
# SERVER_PORT3 = 27017
# SERVER_PORT4 = 27018
SERVER_PORT5 = 27001
SERVER_PORT6 = 27002
SERVER_PORT7 = 27003
SERVER_PORT8 = 27004
ERROR = "Server ma'lumotlari topilmadi!"

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id, text='''Это официальный ИНФО бот - CS Imperia✅

Наш ТГ: @csimperia
АДМИН: @isroil_leo93

Введите команду /public и /cwar ⁉️''')

@dp.message_handler(commands=['public'])
async def info_serv(message: types.Message):
    try:
        info1 = a2s.info((SERVER_IP, SERVER_PORT1))
        max_players1 = info1.max_players
        player1 = info1.player_count
        map_name1 = info1.map_name
        server_name1 = info1.server_name

        # info2 = a2s.info((SERVER_IP, SERVER_PORT2))
        # max_players2 = info2.max_players
        # player2 = info2.player_count
        # map_name2 = info2.map_name
        # server_name2 = info2.server_name

        # info3 = a2s.info((SERVER_IP, SERVER_PORT3))
        # max_players3 = info3.max_players
        # player3 = info3.player_count
        # map_name3 = info3.map_name
        # server_name3 = info3.server_name

        # info4 = a2s.info((SERVER_IP, SERVER_PORT4))
        # max_players4 = info4.max_players
        # player4 = info4.player_count
        # map_name4 = info4.map_name
        # server_name4 = info4.server_name

        text_info = f'''<b>🔸 {server_name1}</b>
<b>🔹 IP:</b>  <em>{SERVER_IP}:{SERVER_PORT1}</em>
<b>👥 Игроков:</b> <em>{player1}/{max_players1}</em>
<b>🗾 Карта:</b> <em>{map_name1}</em>
➖➖➖➖➖➖➖➖➖➖
😎Гл.Админ: @isroil_leo93'''

        await message.reply(text=text_info, parse_mode='HTML')

    except Exception:
        await message.reply(text=ERROR)


@dp.message_handler(commands=['cwar'])
async def info_serv(message: types.Message):
    try:
        info5 = a2s.info((SERVER_IP, SERVER_PORT5))
        max_players5 = info5.max_players
        player5 = info5.player_count
        map_name5 = info5.map_name
        server_name5 = info5.server_name

        info6 = a2s.info((SERVER_IP, SERVER_PORT6))
        max_players6 = info6.max_players
        player6 = info6.player_count
        map_name6 = info6.map_name
        server_name6 = info6.server_name

        info7 = a2s.info((SERVER_IP, SERVER_PORT7))
        max_players7 = info7.max_players
        player7 = info7.player_count
        map_name7 = info7.map_name
        server_name7 = info7.server_name

        info8 = a2s.info((SERVER_IP, SERVER_PORT8))
        max_players8 = info8.max_players
        player8 = info8.player_count
        map_name8 = info8.map_name
        server_name8 = info8.server_name

        text_info1 = f'''<b>🔸</b> {server_name5}
<b>🔹IP:</b> {SERVER_IP}:{SERVER_PORT5}
<b>👥Игроков:</b> {player5}/{max_players5}
<b>🗾Карта:</b> {map_name5}
➖➖➖➖➖➖➖➖➖➖
<b>🔸</b> {server_name6}
<b>🔹IP:</b> {SERVER_IP}:{SERVER_PORT6}
<b>👥Игроков:</b> {player6}/{max_players6}
<b>🗾Карта:</b> {map_name6}
➖➖➖➖➖➖➖➖➖➖
<b>🔸</b> {server_name7}
<b>🔹IP:</b> {SERVER_IP}:{SERVER_PORT7}
<b>👥Игроков:</b> {player7}/{max_players7}
<b>🗾Карта:</b> {map_name7}
➖➖➖➖➖➖➖➖➖➖
<b>🔸</b> {server_name8}
<b>🔹IP:</b> {SERVER_IP}:{SERVER_PORT8}
<b>👥Игроков:</b> {player8}/{max_players8}
<b>🗾Карта:</b> {map_name8}
➖➖➖➖➖➖➖➖➖➖
😎Гл.Админ: @isroil_leo93'''

        await message.reply(text=text_info1, parse_mode='HTML')

    except Exception:
        await message.reply(text=ERROR)

if (__name__ == '__main__'):
    executor.start_polling(dispatcher=dp, skip_updates=True)


# <b>🔸</b> {server_name2}
# <b>🔹IP:</b> {SERVER_IP}:{SERVER_PORT2}
# <b>👥Игроков:</b> {player2}/{max_players2}
# <b>🗾Карта:</b> {map_name2}
# ➖➖➖➖➖➖➖➖➖➖
# <b>🔸</b> {server_name3}
# <b>🔹IP:</b> {SERVER_IP}:{SERVER_PORT3}
# <b>👥Игроков:</b> {player3}/{max_players3}
# <b>🗾Карта:</b> {map_name3}
# ➖➖➖➖➖➖➖➖➖➖
# <b>🔸</b> {server_name4}
# <b>🔹IP:</b> {SERVER_IP}:{SERVER_PORT4}
# <b>👥Игроков:</b> {player4}/{max_players4}
# <b>🗾Карта:</b> {map_name4}
# ➖➖➖➖➖➖➖➖➖➖