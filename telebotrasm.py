from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import random
import os

font = ImageFont.truetype("Rossanova-Bold.ttf",size=100)

import logging
from typing import Dict
from telegram.error import TimedOut,BadRequest,ChatMigrated,Conflict,NetworkError,RetryAfter,TelegramError,Unauthorized
import time

from telegram import ReplyKeyboardMarkup,Update, ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler
)
import telegram
bot = telegram.Bot(token='5024408760:AAEspXu5yZbg4dE0r2UplZcwb60Y89ryKo0',)


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ['Ism Kiritish'],
#    ['Boshqa narsalar...'],
    ['Rasmni olish!🌉🌁'],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True)


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f"{value}" for key, value in user_data.items()]
    return " ".join(facts)

def admin_window(update: Update,callback: CallbackContext) -> None:
    user = update.message.from_user

    admins = [1747078487,1285975410]
    reply_keyboard1 = [
        [InlineKeyboardButton(text='Foydaluvchi soni',callback_data='1')],
       # [InlineKeyboardButton(text='Habarni kiritish',callback_data='2')],
        #    ['Boshqa narsalar...'],
    ]
    if user['id'] in admins:
        replybut = InlineKeyboardMarkup(reply_keyboard1)
        #markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text('Shulardan birini tanlang:', reply_markup=replybut)





