import os
from subprocess import Popen
import sys

index = ['index']
setup_location = 'customization/custom'
abs_setup_location = os.path.abspath(setup_location)

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
    layout = os.path.join(setup_location, 'layout.html')
    navbar = os.path.join(setup_location, 'navbar.html')
    # css    = os.path.join(setup_location, 'main_css.css'
    css    = os.path.join(setup_location, 'alternative_css.css')
    js     = os.path.join(setup_location, 'main_js.html')
    mathjax= os.path.join(setup_location, 'mathjax.txt')
    footer = os.path.join(setup_location, 'footer.html')
else:
    layout = os.path.join(setup_location, 'layout.html')
    navbar = os.path.join(setup_location, 'navbar.html')
    css    = os.path.join(setup_location, 'alternative_css.css')
    js     = os.path.join(setup_location, 'main_js.html')
    mathjax= os.path.join(setup_location, 'mathjax.txt')
    footer = os.path.join(setup_location, 'footer.html')

title = get_arguments('-title', 'Zsolt Diveki')
out   = get_arguments('-out', newFile)

out_rel = out.split(os.sep)
seps = list(['..']) * (len(out_rel)-1)
seps = '/'.join(seps) + '/'
if seps == '/':
    seps = ''


###########################
template = open(layout, 'r').read()

read_navbar = open(navbar, 'r').read()
read_navbar = read_navbar.replace('PATHFILL', seps)
read_css = open(css, 'r').read()
read_css = read_css.replace('PATHFILL', seps)
read_gs = open(js,'r').read()
read_body = open(newFile, 'r').read()
read_mathjax = open(mathjax, 'r').read()
read_footer = open(footer, 'r').read()
back_button = '\n<div class="mb-5"><a href="index.html" class="btn btn-outline-success btn-md active" role="button" aria-pressed="true">Back</a></div>\n'

template = template.replace("title_block", "\n" + title + "\n")
template = template.replace("navbar_block", "\n" + read_navbar + "\n")
template = template.replace("js_block", "\n" + read_gs + "\n")
template = template.replace("css_block", "\n" + read_css + "\n")
template = template.replace("body_block", "\n" + read_body + "\n")
if file_comp[1] == '.ipynb':
    template = template.replace("back_button", back_button )
else:
    template = template.replace("back_button", '' )
template = template.replace("math_block", "\n" + read_mathjax + "\n")
template = template.replace("footer_block", "\n" + read_footer + "\n")

with open(out, 'w') as f:
    f.write(template)
