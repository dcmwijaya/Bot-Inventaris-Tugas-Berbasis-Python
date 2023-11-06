#!/usr/bin/python3.6
import telebot
from telebot import types
import datetime
import pytz

#Waktu
d = datetime.datetime.now()
tz = pytz.timezone("Asia/Jakarta")
d = tz.localize(d)
date = d.strftime("%a, %d-%m-%Y")
timestamp = date

#Api Telegram
api = '6658393237:AAHtW_xpaox4LMOkYRcyHvmGd-79bRTWVEU'
bot = telebot.TeleBot(api)

# unset webhook
bot.remove_webhook()

#Chat ID for notifications
message_id = 'CHAT ID Telegram Anda'

#Message (Alert)
alert_msg = '⚠️ <b>Ada yang mengakses bot anda</b> ❗\n\n🆔 ID = {}\n👤 Nama = {}\n🚹 Username = {}\n📁 Akses Menu = {}\n⏰ Pada = {}'


#Welcome
@bot.message_handler(commands=['start'])
def action_start(message):
  chat_id = message.chat.id
  name = message.from_user.first_name
  last_name = message.from_user.last_name
  if (message.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

  username = message.from_user.username
  id_telegram = message.from_user.id
  menu = '/start'

  custom = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
  a = types.KeyboardButton('/start')

  custom.row(a)

  markdown_html = '<b><a href="https://t.me/Devan_Cakra/">Devan Cakra Mudra Wijaya</a></b>'
  msg = '''📢 Selamat datang di <b>Bot Inventaris Tugas</b>\n\n👋 Hai <b>{}</b>...\n🚹 Username = <b>{}</b>\n🆔 ID = <b>{}</b>

  Buatan : {}
  '''

  bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')
  bot.send_message(chat_id,msg.format(name,username,id_telegram,markdown_html),parse_mode='HTML',reply_markup=custom)




@bot.message_handler(commands=['help'])
def action_help(message):
  chat_id = message.chat.id
  name = message.from_user.first_name
  last_name = message.from_user.last_name
  if (message.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

  username = message.from_user.username
  id_telegram = message.from_user.id
  menu = '/help'

  custom = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
  a = types.KeyboardButton('/start')

  custom.row(a)

  msg = '''🗒️ <b>Menu yang tersedia :</b>\n\n👇👇👇👇👇👇👇👇👇👇👇👇
/start      = mulai
/testbot  = status
/about    = tentang
/date      = waktu
'''''

  bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')
  bot.send_message(chat_id,msg,parse_mode='HTML',reply_markup=custom)


#TestBot
@bot.message_handler(commands=['testbot'])
def action_testbot(message):
  chat_id = message.chat.id
  name = message.from_user.first_name
  last_name = message.from_user.last_name
  if (message.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

  username = message.from_user.username
  id_telegram = message.from_user.id
  menu = '/testbot'

  custom = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
  a = types.KeyboardButton('/start')

  custom.row(a)

  msg = '✅ Status bot :\n---> <b>Saat ini bot aktif...</b>'


  bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')
  bot.send_message(chat_id,msg,parse_mode='HTML',reply_markup=custom)



#About
@bot.message_handler(commands=['about'])
def action_about(message):
  chat_id = message.chat.id
  name = message.from_user.first_name
  last_name = message.from_user.last_name
  if (message.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

  username = message.from_user.username
  id_telegram = message.from_user.id
  menu = '/about'

  msg = '🤖 <b>INFORMASI TENTANG BOT Bot Inventaris Tugas</b>\n\n🔥 <b>Nama bot :</b> \n---> @inventaristugas_bot\n\n👤 <b>Dibuat oleh :</b> \n---> Devan Cakra Mudra Wijaya\n\n✨ <b>Tujuan :</b> \n---> Sebagai pemenuhan tugas\n\n🐍 <b>Bahasa pemrograman :</b> \n---> Python'

  markup = types.InlineKeyboardMarkup()
  inkeyboard = telebot.types.InlineKeyboardButton
  markup.add(inkeyboard(text='🌐 Web profile',url='alamat_web_profil_anda'))
  markup.add(inkeyboard(text='👨🏻‍🎓 Schoolar',url='alamat_schoolar_jika_anda_memilikinya_jika_tidak_ganti_saja'))

  bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')
  bot.send_message(chat_id,msg,reply_markup=markup,parse_mode='HTML')


#Date
@bot.message_handler(commands=['date'])
def action_date(message):
  chat_id = message.chat.id
  name = message.from_user.first_name
  last_name = message.from_user.last_name
  if (message.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

  username = message.from_user.username
  id_telegram = message.from_user.id
  menu = '/date'


  custom = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
  a = types.KeyboardButton('/start')

  custom.row(a)

  msg = '⏰ Current Date : \n---> <b>{}</b>'


  bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')
  bot.send_message(chat_id,msg.format(timestamp),parse_mode='HTML',reply_markup=custom)



#Document New
@bot.message_handler(content_types=['document'])
def kirim_file(message):
  chat_id = message.chat.id
  name = message.from_user.first_name
  last_name = message.from_user.last_name
  if (message.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

  username = message.from_user.username
  id_telegram = message.from_user.id
  menu = 'send document'

  pdf = message.document
  file_id = pdf.file_id
  pdf_name = pdf.file_name
  file = bot.get_file(file_id)
  file_loc = file.file_path
  download = bot.download_file(file_loc)

  with open (pdf_name,"wb") as f:
    f.write(download)

  msg = 'Terima kasih <b>{}</b>, anda telah mengirimkan tugas pada <b>Bot Inventaris Tugas</b>.\n\n📁 Nama file = <b>{}</b>\n\n⏰ Pada = <b>{}</b>\n\n📚 File dapat diakses pada : <b>alamat_file_yang_dapat_diakses</b>'
  bot.send_message(chat_id,msg.format(name, pdf_name, timestamp),parse_mode='HTML')
  bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')


#Handle wrong commands
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  usermsg = message.text
  name = message.from_user.first_name
  last_name = message.from_user.last_name
  if (message.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

  username = message.from_user.username
  id_telegram = message.from_user.id
  menu = 'default'

  msg = '👋 Hai <b>{}</b>\n\nPerintah <b>"{}"</b> pada menu tidak tersedia.\n\nSilahkan akses <b>/help</b> untuk mengetahui pilihan menu yang tersedia.'
  bot.reply_to(message,msg.format(name,usermsg),parse_mode='HTML')
  bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')



#Welcome new member group
@bot.message_handler(func=lambda m: True, content_types=["new_chat_members"])
def on_user_joins(new_chat_members):
    name = new_chat_members.from_user.first_name
    last_name = new_chat_members.from_user.last_name
    if (new_chat_members.from_user.last_name, 'last_name') is not None:
        name += " {}".format(last_name)

    username = new_chat_members.from_user.username
    id_telegram = new_chat_members.from_user.id
    menu = 'welcome'

    pesan = '👋 Selamat datang <b>{}</b> di <b>Bot Inventaris Tugas</b>. Semoga anda merasa nyaman dan selalu berbahagia'


    bot.reply_to(new_chat_members, pesan.format(name),parse_mode='HTML')
    bot.send_message(message_id,alert_msg.format(id_telegram,name,username,menu,timestamp),parse_mode='HTML')



print('bot berhasil dijalankan....')
bot.polling()
