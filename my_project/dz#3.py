import os
import shutil

main = 'my_project'
folder = 'templates'


def pars():
    path = os.path.join(main, folder)
    if os.path.exists(path):
        shutil.rmtree(path)

    for root, dirs, files in os.walk(main):
        for direct in dirs:
            if direct == folder:
                res_path = os.path.join(root, direct)
                shutil.copytree(res_path, path, dirs_exist_ok=True)


pars()
