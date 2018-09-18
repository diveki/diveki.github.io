import os
from subprocess import Popen
import sys

def run_html_buildup(d):
    file_name = d['file_name']
    title = d['title']
    out_file = d['out_file']
    comm = 'python convert.py ' + file_name + ' -title ' + title + ' -out ' + out_file
    print(comm)
    Popen(comm, shell=True).wait()


d_container = [
    {'file_name': 'body_texts/index_template.html',
     'title': 'Zsolt_Diveki',
     'out_file': 'index.html'
    },
    {'file_name': 'body_texts/projects_template.html',
     'title': 'Projects',
     'out_file': 'projects/index.html'
    },
    {'file_name': 'body_texts/wine_list_template.html',
     'title': 'Wine_Project',
     'out_file': 'projects/wine/index.html'
    },
    {'file_name': 'body_texts/variety_analysis_publish.ipynb',
     'title': 'Sommelier_Analysis',
     'out_file': 'projects/wine/wine.html'
    },
    {'file_name': 'body_texts/blind_taster_algorithm.ipynb',
     'title': 'Sommelier_Algorithm',
     'out_file': 'projects/wine/sommelier.html'
    },
    {'file_name': 'body_texts/vectorizer_publish.ipynb',
     'title': 'Vector_model',
     'out_file': 'projects/wine/tfidf.html'
    }
]

for item in d_container:
    run_html_buildup(item)
