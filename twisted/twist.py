class Countdown(object):
    def __init__(self, name, counter=5, delay=1):
        self.name = name
        self.counter = counter
        self.delay = delay
    
    def count(self):
        if self.counter == 0:
            print self.name, ': FINSIHED'
        else:
            print self.name, ':', self.counter, '...'
            self.counter -= 1
            reactor.callLater(self.delay, self.count)


from twisted.internet import reactor
reactor.callWhenRunning(Countdown('1', counter=10, delay=1).count)
reactor.callWhenRunning(Countdown('2', counter=5, delay=2).count)
reactor.callWhenRunning(Countdown('3', counter=7, delay=1.5).count)
reactor.run()
