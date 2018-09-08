import os
from subprocess import Popen
import sys

index = ['index']

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
file_comp = os.path.splitext(inFile)
newFile = file_comp[0]+'.html'

if file_comp[1] == '.ipynb':
    Popen('jupyter nbconvert '+inFile +' --template basic', shell=True).wait()
    layout = 'custom/layout.html'
    navbar = 'custom/navbar.html'
    # css    = 'custom/main_css.css'
    css    = 'custom/alternative_css.css'
    js     = 'custom/main_js.html'
    mathjax= 'custom/mathjax.txt'
    footer = 'custom/footer.html'
else:
    layout = 'custom/layout.html'
    navbar = 'custom/navbar.html'
    css    = 'custom/alternative_css.css'
    js     = 'custom/main_js.html'
    mathjax= 'custom/mathjax.txt'
    footer = 'custom/footer.html'

title = get_arguments('-title', 'Zsolt Diveki')
out   = get_arguments('-out', newFile)
###########################
template = open(layout, 'r').read()

read_navbar = open(navbar, 'r').read()
read_css = open(css, 'r').read()
read_gs = open(js,'r').read()
read_body = open(newFile, 'r').read()
read_mathjax = open(mathjax, 'r').read()
read_footer = open(footer, 'r').read()
#
template = template.replace("title_block", "\n" + title + "\n")
template = template.replace("navbar_block", "\n" + read_navbar + "\n")
template = template.replace("js_block", "\n" + read_gs + "\n")
template = template.replace("css_block", "\n" + read_css + "\n")
template = template.replace("body_block", "\n" + read_body + "\n")
template = template.replace("math_block", "\n" + read_mathjax + "\n")
template = template.replace("footer_block", "\n" + read_footer + "\n")

with open(out, 'w') as f:
    f.write(template)