def start(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask user for input."""

    admins = [1747078487, 1285975410]

    user = update.message.from_user

    data = pd.read_csv('userinfo.csv', sep=',')


    id = user['username']
    info = user['id'],
    info1 = user['id']
    # now it is time to add info to excel file
    if info1 not in list(data['userid']):
        data1 = pd.DataFrame({'id': id,
                              'userid': info})
        data1.to_csv('userinfo.csv', mode='a', index=False, header=False)
    # return to admin window

    if user['id'] in admins:
        admin_window(update,context)
    try:
        update.message.reply_text(
            "Assalomu alaykum men Tabrik botman. "
            "Siz menga yaqiningizni ismini jo'natsangiz men sizga 🎊tabrik yasab beraman.",
            reply_markup=markup,
        )
    except TimedOut as e:
        time.sleep(0.001)
        return start(update,context)
    except BadRequest as e:
        time.sleep(0.001)
        return start(update,context)
    except ChatMigrated as e:
        time.sleep(0.001)
        return start(update,context)
    except Conflict as e:
        time.sleep(0.001)
        return start(update,context)
    except NetworkError as e:
        time.sleep(0.001)
        return start(update,context)
    except RetryAfter as e:
        time.sleep(0.001)
        return start(update,context)
    except TelegramError as e:
        time.sleep(0.001)
        return start(update,context)


    return CHOOSING



def regular_choice(update: Update, context: CallbackContext) -> int:
    """Ask the user for info about the selected predefined choice."""
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(f'Yaqiningizni Ismini jonating!')
    return TYPING_REPLY



def the_number_of_users(update: Update, context: CallbackContext,) -> int:
    """Ask the user for info about the selected predefined choice."""
    query = update.callback_query
    query.answer()

    if query.data == '1':
        data = pd.read_csv('userinfo.csv', sep=',')
        numbers = list(data['userid'])
        update.callback_query.message.edit_text(f"Foydalanuvchilar soni: {len(numbers)}")
    #elif query.data == '2':
    #    update.callback_query.message.edit_text(
    #        f"Itimos menga habaringizni jonating men uni bot foydalanuvchilariga "
    #        f"yuboraman albatta matnni hatosiz ekanligini kozdan kechiring chunki"
    #        f"habarni qayatrib bolmaydi.")
    #    main_handler(update,context)
        return CHOOSING






#def custom_choice(update: Update, context: CallbackContext) -> int:
#    """Ask the user for a description of a custom category."""
#    update.message.reply_text(
#        'Albatta, birinchi menga kategoriyani jonating, masalan "Ish Manzil:"'
#    )
#
#    return TYPING_CHOICE
def main_handler(update:Update, context: CallbackContext):
    #this function sends message to the all members of the group



    data = pd.read_csv('userinfo.csv', sep=',')
    useridslist = list(data['userid'])
    admins = [1054132889,1285975410 ]


    #bot.sendPhoto(photo=open('bekzod.jpg','rb'),caption='bekzotning rasmi',chat_id=1285975410)
    #update.message.reply_media_group(update.message.forward)



    try:
        if update.message.from_user['id'] in admins:
            if '/send' in update.message.caption:
                update.message.caption = (update.message.caption).replace('/send','')
                photo_file = update.message.photo[-1].get_file()
                photo_file.download('user_photo1.jpg')
                for i in useridslist:
                    pic = open('user_photo1.jpg', 'rb')
                    bot.send_photo(photo=pic, caption=update.message.caption,chat_id=i)
                    pic.close()
                    #os.remove('user_photo1.jpg')
                update.message.reply_text("habar yuborildi!")
    except TimedOut as e:
        time.sleep(0.001)
        return start(update, context)
    except BadRequest as e:
        time.sleep(0.001)
        return start(update, context)
    except ChatMigrated as e:
        time.sleep(0.001)
        return start(update, context)
    except Conflict as e:
        time.sleep(0.001)
        return start(update, context)
    except NetworkError as e:
        time.sleep(0.001)
        return start(update, context)
    except RetryAfter as e:
        time.sleep(0.001)
        return start(update, context)
    except TelegramError as e:
        time.sleep(0.001)
        return start(update, context)
    return CHOOSING




def received_information(update: Update, context: CallbackContext) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    del user_data['choice']

    update.message.reply_text(
    f"Yaqiniz ismi: {facts_to_str(user_data).title()}✅\n"
    f"Ismni o\'zgartish uchun qaytadan♻️  Ism Kiritish, yoki Rasmni olish tugmasini bosing!",
    reply_markup=markup,
    )


    return CHOOSING
def received_information_from_admin(update: Update, context: CallbackContext) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    del user_data['choice']

    update.message.reply_text(
        f"Yaqiniz ismi: {facts_to_str(user_data).title()}.\n"
        f"Ismni o\'zgartish uchun qaytadan ismni kiritish",
    )

    return CHOOSING


def done(update: Update, context: CallbackContext) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text(
        f"Ushbu ism asosida tabrik: {facts_to_str(user_data)} , Qayta foydalanish uchun /start bosing!",
        reply_markup=ReplyKeyboardRemove(),
    )

#    print('You talk with user {} and his user ID: {}'.format(user['username'], user['id']))





    try:
        malumot = facts_to_str(user_data)
        pic = random.choice([Image.open('renamedpictureone1.jpg'),Image.open('renamedpicturetwo2.jpg'),Image.open('1.jpg')])


        #rasmlarni random qilib ulardan birini jonatamiz
        draw = ImageDraw.Draw(pic)
        draw.text((500, 540), text=malumot.title(), font=font,fill=(255,0,0))



        pic.save(f"{malumot}.jpg")

        file = open(f"{malumot}.jpg",'rb')
        update.message.reply_photo(photo=file, caption="@yangi_yil_tabrikbot")
        file.close()
        #os.remove(f"{malumot}.jpg")
    except:
        return start(update,context)





    user_data.clear()
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5024408760:AAEspXu5yZbg4dE0r2UplZcwb60Y89ryKo0",use_context=True                                                     )

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher





    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(Ism Kiritish)$'), regular_choice
                ),
                #MessageHandler(Filters.regex('^Boshqa narsalar...$'), custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Rasmni olish!🌉🌁$')), regular_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Rasmni olish!🌉🌁$')),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Rasmni olish!🌉🌁$'), done)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.dispatcher.add_handler(CallbackQueryHandler(the_number_of_users))
    updater.dispatcher.add_handler(MessageHandler(Filters.text,main_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo,main_handler))
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()