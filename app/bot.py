import os
import time
from dotenv import load_dotenv
import telebot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


    
@bot.message_handler(commands=['start'])
def send_welc(msg):

    bot.send_photo(chat_id=msg.chat.id,photo=open("./app/photo/cover.png","rb"))
    
    # challenge 1
    reply_chall1 = telebot.types.InlineKeyboardMarkup(
        [
            [telebot.types.InlineKeyboardButton(text="Let's Go!",callback_data="dance_quiz")]
        ]
    )

    bot.send_message(chat_id=msg.chat.id,text="Hi Charmaine, welcome to your 24th B'Day escape room...\nWhat will be the surprise waiting for you? \U0001F608")
    chall1 = bot.send_message(chat_id=msg.chat.id,text="Since you love ZB1 so much... \nWhy not show us your love for them? \nhttps://youtube.com/clip/UgkxNVxAyxgVKZNG30IejFedojg2h8gedwOg?si=MZNku24XEtEewllq \nFrom 00:07 to 00:12",
        reply_markup=reply_chall1
    )
    

    
@bot.callback_query_handler(lambda query: query.data == "dance_quiz")
def dance_quiz(query):
    forfeit1_text = "Forfeit time!\nDo this to exchange for clue!\n<placeholder text>"
    forfeit1 = telebot.types.MessageEntity(type="bold",offset=0,length=len(forfeit1_text))
    dance_quiz = bot.send_poll(
        chat_id=query.message.chat.id,
        question="Guess the vowel key to the treasue:",
        options=[
            telebot.types.InputPollOption("A"),
            telebot.types.InputPollOption("I"),
            telebot.types.InputPollOption("U")
        ],
        type="quiz",
        allows_multiple_answers=False,
        correct_option_id=1,
        is_anonymous=False,
        open_period=60,
        explanation=forfeit1_text,
        explanation_entities=[forfeit1],
    )
    
    time.sleep(25)

    # challenge 2
    reply_chall2 = telebot.types.InlineKeyboardMarkup(
        [
            [telebot.types.InlineKeyboardButton(text="Start!",callback_data="image_quiz")]
        ]
    )

    chall2 = bot.send_message(chat_id=query.message.chat.id, text="\U0001F624Just a dance is not enough to show how much you love them \nYou have to prove your love by recognising... \n their BODY!!!",
        reply_markup=reply_chall2
    )

@bot.callback_query_handler(lambda query: query.data == "image_quiz")
def image_quiz(query):
    forfeit2_text = "Forfeit time!\nDo this to exchange for clue!\n<placeholder text>"
    forfeit2 = telebot.types.MessageEntity(type="bold",offset=0,length=len(forfeit2_text))

    # candidate 1
    image1 = bot.send_photo(chat_id=query.message.chat.id,photo=open("./app/photo/gyuvin.jpg","rb"),caption="This is our candidate 1")
    image1_quiz = bot.send_poll(
        chat_id=query.message.chat.id,
        question="Guess whose this is:",
        options=[
            telebot.types.InputPollOption("Zhang Hao"),
            telebot.types.InputPollOption("Ricky"),
            telebot.types.InputPollOption("Gyuvin"),
            telebot.types.InputPollOption("Taerae"),
            telebot.types.InputPollOption("Han bin"),
            telebot.types.InputPollOption("Matthew"),
            telebot.types.InputPollOption("Yu jin"),
            telebot.types.InputPollOption("Gunwook"),
            telebot.types.InputPollOption("Jiwoong")
        ],
        type="quiz",
        allows_multiple_answers=False,
        correct_option_id=2,
        is_anonymous=False,
        open_period=60,
        explanation=forfeit2_text,
        explanation_entities=[forfeit2],
        
    )

    # candidate 2
    image2 = bot.send_photo(chat_id=query.message.chat.id,photo=open("./app/photo/zhanghao.jpg","rb"),caption="This is our candidate 2")
    image2_quiz = bot.send_poll(
        chat_id=query.message.chat.id,
        question="Guess whose this is:",
        options=[
            telebot.types.InputPollOption("Zhang Hao"),
            telebot.types.InputPollOption("Ricky"),
            telebot.types.InputPollOption("Gyuvin"),
            telebot.types.InputPollOption("Taerae"),
            telebot.types.InputPollOption("Han bin"),
            telebot.types.InputPollOption("Matthew"),
            telebot.types.InputPollOption("Yu jin"),
            telebot.types.InputPollOption("Gunwook"),
            telebot.types.InputPollOption("Jiwoong")
        ],
        type="quiz",
        allows_multiple_answers=False,
        correct_option_id=0,
        is_anonymous=False,
        open_period=60,
        explanation=forfeit2_text,
        explanation_entities=[forfeit2],
        
    )

    # candidate 3
    image3 = bot.send_photo(chat_id=query.message.chat.id,photo=open("./app/photo/hanbin.jpg","rb"),caption="This is our candidate 3")
    image3_quiz = bot.send_poll(
        chat_id=query.message.chat.id,
        question="Guess whose this is:",
        options=[
            telebot.types.InputPollOption("Zhang Hao"),
            telebot.types.InputPollOption("Ricky"),
            telebot.types.InputPollOption("Gyuvin"),
            telebot.types.InputPollOption("Taerae"),
            telebot.types.InputPollOption("Han bin"),
            telebot.types.InputPollOption("Matthew"),
            telebot.types.InputPollOption("Yu jin"),
            telebot.types.InputPollOption("Gunwook"),
            telebot.types.InputPollOption("Jiwoong")
        ],
        type="quiz",
        allows_multiple_answers=False,
        correct_option_id=4,
        is_anonymous=False,
        open_period=60,
        explanation=forfeit2_text,
        explanation_entities=[forfeit2],
        
    )

    # clue: challenge 2
    bot.send_message(chat_id=query.message.chat.id, text="Here's your clue for challenge 2~ \nGuess the consonant key: \nThey are all 남성/남자.")

    time.sleep(60)

    # challenge 3
    forfeit3_text = "Forfeit time!\nHOW COULD YOU \nYou got no clue for this round!"
    forfeit3 = telebot.types.MessageEntity(type="bold",offset=0,length=len(forfeit3_text))

    bot.send_message(chat_id=query.message.chat.id,text="You're at the last step before treasure location reveal... \nHere comes your last clue!")
    image3_quiz = bot.send_poll(
        chat_id=query.message.chat.id,
        question="Who's more important:",
        options=[
            telebot.types.InputPollOption("Us"),
            telebot.types.InputPollOption("Sung Hanbin")
        ],
        type="quiz",
        allows_multiple_answers=False,
        correct_option_id=0,
        is_anonymous=False,
        open_period=3,
        explanation=forfeit3_text,
        explanation_entities=[forfeit3],
        
    )

    time.sleep(3)
    bot.send_message(chat_id=query.message.chat.id,text="Time to guess who your treasure is with~")



if __name__ == "__main__":
    bot.infinity_polling()
