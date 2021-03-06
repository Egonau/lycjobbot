import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler, Filters)
import jobdata
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
CREATION_BEFORE_NAME, NAME, PAY, INFO_ABOUT_VACANCY, DEADLINE, CREATE = range(6)
# Callback data
ZERO, ONE, TWO, FIND_JOB, THREE, CONTENT, COMPUTER_HELP, PROGRAMMING, HELP_HOMEWORK, VOLUNTEER, MARKETING, \
LANGUAGES, SERVING, F_CONTENT, ACCEPT, F_COMPUTER_HELP, F_PROGRAMMING, F_HELP_HOMEWORK, F_VOLUNTEER, F_MARKETING, \
F_LANGUAGES, F_SERVING, VACANCIES, NAME, PAY_CARD, PAY_CASH, WITHOUT_MONEY = \
    range(27)
INFO_ABOUT_CLIENT = {}
ALREADY_WATCHED = []
NEEDED = []
CHOSEN_VACANCY = None

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("Создать/изменить вакансию", callback_data=str(ONE)),
            InlineKeyboardButton("Найти вакансию", callback_data=str(FIND_JOB)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Что вы хотите сделать?", reply_markup=reply_markup)
    return CREATION_BEFORE_NAME


def zero(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Создать/изменить вакансию", callback_data=str(ONE)),
            InlineKeyboardButton("Найти вакансию", callback_data=str(FIND_JOB)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text="Что вы хотите сделать?", reply_markup=reply_markup)
    return CREATION_BEFORE_NAME


def one(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Создать новую", callback_data=str(TWO)),
            InlineKeyboardButton("Изменить существующую", callback_data=str(THREE)),
            InlineKeyboardButton("Назад", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Что именно вы хотите сделать?", reply_markup=reply_markup
    )
    return CREATION_BEFORE_NAME


def find_job(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    NEEDED.clear()
    ALREADY_WATCHED.clear()

    keyboard = [
        [
            InlineKeyboardButton("Создание контента", callback_data=str(F_CONTENT)),
            InlineKeyboardButton("Компьютерная помощь", callback_data=str(F_COMPUTER_HELP)),
        ], [
            InlineKeyboardButton("Программирование", callback_data=str(F_PROGRAMMING)),
            InlineKeyboardButton("Уроки(помощь)", callback_data=str(F_HELP_HOMEWORK))], [
            InlineKeyboardButton("Волонтерская помощь", callback_data=str(F_VOLUNTEER)),
            InlineKeyboardButton("Маркетинг", callback_data=str(F_MARKETING))], [
            InlineKeyboardButton("Языки", callback_data=str(F_LANGUAGES)),
            InlineKeyboardButton("Обслуживание", callback_data=str(F_SERVING))], [
            InlineKeyboardButton("Назад", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Выберите тип вакансии", reply_markup=reply_markup
    )


def two(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("Создание контента", callback_data=str(CONTENT)),
            InlineKeyboardButton("Компьютерная помощь", callback_data=str(COMPUTER_HELP)),
        ], [
            InlineKeyboardButton("Программирование", callback_data=str(PROGRAMMING)),
            InlineKeyboardButton("Уроки(помощь)", callback_data=str(HELP_HOMEWORK))], [
            InlineKeyboardButton("Волонтерская помощь", callback_data=str(VOLUNTEER)),
            InlineKeyboardButton("Маркетинг", callback_data=str(MARKETING))], [
            InlineKeyboardButton("Языки", callback_data=str(LANGUAGES)),
            InlineKeyboardButton("Обслуживание", callback_data=str(SERVING))], [
            InlineKeyboardButton("Назад", callback_data=str(ONE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Выберите тип вакансии", reply_markup=reply_markup
    )
    return CREATION_BEFORE_NAME


def content(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Создание контента"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def computer_help(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Компьютерная помощь"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def programming(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Программирование"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def help_homework(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Уроки(помощь)"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def volunteer(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Волонтерская помощь"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def marketing(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Маркетинг"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def languages(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Языки"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def serving(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["type_of_work"] = "Обслуживание"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Введите название вакансии"
    )
    return NAME


def name(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["user_id"] = update.message.chat.username
    text = update.message.text
    INFO_ABOUT_CLIENT["name_of_vacancy"] = text
    # далее заносится в базу данных
    keyboard = [
        [
            InlineKeyboardButton("Наличными при встрече", callback_data=str(PAY_CARD))], [
            InlineKeyboardButton("Оплата картой", callback_data=str(PAY_CASH))], [
            InlineKeyboardButton("Безвозмездная работа", callback_data=str(WITHOUT_MONEY))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        text="Введите тип оплаты", reply_markup=reply_markup
    )
    return PAY


# PAY_CARD, PAY_CASH, WITHOUT_MONEY
def pay_card(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["payment"] = "Оплата картой"
    query = update.callback_query
    query.answer()
    query.message.reply_text(
        text="Введите описание вакансии"
    )
    return INFO_ABOUT_VACANCY


def pay_cash(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["payment"] = "Наличными при встрече"
    query = update.callback_query
    query.answer()
    query.message.reply_text(
        text="Введите описание вакансии"
    )
    return INFO_ABOUT_VACANCY


def without_money(update: Update, context: CallbackContext) -> None:
    INFO_ABOUT_CLIENT["payment"] = "Безвозмездная работа"
    query = update.callback_query
    query.answer()
    query.message.reply_text(
        text="Введите описание вакансии"
    )
    return INFO_ABOUT_VACANCY


def info_about_vacancy(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    INFO_ABOUT_CLIENT["about_vacancy"] = text
    update.message.reply_text(
        text="Укажите срок выполнения работы"
    )
    return DEADLINE


def deadline(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    INFO_ABOUT_CLIENT["deadline"] = text
    # INFO_ABOUT_CLIENT["_id"] = jobdata.collection.find().count() + 1
    keyboard = [
        [
            InlineKeyboardButton("Создать", callback_data=str(CREATE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        text="Название: {} \nТип: {} \nОписание: {} \nОплата: {} \nСрок: {}".format(
            INFO_ABOUT_CLIENT["name_of_vacancy"], INFO_ABOUT_CLIENT["type_of_work"], INFO_ABOUT_CLIENT["about_vacancy"],
            INFO_ABOUT_CLIENT["payment"], INFO_ABOUT_CLIENT["deadline"]), reply_markup=reply_markup
    )

    return CREATE


def create(update: Update, context: CallbackContext) -> None:
    jobdata.collection.insert_one(INFO_ABOUT_CLIENT)
    query = update.callback_query
    query.answer()
    query.message.reply_text(
        text="Вакансия успешно создана."
    )
    return ConversationHandler.END


def accept(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Назад", callback_data=F_CONTENT)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.message.reply_text(text="Ник: {}".format(
        CHOSEN_VACANCY["user_id"]
    ), reply_markup=reply_markup)

    return CREATION_BEFORE_NAME


def f_content(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Следующая", callback_data=str(F_CONTENT)),
        ],
        [
            InlineKeyboardButton("Выбрать", callback_data=str(ACCEPT))
        ],
        [
            InlineKeyboardButton("Выбрать другой тип", callback_data=str(FIND_JOB))
        ]

    ]
    keyboard2 = [
        [
            InlineKeyboardButton("Выбрать другой тип", callback_data=str(FIND_JOB))
        ]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_markup2 = InlineKeyboardMarkup(keyboard2)
    vacancies = jobdata.collection.find()
    for i in vacancies:
        if i["type_of_work"] == "Создание контента":
            NEEDED.append(i)
    for i in NEEDED:
        if i not in ALREADY_WATCHED:
            ALREADY_WATCHED.append(i)
            CHOSEN_VACANCY = i
            query.message.reply_text(text="Название: {} \nТип: {} \nОписание: {} \nОплата: {} \nСрок: {}".format(
                i["name_of_vacancy"], i["type_of_work"],
                i["about_vacancy"],
                i["payment"], i["deadline"]), reply_markup=reply_markup)
        elif ALREADY_WATCHED == NEEDED:
            NEEDED.clear()
            ALREADY_WATCHED.clear()
            query.message.reply_text(text="Вы всё просмотрели", reply_markup=reply_markup2)
    return CREATION_BEFORE_NAME


def f_computer_help(update: Update, context: CallbackContext) -> None:
    WANTED_VACANCY = "Компьютерная помощь"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ща поищем"
    )
    return VACANCIES


def f_programming(update: Update, context: CallbackContext) -> None:
    WANTED_VACANCY = "Программирование"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ща поищем"
    )
    return VACANCIES


def f_help_homework(update: Update, context: CallbackContext) -> None:
    WANTED_VACANCY = "Уроки(помощь)"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ща поищем"
    )
    return VACANCIES


def f_volunteer(update: Update, context: CallbackContext) -> None:
    WANTED_VACANCY = "Волонтерская помощь"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ща поищем"
    )
    return VACANCIES


def f_marketing(update: Update, context: CallbackContext) -> None:
    WANTED_VACANCY = "Маркетинг"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ща поищем"
    )
    return VACANCIES


def f_languages(update: Update, context: CallbackContext) -> None:
    WANTED_VACANCY = "Языки"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ща поищем"
    )
    return VACANCIES


def f_serving(update: Update, context: CallbackContext) -> None:
    WANTED_VACANCY = "Обслуживание"
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Ща поищем"
    )
    return VACANCIES

    # def vacancies(update: Update, context: CallbackContext) -> None:
    # print(jobdata.collection)


def main():
    updater = Updater("1617510398:AAG4zbRLKarnb9tvW_0clME-n97riE7-Y_g")

    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CREATION_BEFORE_NAME: [
                CallbackQueryHandler(zero, pattern='^' + str(ZERO) + '$'),
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(find_job, pattern='^' + str(FIND_JOB) + '$'),
                CallbackQueryHandler(content, pattern='^' + str(CONTENT) + '$'),
                CallbackQueryHandler(computer_help, pattern='^' + str(COMPUTER_HELP) + '$'),
                CallbackQueryHandler(programming, pattern='^' + str(PROGRAMMING) + '$'),
                CallbackQueryHandler(help_homework, pattern='^' + str(HELP_HOMEWORK) + '$'),
                CallbackQueryHandler(volunteer, pattern='^' + str(VOLUNTEER) + '$'),
                CallbackQueryHandler(languages, pattern='^' + str(LANGUAGES) + '$'),
                CallbackQueryHandler(serving, pattern='^' + str(SERVING) + '$'),
                CallbackQueryHandler(marketing, pattern='^' + str(MARKETING) + '$'),
                CallbackQueryHandler(accept, pattern='^' + str(ACCEPT) + '$'),
                CallbackQueryHandler(f_content, pattern='^' + str(F_CONTENT) + '$'),
                CallbackQueryHandler(f_computer_help, pattern='^' + str(F_COMPUTER_HELP) + '$'),
                CallbackQueryHandler(f_programming, pattern='^' + str(F_PROGRAMMING) + '$'),
                CallbackQueryHandler(f_help_homework, pattern='^' + str(F_HELP_HOMEWORK) + '$'),
                CallbackQueryHandler(f_volunteer, pattern='^' + str(F_VOLUNTEER) + '$'),
                CallbackQueryHandler(f_languages, pattern='^' + str(F_LANGUAGES) + '$'),
                CallbackQueryHandler(f_serving, pattern='^' + str(F_SERVING) + '$'),
                CallbackQueryHandler(f_marketing, pattern='^' + str(F_MARKETING) + '$'),
            ],
            NAME: [
                CommandHandler('start', start), MessageHandler(Filters.text, name)
            ],

            PAY: [CallbackQueryHandler(pay_card, pattern='^' + str(PAY_CARD) + '$'),
                  CallbackQueryHandler(pay_cash, pattern='^' + str(PAY_CASH) + '$'),
                  CallbackQueryHandler(without_money, pattern='^' + str(WITHOUT_MONEY) + '$'),
                  ],
            INFO_ABOUT_VACANCY: [CommandHandler('start', start), MessageHandler(Filters.text, info_about_vacancy)],
            DEADLINE: [CommandHandler('start', start), MessageHandler(Filters.text, deadline)],
            CREATE: [CallbackQueryHandler(create, pattern='^' + str(CREATE) + '$')]
        },
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
