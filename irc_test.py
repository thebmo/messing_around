import mendel_bot

server = 'irc.wherestheparty.at'
port = 6697
nick = 'ShutUp'
use_ssl = True
owner = 'BMO'
taunt = 'Shut up'

channels = ['#wtpa']
targets = ['FredBot']

bot = mendel_bot.TauntBot(server, port, owner, taunt, nick, use_ssl)

for channel in channels:
    bot.add_channel(channel, targets)
bot.start()