# Bad News Baseball|1990|Tecmo|United States|NTSC|Licensed|Sports
# Title[0]|year[1]|publisher[2]|region[3]|format[4]|license[5]|genre[6]

file = 'C:\\Users\\bmo\\Desktop\\nes_parsed.txt'
with open(file, 'r') as f:
    for line in f.readlines():
        game = line.replace('\n', '').split('|')
    
        g = Game(title=game[0], year=game[1],publisher=game[2],
            region=game[3], format=game[4], license=game[5], genre=[6])
        g.save()