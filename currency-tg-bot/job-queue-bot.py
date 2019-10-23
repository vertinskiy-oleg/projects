import telegram.ext
from telegram.ext import Updater

user_id = '195895849'
token = '734516183:AAEs81N8bZdFK4YqwpBsYm7CODXNoe-1nqY'

updater = Updater(token, use_context=True)
jobs = updater.job_queue

def callback_minute(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=user_id, 
                             text='One message every minute')

job_minute = jobs.run_repeating(callback_minute, interval=60, first=0)

updater.start_polling()

