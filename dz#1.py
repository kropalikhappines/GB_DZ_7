import os

folders = {'my_project':
               {'settings',
                'mainapp',
                'adminapp',
                'autoapp'}}

def create_folders(fold):
    for i, x in folders.items():
        print(x)
        for y in x:
            path = os.path.join(i, y)
            print(i, y)
            if not os.path.exists(path):
                os.makedirs(path)

create_folders(folders)