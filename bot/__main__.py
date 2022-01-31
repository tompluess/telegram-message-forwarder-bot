import random
from time import sleep
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, sudo_users
from bot.helper.utils import get_formatted_chat
from bot.helper.message import send_message
from bot.helper.invite_links import get_invite_link

LOG.info("Welcome, this is the telegram-message-forwarder-bot. main routine...")


@app.on_message(filters.chat(from_chats) & filters.incoming & ~filters.reply & ~filters.poll)
def work(client, message):
    if advance_config:
        try:
            for chat in chats_data[message.chat.id]:
                forward_message(message, chat, app)
        except Exception as e:
            LOG.error(e)
    else:
        try:
            for chat in to_chats:
                forward_message(message, chat, app)
        except Exception as e:
            LOG.error(e)


def forward_message(message, target_chat_id, app):
    invite_link = get_invite_link(message.chat.id, app)
    send_message(message, target_chat_id,  app, invite_link=invite_link)

@ app.on_message(filters.user(sudo_users) & filters.command(["fwd", "forward"]), group=1)
def forward(app, message):
    if len(message.command) > 1:
        chat_id = get_formatted_chat(message.command[1], app)
        if chat_id:
            try:
                offset_id = 0
                limit = 0
                if len(message.command) > 2:
                    limit = int(message.command[2])
                if len(message.command) > 3:
                    offset_id = int(message.command[3])
                for msg in app.iter_history(chat_id, limit=limit, offset_id=offset_id):
                    msg.copy(message.chat.id)
                    sleep(random.randint(1, 10))
            except Exception as e:
                message.reply_text(f"```{e}```")
        else:
            reply = message.reply_text(
                "```Invalid Chat Identifier. Give me a chat id, username or message link.```")
            sleep(5)
            reply.delete()
    else:
        reply = message.reply_text(
            "```Invalid Command ! Use /fwd {ChatID} {limit} {FirstMessageID}```")
        sleep(20)
        reply.delete()


app.run()
