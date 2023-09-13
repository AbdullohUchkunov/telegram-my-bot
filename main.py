from telegram.ext import CommandHandler,Updater,CallbackQueryHandler,MessageHandler,Filters,ConversationHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from database import Database
from commons import *
from inline import inline_handler
from tk import TOK
# from kurs_dollar import list_1
# num_1 = list_1[-1]
# number = 998_97_709_00_04
# number_2 = 998_90_300_09_04
# admin = "@pantera0904"

db = Database("pantera.db")


def start_handlar(update, context):
    context.user_data['language'] = None
    context.user_data['data'] = None
    buttons = [
        [KeyboardButton(text="🇺🇿 UZBEK"),KeyboardButton(text="🇷🇺 РУССКИЙ"),KeyboardButton(text="🇬🇧 ENGLISH")]
    ]
    update.message.reply_text(text="Tilni tanlang:\nВыберите язык:\nChoose language:",
                              reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True))
def message_handler(update, context):
    message = update.message.text
    if message == "🇺🇿 UZBEK":
        context.user_data['language'] = message
        product = db.get_all_product_by_uz()
        send_product(context=context, products=product, chat_id=update.message.from_user.id)
    elif message == "🇷🇺 РУССКИЙ":
        context.user_data['language'] = message
        product = db.get_all_product_by_rus()
        send_product(context=context, products=product, chat_id=update.message.from_user.id)
    elif message == "🇬🇧 ENGLISH":
        context.user_data['language'] = message
        product = db.get_all_product_by_eng()
        send_product(context=context, products=product, chat_id=update.message.from_user.id)



def main():
    updater = Updater(token=TOK)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_handlar))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

