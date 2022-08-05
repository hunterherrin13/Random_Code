import os,shutil
from pathlib import Path

Source = 'C:/Users/v-hherrin/Pictures/Saved Pictures'
Final = 'C:/Users/v-hherrin/Pictures/Saved Pictures/Grouped'

if not os.path.isdir(Final):
    os.mkdir(Final)


for file in Path(Source).rglob('*.jpg'):
    print(file)
    shutil.move(file,Final+'/'+os.path.basename(file))


    