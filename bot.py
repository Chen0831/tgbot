#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot
import simsimi
import sys
import time

def on_chat_message(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)

    command = msg['text']

    text = simsimi.simsimi(command)
    bot.sendMessage(str(msg['chat']['id']), text)

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)

bot.message_loop({'chat': on_chat_message})
print('Listening ...')

while 1:
    time.sleep(10)
