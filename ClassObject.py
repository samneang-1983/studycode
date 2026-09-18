from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters


BOT_TOKEN = "8746969042:AAH-5oLV7U7zt8inFCBbDt-02s2s_16rNrQ"

class Country:
    def __init__(self, capital: str, population: str, currency: str, region: str):
        self.capital = capital
        self.population = population
        self.currency = currency
        self.region = region

    def __str__(self):
        return (
            f"🏛 Capital: {self.capital}\n"
            f"👥 Population: {self.population}\n"
            f"🪙 Currency: {self.currency}\n"
            f"📍 Region: {self.region}"
        )


DATA = {
    "cambodia": Country(
        "Phnom Penh",
        "16.9 million",
        "Riel (KHR)",
        "Southeast Asia"
    ),

    "japan": Country(
        "Tokyo",
        "125.1 million",
        "Yen (JPY)",
        "East Asia"
    ),

    "france": Country(
        "Paris",
        "67.7 million",
        "Euro (EUR)",
        "Western Europe"
    ),
}


async def reply_capital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    country = update.message.text.strip().lower()
    info = DATA.get(country)

    if info:
        await update.message.reply_text(str(info))
    else:
        await update.message.reply_text(
            f"❌ '{update.message.text}' doesn't look like a valid country name. "
            "Try again!"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, reply_capital)
)

print("🤖 Bot is running... Open Telegram and send: cambodia")

app.run_polling()
