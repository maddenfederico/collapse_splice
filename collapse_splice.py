#! python3

import os
import shutil
from pathlib import Path

splice_packs = 'E:\\Splice\\Samples\packs'

#Move samples to root of pack folder for each pack
for folder_name, _, samples in os.walk(splice_packs):
    print('The current folder is ' + folder_name)

    if Path(folder_name).parent.name == 'packs':
        pack_folder = folder_name

    for sample in samples:
        try:
            print(f'Moving {sample} to {pack_folder}')
            shutil.move(os.path.join(folder_name, sample), pack_folder)
        except:
            pass

    print('')


#Remove now-empty subdirectories
for folder_name, subfolders, _ in os.walk(splice_packs):
    print(f'The current folder is {folder_name}')

    if Path(folder_name).parent.name == 'packs':
        for subfolder in subfolders:
            print(f'Removing folder {os.path.join(folder_name, subfolder)}')
            shutil.rmtree(os.path.join(folder_name, subfolder))
