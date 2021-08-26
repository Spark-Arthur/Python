import os

# def copyfolder(folder, newfolder):
#     os.system("xcopy \""+folder+"\" \""+newfolder+"\" /h /i /c /k /e /r /y")
#
# folder = r'\Users\danza\Python-course\my_project\mainapp\templates'
# newfolder = r'\Users\danza\Python-course\my_project\templates'
#
# copyfolder(folder, newfolder)
#
# folder = r'\Users\danza\Python-course\my_project\authapp\templates'
# newfolder = r'\Users\danza\Python-course\my_project\templates'
#
# copyfolder(folder, newfolder)
# ----------------------------------------------------------------------
import os
import shutil

templates = 'templates'
html = '.html'
path = r'\Users\danza\Python-course\my_project'

for dirs, folder, files in os.walk(path):
    for file in files:
        if file.find(html) != -1:
            os.chdir(path)
            try:
                os.mkdir(templates)
            except FileExistsError:
                pass
            os.chdir(os.path.join(path, templates))
            html_file = os.path.split(dirs)
            try:
                os.mkdir(html_file[1])
            except FileExistsError:
                pass
            os.chdir(os.path.join(path, templates, html_file[1]))
            way = os.path.join(dirs, file)
            way_safe = os.path.join(path, templates, html_file[1])
            shutil.copy(way, way_safe)

