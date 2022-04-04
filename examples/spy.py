import cnbc

STOCK = "SPY"

client = cnbc.Client()
client.apply(STOCK, client.queryQuote, cnbc.Client.save)