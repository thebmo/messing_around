# used resolution 700x465

# if tall, height = 465, width dynamic (max 700)
# talls 324x465
from PIL import Image
import os
import shutil

# gets the Current working directory and stores in CWD
CWD = os.getcwd()

# builds the main dir list 
dir_list = os.listdir(CWD)


    
# takes height and width returns ratio
def get_ratio(height, width):
    ratio = float(width)/float(height)
    #print ratio
    return ratio


def main():
    # makes the output folder
    output = os.path.join(CWD, 'output')
    if os.path.exists(output):
        shutil.rmtree(output)
        
    os.makedirs(output)
    
    # for loop to iterate through directories
    for dir in dir_list:
        
        
        # removes python files from dir list
        if '.py' in dir:
            dir_list.remove(dir)
        
        # removes jpg files from dir list
        elif '.jpg' in dir:
            dir_list.remove(dir)
       
       # builds the file list for the dir iterator
        else:
            # makes the new in output folder
            new_dir = os.path.join(output, dir)
            os.makedirs(new_dir)
            
            # makes a list of files in the sub dir
            files = os.listdir(dir)
            
            # prints the directory title
            print '\n' + dir
            
            # resets count to zero, used for naming jpgs
            count = 0
            
            for file in files:
                
                # adds one to the title iterator
                count +=1
                if count < 10:
                    title = '0' + str(count) + '.jpg'
                else:
                    title = str(count) + '.jpg'
                title = os.path.join(new_dir, title)
                
                path = os.path.join(CWD, dir)
                path = os.path.join(path, file)
                print file
    
    
                # opens the image to resize
                src = Image.open(path)

                o_width = src.size[0]
                o_height = src.size[1]

                ratio = get_ratio(o_height, o_width)

                # if image is taller than wider
                if o_height > o_width:
                    
                    # creates a black 700x465 image
                    img = Image.new('RGB', (700, 465))
                    
                    # sets new height width
                    n_height = 465
                    n_width = int(ratio * n_height)
                    
                    # resizes the source pick to new h/w
                    src = src.resize((n_width, n_height))
                    
                    # copy/pastes the src into the blank image and saves
                    copy = (0, 0, int(n_width), int(n_height))
                    copied = src.crop(copy)
                    paste = (((700-int(n_width))/2), 0)
                    img.paste(copied, paste)
                    
                    img.save(title, "JPEG")
                    
                # if image is wider, just resizes and saves
                else:
                    n_height = 465
                    n_width = 700
                    src = src.resize((n_width, n_height))
                    src.save(title, "JPEG")


# boiler plate to start out
if __name__ == '__main__':
    main()
    
    