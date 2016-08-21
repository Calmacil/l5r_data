#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import irclib as irc
import ircbot as bot
import re
from random import randint


config = {
    "host":         "irc.quakenet.org",
    "port":         6667,
    "gmpassword":   "waz2gala",
    "gamechannel":  "#iaijutsu",
    "botuser":      "L5RGm",
    "botnick":      "Kusabana",
    "botpassw":     "aromatherapie",
    "datafile":     "./data.json"
}


class Die(object):
    """ A simple d10 """

    def __init__(self, explodeOn=10, below=0):
        """ Inits the die """
        self.explodeOn = explodeOn

    def roll(self):
        """ Rolls the die """
        total = 0
        current = 0
        alreadyBelowed = False

        while True:
            current = randint(1,10)
            total = total + current

            if current < self.explodeOn and current > self.below and alreadyBelowed:
                break

            if current < self.below:
                alreadyBelowed = True

        return total


class Pool(object):
    """ TODO IMPLEMENT """

    def __init__(self, cmd):
        pattern = re.compile("(\d)k([uem]?)(\d)")
        matches = pattern.search(cmd)


class Py5RBot(bot.SingleServerIRCBot):
    """ Bot IRC destiné à faciliter la gestion de parties de L5R en ligne
    Modele des méthodes: on_event(self, serv/conn, event) """

    def __init__(self, config):
        """ Creates the bot """

        self.host = config['host']
        self.port = config['port']
        self.gmpassword = config['gmpassword']
        self.gamechannel = config['gamechannel']
        self.botuser = config['botuser']
        self.botnick = config['botnick']
        self.botpassw = config['botpassw']
        self.datafile = config['datafile']

        bot.SingleServerIRCBot.__init__(self, [(self.host, self.port)], self.botnick, self.botuser)
        self.start()

    def on_welcome(self, c, e):
        """ Joins the game channel """
        c.join(self.gamechannel)

    def on_privmsg(self, c, e):
        """ Parses privmsgs and launches commands """
        self.doCommand(e, e.arguments()[0])

    def doCommand(self, e, cmd):
        """ Checks commands """
        nick = irc.nm_to_n(e.source())
        t = e.target()
        c = self.connection

        if re.compile('^\d{,2}k[uem]?\d{,2}').search(cmd):   # dice roll
            c.privmsg(self.gamechannel, 'Coucou')

if __name__ == '__main__':
    ircbot = Py5RBot(config)
    print ircbot.host
