import sys
import os
import shutil

# **************** #
# Global Variables #
# **************** #

# path to images and galleries and variables needed
PATH = '\\galleries'

# gets the Current working directory and stores in CWD
CWD = os.getcwd()


# ************************************** #
# build_html                             #
# writes the HTML file                   #
# takes date and title from DIR listing  #
# and full list of dates for indexing    #
# ************************************** #
def build_html(date, dates, title, gal_path, gal_name):
    
    # builds the full title string
    temp_date = date.split('_')
    month = get_month(temp_date[1])
    year = temp_date[0]
    full_title = title + " - " + month + ", " + year
    index_count = 0
    
    
    
    # builds the image list for later iteration
    image_list = os.listdir(gal_path)
    
    # opens f to read template g to write file
    f = open(CWD + '\\gal_temp.html', 'r')
    g = open(CWD  + '\\' + date + '.html', 'w')
    
    # loop to read and write the main HTML
    # conditions to write the new code using
    # nested for loop to iterate over image_list
    for line in f:
        g.write(line)
        temp = line.strip()
        if temp == "<!-- PRELOAD IMAGES HERE -->": #image preloader
            for image in image_list:
                g.write('\t\t<img src = \"galleries\\' + gal_name + '\\' + image + '\">\n')
        elif temp == "<!-- TITLE -->": #the gallerie title
            g.write('\t\t' + full_title)
        elif temp == "<!-- ADD IMAGES HERE -->": #slide loader
            for image in image_list:
                g.write('\t\t\t\t<img src = \"galleries\\' + gal_name + '\\' + image + '\">\n')
    
        elif temp == "<!-- MENU -->": #slide menu index
            for date in dates:
                index_count +=1
                if date == dates[-1]:
                        g.write('\t\t<a href=\"' + date + '.html\">' + str(index_count) +'</a>\n')
                else:
                    g.write('\t\t<a href=\"' + date + '.html\">' + str(index_count) +'</a> | \n')
                

    
    
    
    print 'Built: ' + full_title + ' ( ' + date + '.html )'
    
    
    f.close()
    g.close()

# ********************************* #
# get_month                         #
# takes the num value and converets #
# to text version                   #
# ********************************* #

def get_month(month_num):
    months = { "01" : "January",
               "02" : "February",
               "03" : "March",
               "04" : "April",
               "05" : "May",
               "06" : "June",
               "07" : "July",
               "08" : "August",
               "09" : "September",
               "10": "October",
               "11": "November",
               "12": "December", }
    return months.get(month_num)

# ************* #
# MAIN Function #
# ************* #
def main():
    # gets the path of the imgages directory
    path = CWD + PATH
    
    print "working dir: " + path +'\n'
    
    # creates a list of directories of galleries
    dirs = os.listdir(path)
    dirs.sort()
    dirs.reverse()
    
    # builts the list of dates
    # yyyy_MM format then sorts
    dates = []
    for dir in dirs:
        temp_dir = dir.split('.')
        dates.append(temp_dir[0])
    dates.sort()
    dates.reverse()
    
    # Main loop
    #builds the page out and 
    for dir in dirs:
    
        #the path to current directory
        temp_path = path + '\\' + dir
    
        #temporary list holder 
        temp_dir = dir.split('.')
        
        #splits date and title into vars
        date = temp_dir[0]
        title = temp_dir[1]
        
        
        
        # debug code
        #month = temp_dir[0].split('_')
        #month = get_month(month[1])
        #print "temp_dir: "
        #print temp_dir
        #print "temp_path: " + temp_path +"\n"
        #print title
        #print date
        #print "Month: " + month
        #print "HTML Exists?: " + str(os.path.exists(temp_dir[0] +'.html')) +'\n'
        # print dir
        # end debug code
        
        # runs the build html function that actually builds the pages
        build_html(date, dates, title, temp_path, dir)
        
        # creates a duplicate gallery if the first/newest item
        if dir == dirs[0]:
            if os.path.exists(CWD + '\\gallery.html'):
                os.remove(CWD + '\\gallery.html')
            shutil.copyfile(CWD + '\\' + date + '.html', CWD + '\\gallery.html')

    raw_input("press enter to exit!")
    
  

# boiler plate to start out
if __name__ == '__main__':
    main()