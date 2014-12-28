"""
A simple IRC bot which can join a channel and taunt people the channels it is in. It
will simply reply when a target says something in the channel with <nick>: <taunt>!
It can be configured through IRC once it starts up.
"""

import re
import socket
from contextlib import closing

class IRCBot(object):
    """
    Base class for most IRC bots. Fleshed out implementations of IRC bots should
    implement the handle_* methods.
    """

    def __init__(self, server, port, nick="simplebot", use_ssl=False):
        # Set up the connection, connect, and identify with the server before it boots us
        self.connection = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        if use_ssl:
            import ssl
            self.connection = ssl.wrap_socket(self.connection)

        self.connection.connect((server,port))
        self.infile = self.connection.makefile("rb")
        self.channels = []

        self.identify(nick)

    def identify(self, nick):
        "Identifies the IRC bot with the IRC server."
        self.writeline("NICK %s" % nick)
        self.writeline("USER %(nick)s %(nick)s %(nick)s %(nick)s" % {"nick" : nick})

    def say(self, channel, msg):
        "Convenience method for saying something in a given channel."
        self.writeline("PRIVMSG %s :%s" % (channel, msg))

    def add_channel(self, channel):
        "Tells the IRC bot to join the given channel when it starts up."
        self.channels.append(channel)

    def join(self, channel):
        "Issues a JOIN command to the IRC server for the bot for the given channel."
        self.writeline("JOIN %s" % channel)

    def part(self, channel, msg=""):
        "Issues a PART command to the IRC server for the bot for the given channel."
        self.writeline("PART %s %s" % (channel, msg))

    def handle_join(self, user, channel):
        """
        Called when the IRC bot or any other user joins a channel. Subclasses should
        override this method.
        """

    def handle_channel_msg(self, channel, sender, msg):
        """
        Called when someone says something in a channel this bot is in. Subclasses
        should override this method.
        """

    def handle_private_msg(self, sender, msg):
        """
        Called when someone says something directly to this bot. Subclasses should
        override this method.
        """

    def start(self):
        """
        Starts the IRC bot. First it tries to join all channels it was told to. Then, it
        parses all data returned to it from the server. It will automatically PONG on PING
        requests. Any JOIN or PRIVMSG it encounters will be passed along to the
        appropriate handle_* method.
        """

        for channel in self.channels:
            self.join(channel)
        
        with closing(self.connection):
            while True:
                line = self.readline()
                if not line:
                    break

                if line.startswith("PING"):
                    server = line.split()
                    self.writeline("PONG %s" % server)

                elif "JOIN" in line and "PRIVMSG" not in line:
                    m = re.match(":([^!]*).*JOIN :(#\S*)", line)
                    if m is not None:
                        user, channel = m.groups()
                        self.handle_join(user, channel)

                elif "PRIVMSG" in line:
                    m = re.match(":([^!]*).*PRIVMSG (\S*).*?:(.*)", line)
                    if m is not None:
                        sender, channel, msg = m.groups()
                        if channel.startswith("#"):
                            self.handle_channel_msg(channel, sender, msg)
                        else:
                            self.handle_private_msg(sender, msg)

    def writeline(self, msg):
        "Convenience method to write a line to the IRC server."
        self.connection.send(msg + "\r\n")

    def readline(self):
        "Convenience method for getting a line from the IRC server."
        s = self.infile.readline()
        if not s:
            raise EOFError
        if s[-2:] == "\r\n":
            s = s[:-2]
        elif s[-1:] in "\r\n":
            s = s[:-1]
        return s


class TauntBot(IRCBot):
    """
    An IRC bot implementation that joins channels and taunts configured users with a
    certain taunt whenever they say something. Once started, the bot can be configured by
    it's owner through private messages.
    """

    def __init__(self, server, port, owner, taunt="No!", nick="tauntbot", use_ssl=False):
        super(TauntBot, self).__init__(server, port, nick, use_ssl)
        self.owner, self.nick, self.taunt, self.targets = owner, nick, taunt, {}

    def add_channel(self, channel, targets=None):
        "Adds the bot to the given channel, targeting targets if specified."
        super(TauntBot, self).add_channel(channel)
        if targets:
            self.targets[channel] = set(targets)

    def handle_channel_msg(self, channel, sender, msg):
        "When a target says something in a channel, taunt him."
        if sender in self.targets.get(channel, []):
            self.say(channel, "%s: %s" % (sender, self.taunt))

    def handle_join(self, user, channel):
        """
        When the bot joins, it says who it is targeting. If a target joins, it tell them
        to watch out.
        """
        if self.nick == user:
            self.intimidate(channel, self.targets.get(channel, []))
        elif channel in self.targets and user in self.targets.get(channel, []):
            self.intimidate(channel, user)

    def handle_private_msg(self, sender, msg):
        """
        Responds in private messages to it's owner only. Allows the owner to configure the
        bot after it has been started. The available commands are:
            !targets - Lists all the targets in all the channels
            !target <channel> <target>* - Targets each target in the given channel
            !untarget <channel> <target>* - Untargets each target in the given channel
            !join <channel> - Joins the given channel
            !part <channel> - Leaves the given channel
        If anyone other than the owner messages it, it tells then to go away.
        """
        reply = lambda rpl: self.say(sender, rpl)

        if sender == self.owner:
            try:
                if msg == "!targets":
                    for channel in self.targets:
                        reply("Targeting %s in channel %s" % (self.targets[channel],
                                                              channel))
                    else:
                        reply("Not targeting anyone")

                elif msg.startswith("!target"):
                    channel = msg.split()[1]
                    targets = msg.split()[2:]
                    if targets:
                        if channel not in self.targets:
                            self.targets[channel] = set([])
                            self.targets[channel].update(targets)
                            reply("Now targeting %s in %s" % (targets, channel))
                            self.intimidate(channel, targets)

                elif msg.startswith("!join"):
                    channel = msg.split()[1]
                    reply("Now entering %s" % channel)
                    self.join(channel)

                elif msg.startswith("!untarget"):
                    channel = msg.split()[1]
                    targets = msg.split()[2:]
                    if channel in self.targets:
                        self.targets[channel].difference_update(targets)
                        reply("Targets for channel %s are now %s" % (channel,
                                                                     self.targets[channel]))
                        if len(self.targets[channel]) == 0:
                            del self.targets[channel]

                elif msg.startswith("!part"):
                    channel = msg.split()[1]
                    msg = " ".join(msg.split()[2:])
                    reply("Leaving %s" % channel)
                    self.part(channel, msg)
            except:
                reply("Invalid syntax to command. Don't try to break me please.")
        else:
            reply("I don't have to listen to you")

    def intimidate(self, channel, targets):
        "Tells the given target in the given channel to watch out."
        if len(targets) == 0:
            return
        # to_say = "I am coming for you %s!"
        # target_str = " and".join(", ".join(targets).rsplit(",", 1))
        # self.say(channel, to_say % target_str)