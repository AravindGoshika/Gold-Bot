import telebot, random, time, threading, os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
users = set()

def get_gold_signal():
    side = random.choice(["BUY", "SELL"])
    price = random.randint(2670, 2690)
    sl = price-10 if side=="BUY" else price+10
    tp1 = price+10 if side=="BUY" else price-10
    tp2 = price+20 if side=="BUY" else price-20
    return f"🔥 GOLD SIGNAL 🔥\n\n📊 {side} GOLD @ {price}\n⛔ SL: {sl}\n🎯 TP1: {tp1}\n🎯 TP2: {tp2}"

@bot.message_handler(commands=['start'])
def start(m):
    users.add(m.chat.id)
    bot.reply_to(m, "Bot LIVE! Auto signal every 1 hour ON! Use /signal")

@bot.message_handler(commands=['signal'])
def sig(m):
    bot.send_message(m.chat.id, get_gold_signal())

def auto_sender():
    while True:
        time.sleep(3600)
        for uid in list(users):
            try: bot.send_message(uid, get_gold_signal())
            except: pass

threading.Thread(target=auto_sender, daemon=True).start()
bot.infinity_polling()
