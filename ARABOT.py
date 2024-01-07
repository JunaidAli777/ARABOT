import pandas as pd
from typing import Final
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
import os

my_variable = os.environ.get("TOKEN")
BOT_USERANME: Final = '@arabdict1_bot'


#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi, I am ARABOT')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am an arabic language dictionary bot, give me a word in english and I can translate it into arabic and vice versa')


#handling data
def handling_data(file_path):
    data = pd.read_excel(file_path)
    custom_data_dict = {}
    #custom_data_dict = {row[0]: list(row[1:]) for row in data.itertuples(index=False)}
    for row in data.itertuples(index=False):
        word = row[0]
        meanings = list(row[1:])
        if word not in custom_data_dict:
            custom_data_dict[word] = meanings
        else:
            custom_data_dict[word].extend(meanings) 
    return custom_data_dict



#handling messages
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    if isinstance(user_text, str) and user_text.isascii():
        file_path = '/home/qaiser-server/Documents/modified_eng-ar.xlsx'
        custom_data_dict = handling_data(file_path)
        user_text = user_text.lower()
        if user_text in custom_data_dict:
            bot_response = ', '.join(custom_data_dict[user_text])
            await update.message.reply_text(f'The meaning(s) of the word, {user_text} is/are {bot_response}')
                
        else:
            if '-' in user_text or ' ' in user_text:
                await update.message.reply_text(f'For the time being I can respond to only one word per text')
            else:    
                await update.message.reply_text(f'This word does not exist in the dictionary')
        
    elif isinstance(user_text, str) and not user_text.isascii():
        file_path = '/home/qaiser-server/Documents/modified_ar-eng.xlsx'
        custom_data_dict = handling_data(file_path)
        
        if user_text in custom_data_dict:
            bot_response = ', '.join(custom_data_dict[user_text])
            await update.message.reply_text(f'The meaning(s) of the word, {user_text} is/are {bot_response}')
        else:
            if '-' in user_text or ' ' in user_text:
                await update.message.reply_text(f'For the time being I can respond to only one word per text')
            else:
                await update.message.reply_text(f'This word does not exist in the dictionary')



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")



if __name__ == '__main__':
    

    #starting the bot
    print('starting the bot...')
    app = Application.builder().token(TOKEN).build()
    

    #handling commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    #handling Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_messages))


    #error
    app.add_error_handler(error)

    #polling the bot
    print('polling...')
    app.run_polling(poll_interval=3)