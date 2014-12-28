genre=''
count = 0
with open('C:\Users\\bmo\\Desktop\\nes_parsed.txt','a') as p:
    with open('C:\\Users\\bmo\\Desktop\\nes_temp.txt', 'r') as n:
        str_line = ''
        for line in n.readlines():
            if '[*]' in line:
                genre = line.replace('[*]','').replace('\n','')
                continue
            str_line+= line
            count+=1
            if count == 6:
                str_line = str_line.replace('\n','|')
                count = 0
                if str_line[-1] != '|':
                    str_line+='|'
                p.write(str_line+genre+'\n')
                str_line = ''
    p.write('\n')
    print "updated: %s" % genre