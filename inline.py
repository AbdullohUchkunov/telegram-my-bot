from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from database import Database
from commons import *
from kurs_dollar import list_1
num_1 = list_1[-1]
number = 998_97_709_00_04
number_2 = 998_90_300_09_04
admin = "@pantera0904"
db = Database("pantera.db")

def inline_handler(update,context):
    query = update.callback_query
    data_sp = str(query.data).split("_")
    if data_sp[0] == "product":
        if data_sp[1] == "uz":
            context.user_data['data'] = int(data_sp[2])
            product = db.get_all_main_2_uz(int(data_sp[2]))
            send_main_2(context=context, product_type=product, chat_id=query.message.chat_id,
                         message_id=query.message.message_id)
        elif data_sp[1] == "ru":
            context.user_data['data'] = int(data_sp[2])
            product = db.get_all_main_2_ru(int(data_sp[2]))
            send_main_2(context=context, product_type=product, chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
        elif data_sp[1] == "eng":
            context.user_data['data'] = int(data_sp[2])
            product = db.get_all_main_2_eng(int(data_sp[2]))
            send_main_2(context=context, product_type=product, chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
        elif data_sp[1] == "back":
            if context.user_data['language'] == "🇺🇿 UZBEK":
                product = db.get_all_product_by_uz()
                send_product(context=context, products=product, chat_id=query.message.chat_id,
                             message_id=query.message.message_id)
            elif context.user_data['language'] == "🇷🇺 РУССКИЙ":
                product = db.get_all_product_by_rus()
                send_product(context=context, products=product, chat_id=query.message.chat_id,
                             message_id=query.message.message_id)
            elif context.user_data['language'] == "🇬🇧 ENGLISH":
                product = db.get_all_product_by_eng()
                send_product(context=context, products=product, chat_id=query.message.chat_id,
                             message_id=query.message.message_id)
        elif data_sp[1] == "main":
            if data_sp[2] == "uz":
                main_3 = db.get_all_main_3(str(data_sp[3]))
                context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
                for main in main_3:
                    query.message.reply_photo(photo=open(f"{main['photo']}","rb"),
                                              caption=f"🖌<b>Mahsulot nomi</b>: {main['name']}\n♾<i>Razmer </i>: {main['size_1']} x {main['size_2']} x {main['size_3']} x {main['size_4']}\n💰<i>Narxi</i>: {main['price']} $|  {int(main['price'])*num_1} sum\n📞<i>Tel</i>: +{number_2}     ✅<a>Admin </a>: {admin}",parse_mode="HTML")
                buttons = [[InlineKeyboardButton(text="Orqaga",callback_data="product_backs")]]
                query.message.reply_text(text="Orqaga bosing",reply_markup=InlineKeyboardMarkup(buttons))
            elif data_sp[2] == "ru":
                main_3 = db.get_all_main_3(str(data_sp[3]))
                context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
                for main in main_3:
                    query.message.reply_photo(photo=open(f"{main['photo']}","rb"),
                                             caption=f"🖌<b>Наименование товара</b>: {main['name']}\n♾<i>Размер </i>: {main['size_1']} x {main['size_2']} x {main['size_3']} x {main['size_4']}\n💰<i>Цена</i>: {main['price']} $|  {int(main['price'])*num_1} sum\n📞<i>Тел</i>: +{number_2}     ✅<a>Админ </a>: {admin}",parse_mode="HTML")
                buttons = [[InlineKeyboardButton(text="Назад", callback_data="product_backs")]]
                query.message.reply_text(text="Нажмите назад", reply_markup=InlineKeyboardMarkup(buttons))
            elif data_sp[2] == "eng":
                main_3 = db.get_all_main_3(str(data_sp[3]))
                context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
                for main in main_3:
                    query.message.reply_photo(photo=open(f"{main['photo']}","rb"),
                                              caption=f"🖌<b>Name of product</b>: {main['name']}\n♾<i>Size </i>: {main['size_1']} x {main['size_2']} x {main['size_3']} x {main['size_4']}\n💰<i>Price</i>: {main['price']} $|  {int(main['price'])*num_1} sum\n📞<i>Tel</i>: +{number_2}     ✅<a>Admin </a>: {admin}",parse_mode="HTML")
                buttons = [[InlineKeyboardButton(text="Back", callback_data="product_backs")]]
                query.message.reply_text(text="Press back", reply_markup=InlineKeyboardMarkup(buttons))
        elif data_sp[1] == "backs":
            if context.user_data['language'] == "🇺🇿 UZBEK":
                product = db.get_all_main_2_uz(context.user_data['data'])
                send_main_2(context=context, product_type=product, chat_id=query.message.chat_id,
                            message_id=query.message.message_id)
            elif context.user_data['language'] == "🇷🇺 РУССКИЙ":
                product = db.get_all_main_2_ru(context.user_data['data'])
                send_main_2(context=context, product_type=product, chat_id=query.message.chat_id,
                            message_id=query.message.message_id)
            elif context.user_data['language'] == "🇬🇧 ENGLISH":
                product = db.get_all_main_2_eng(context.user_data['data'])
                send_main_2(context=context, product_type=product, chat_id=query.message.chat_id,
                            message_id=query.message.message_id)





    elif query.data == "close":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)













            # else:
            #     data = db.get_furnitura(str(data_sp[2]))
            #     context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            #     for furniture in data:
            #         query.message.reply_photo(
            #             photo= open(f"{furniture['image']}","rb"),
            #             caption=f"🖌<b>Nomi</b>: {furniture['furniture_names']}\n"
            #                     f"♾<i>Razmer </i>: {furniture['furniture_uzunlik_1']} x {furniture['furniture_uzunlik_2']} x {furniture['furniture_balandligi']} x {furniture['furniture_eni']}\n"
            #                     f"💰<i>Narxi</i>: {furniture['price']} $ ({furniture['price']*num_1} sum)\n"
            #                     f"📞<i>Tel</i>:  +{number_2}, +{number} \n"
            #                     f"✅<a>Admin </a>: {admin} ",
            #             parse_mode="HTML"
            #         )

    #     else:
    #         product_type = db.get_type_by_product(int(data_sp[1]))
    #         send_mahsulot_tur(context=context, product_type=product_type, chat_id=query.message.chat_id,
    #                           message_id=query.message.message_id)
    #

        # main_menu(context=context, chat_id=query.message.chat_id)