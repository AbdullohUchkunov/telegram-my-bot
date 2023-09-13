from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup



def send_product(context,products,chat_id,message_id = None):
    if context.user_data['language'] == "🇺🇿 UZBEK":
        buttons = []
        for product in products:
            buttons.append(
                [
                    InlineKeyboardButton(text=f"{product['name_uz']}", callback_data=f"product_uz_{product['id']}")
                ]
            )
        buttons.append([InlineKeyboardButton(text="Yopish", callback_data="close")])
        if message_id:
            context.bot.edit_message_text(chat_id=chat_id,
                                          message_id=message_id,
                                          text="<b>Mebellar turi</b>",
                                          reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        else:
            context.bot.send_message(chat_id=chat_id,
                                     text="<b>Mebellar turi</b>",
                                     reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
    elif context.user_data['language'] == "🇷🇺 РУССКИЙ":
        buttons = []
        for product in products:
            buttons.append(
                [
                    InlineKeyboardButton(text=f"{product['name_ru']}", callback_data=f"product_ru_{product['id']}")
                ]
            )
        buttons.append([InlineKeyboardButton(text="Закрывать", callback_data="close")])

        if message_id:
            context.bot.edit_message_text(chat_id=chat_id,
                                          message_id=message_id,
                                          text="<b>Тип мебели</b>",
                                          reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        else:
            context.bot.send_message(chat_id=chat_id,
                                     text="<b>Тип мебели</b>",
                                     reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
    elif context.user_data['language'] == "🇬🇧 ENGLISH":
        buttons = []
        for product in products:
            buttons.append(
                [
                    InlineKeyboardButton(text=f"{product['name_eng']}", callback_data=f"product_eng_{product['id']}")
                ]
            )
        buttons.append([InlineKeyboardButton(text="Close", callback_data="close")])
        if message_id:
            context.bot.edit_message_text(chat_id=chat_id,
                                          message_id=message_id,
                                          text="<b>Type of furniture</b>",
                                          reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        else:
            context.bot.send_message(chat_id=chat_id,
                                     text="<b>Type of furniture</b>",
                                     reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")


def send_main_2(context, product_type, chat_id, message_id=None):
    if context.user_data['language'] == "🇺🇿 UZBEK":
        buttons = []
        for product in product_type:
            buttons.append(
                [
                    InlineKeyboardButton(text=f"{product['type_uz']}",
                                         callback_data=f"product_main_uz_{product['type_id']}")
                ]
            )
        buttons.append([InlineKeyboardButton(text="orqaga", callback_data="product_back")])
        if message_id:
            context.bot.edit_message_text(chat_id=chat_id,
                                          message_id=message_id,
                                          text="<b>Mebel turini tanlang:</b>",
                                          reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        else:
            context.bot.send_message(chat_id=chat_id,
                                     text="<b>Mebel turini tanlang:</b>",
                                     reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
    elif context.user_data['language'] == "🇷🇺 РУССКИЙ":
        buttons = []
        for product in product_type:
            buttons.append(
                [
                    InlineKeyboardButton(text=f"{product['type_ru']}",
                                         callback_data=f"product_main_ru_{product['type_id']}")
                ]
            )
        buttons.append([InlineKeyboardButton(text="назад", callback_data="product_back")])
        if message_id:
            context.bot.edit_message_text(chat_id=chat_id,
                                          message_id=message_id,
                                          text="<b>Выбрать тип мебели:</b>",
                                          reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        else:
            context.bot.send_message(chat_id=chat_id,
                                     text="<b>Выбрать тип мебели:</b>",
                                     reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
    elif context.user_data['language'] == "🇬🇧 ENGLISH":
        buttons = []
        for product in product_type:
            buttons.append(
                [
                    InlineKeyboardButton(text=f"{product['type_eng']}",
                                         callback_data=f"product_main_eng_{product['type_id']}")
                ]
            )
        buttons.append([InlineKeyboardButton(text="back", callback_data="product_back")])
        if message_id:
            context.bot.edit_message_text(chat_id=chat_id,
                                          message_id=message_id,
                                          text="<b>Choose the type of furniture:</b>",
                                          reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        else:
            context.bot.send_message(chat_id=chat_id,
                                     text="<b>Choose the type of furniture:</b>",
                                     reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")















