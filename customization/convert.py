import os
from subprocess import Popen
import sys

def get_arguments(arg, alter):
    if arg in sys.argv:
        ind = sys.argv.index(arg)
        try:
            value = sys.argv[ind+1]
        except IndexError:
            print('Error: You have to give a title!')
            sys.exit()
    else:
        value = alter
    return value

# register the file that you want to convert
inFile = sys.argv[1]

title = get_arguments('-title', 'Zsolt Diveki')

Popen('jupyter nbconvert '+inFile +' --template basic', shell=True).wait()
newFile = os.path.splitext(inFile)[0]+'.html'

template = open('custom/layout.html', 'r').read()

read_navbar = open('custom/navbar.html', 'r').read()
read_css = open('custom/main_css.css', 'r').read()
read_gs = open('custom/main_js.html','r').read()
read_body = open(newFile, 'r').read()
read_mathjax = open('custom/mathjax.txt', 'r').read()
read_footer = open('custom/footer.html', 'r').read()
#
template = template.replace("title_block", "\n" + title + "\n")
template = template.replace("navbar_block", "\n" + read_navbar + "\n")
template = template.replace("js_block", "\n" + read_gs + "\n")
template = template.replace("css_block", "\n" + read_css + "\n")
template = template.replace("body_block", "\n" + read_body + "\n")
template = template.replace("math_block", "\n" + read_mathjax + "\n")
template = template.replace("footer_block", "\n" + read_footer + "\n")

with open(newFile, 'w') as f:
    f.write(template)
