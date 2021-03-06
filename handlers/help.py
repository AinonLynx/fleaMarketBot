from handlers.system import silence_keeper


@silence_keeper
def help(bot, update):
    update.message.reply_text(
        '/help - показать это сообщение\n'
        '/list - показать список из названий товаров, которые сейчас продаются\n'
        '/subscribe - подписаться на новые товары\n'
        '/unsubscribe - отписаться от рассылки новых товаров\n'
        '/add - добавить свой товар\n'
        '/edit - отредактировать свой товар\n'
        '/delete - удалить свой товар\n'
        '/support - спросить поддержку'
    )
