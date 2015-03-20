def notify():
    print 'Reactor loop initiated!'
    print 'Please continue to wait.'


from twisted.internet import reactor

reactor.callWhenRunning(notify)

print 'Here we go!'

reactor.run()
