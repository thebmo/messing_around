import re

words = ['Fester\'s Quest', 'Fast Break, Magic Johnson\'s', 'Castlevania III: Dracula\'s Curse', 'Golf Power, Greg Norman\'s', 'George Foreman\'s K.O. Boxing','Adventures in The Magic Kingdom, Disney\'s']

reg = ', \w* \w*\'s'
titles = []
print "\nwords\n-----------------------"
for word in words:
    print word


print "\nfound words (%s)\n-----------------------" % reg
for word in words:
    if re.search(reg, word, flags=re.IGNORECASE):
        print word
        titles.append(word)



print "\nfixed titles\n-----------------------"
for title in titles:
    temp = title.split(', ')
    title = ' '.join((temp[1], temp[0]))
    print title