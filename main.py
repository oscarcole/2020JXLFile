import os
import shutil

# otherMainDir = r'O:\FolderForTesting\2020 Jobs'
mainDir = r'O:\2020 Jobs'
subDir = r'O:\2020 Jobs\AllTheJXLs2020'
list_of_jxls = []


def list_files(directory):

    # loops through 2020 Jobs and prints .jxl file name
    for root, rdf, files in os.walk(mainDir):
        for name in files:

            # looks for .jxl extension in folders
            if name.endswith('.jxl'):

                # appends file paths to list
                list_of_jxls.append(os.path.join(root, f'{name}'))

                # writes jxls to log
                with open(f"{mainDir}/log.txt", 'a') as log:
                    log.write(os.path.join(root, f'{name}\n'))
            else:
                pass

    log.close()


list_files(r'O:\2020 Jobs')

for item in list_of_jxls:
    shutil.copy(item, subDir)
