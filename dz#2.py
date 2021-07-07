import os
import yaml


def create_folders(folder, prev=None):
    for main, folders in folder.items():
        mains = [main] if not prev else prev + [main]
        path = os.path.join(*mains)
        if not os.path.exists(path):
            os.makedirs(path)
        if type(folders) == list:
            for fold in folders:
                if type(fold) == str:
                    path = os.path.join(*mains, fold)
                    if fold.endswith('.py') or fold.endswith('.html'):
                        with open(path, 'a+') as f:
                            #print(f)
                            pass
                elif type(fold) == dict:
                    create_folders(fold, mains)
        elif type(folders) == dict:
            create_folders(folders, mains)


def file_conf():
    with open('config.yaml') as conf:
        templates = yaml.safe_load(conf)
    create_folders(templates)


file_conf()
