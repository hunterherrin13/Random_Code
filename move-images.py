import os,shutil
from pathlib import Path

Source = 'D:/2022-08-05'
Final = 'D:/2022-08-05/Sorted'
os.mkdir(Final+'/JPEG/')

if not os.path.isdir(Final):
    os.mkdir(Final)
    os.mkdir(Final+'/JPG/')
    os.mkdir(Final+'/JPEG/')
    os.mkdir(Final+'/PNG/')
    os.mkdir(Final+'/BMP/')
    os.mkdir(Final+'/GIF/')
    os.mkdir(Final+'/MP4/')
    os.mkdir(Final+'/MOV/')


for file in Path(Source).rglob('*.jpg'):
    print(file)
    shutil.move(file,Final+'/JPG/'+os.path.basename(file))

for file in Path(Source).rglob('*.jpeg'):
    print(file)
    shutil.move(file,Final+'/JPEG/'+os.path.basename(file))

for file in Path(Source).rglob('*.png'):
    print(file)
    shutil.move(file,Final+'/PNG/'+os.path.basename(file))

for file in Path(Source).rglob('*.bmp'):
    print(file)
    shutil.move(file,Final+'/BMP/'+os.path.basename(file))

for file in Path(Source).rglob('*.GIF'):
    print(file)
    shutil.move(file,Final+'/GIF/'+os.path.basename(file))

for file in Path(Source).rglob('*.mp4'):
    print(file)
    shutil.move(file,Final+'/MP4/'+os.path.basename(file))

for file in Path(Source).rglob('*.mov'):
    print(file)
    shutil.move(file,Final+'/MOV/'+os.path.basename(file))
