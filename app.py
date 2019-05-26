TOKEN = "<TELEGRAM_BOT_TOKEN>"
from balautil import requestutil
API_KEY = "<API_KEY_FOR_MIN_API>"

# SETP 1: INSTALL A PACKAGE CALLED botogram


# SETP 2: Get simple boilerplate code for bot
import botogram
bot = botogram.create( TOKEN )


def load_symbols():
    base_url_syml_mapping = f"https://min-api.cryptocompare.com/data/pair/mapping/fsym?fsym=BTC&api_key={API_KEY}"
    resp = requestutil.Get(base_url_syml_mapping)
    symbols = ["BTC"] + list(set([ item["tsym"] for item in resp.get("Data")]))
    return symbols

def get_price(symbols, from_sym="BTC", to_sym="USD"):

    if from_sym not in symbols or to_sym not in symbols:
        return "Please check your inputs for from and to symbol"
    
    r =requestutil.Get(f"https://min-api.cryptocompare.com/data/price?fsym={from_sym}&tsyms={to_sym}")
    return r

SYMBOLS = load_symbols()

@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("Hello world")

@bot.command("getprice")
def getprice_command(chat, message, args):
    """I will get the price ofl = args[0]
    to_symbol = args[1]
 any crypto currency"""


    if len(args) < 2:
        chat.send("Usage: /getprice <FROM SYMBOL> <TO SYMBOL>")
        chat.send("Usage: /getprice SGD USD")
        return

    from_symbol = args[0]
    to_symbol = args[1]

    result = get_price(SYMBOLS, from_symbol, to_symbol)    

    chat.send(f" {from_symbol} is {result}")

if __name__ == "__main__":
    bot.run()

# STEP 3: Start the bot
