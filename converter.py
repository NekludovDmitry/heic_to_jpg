from PIL import Image
from pillow_heif import register_heif_opener
import os
from datetime import datetime
register_heif_opener()

folder_path = "../Фото и видео из Яндекс.Диска"
# date_str = datetime.now().strftime('%y%m%d') 
date_str = '240513'  # put date str in format yymmdd, for unique converting
jpg_qulity = 70

# Нужно найти все .heic фото
# Конвертировать их в .jpg с форматом названия и текущей датой "старое название, без формата"_hYYYYMMDD.jpg
# удалить .heic фото
# Скопировать на диски

all_files = os.listdir(folder_path)
print('number of all files in folder:',len(all_files))
set_all_files = all_files
heic_files = [f for f in all_files if f.endswith('.HEIC')] #os.path.splitext(f)
l_heic_files = len(heic_files)
print('number of heic files in folder:',l_heic_files)
set_heic_new_filenames = set([f'{os.path.splitext(f)[0]}_h{date_str}.jpg' for f in heic_files])
print('number already converted heic files:',len(set_heic_new_filenames.intersection(set_all_files)))
if len(set_heic_new_filenames.intersection(set_all_files)) > 0:
    print('5 sample:')
    print(list(set_heic_new_filenames.intersection(set_all_files))[:5])
    useranswer = input(f'already converted files will be ignored, other {len(set_heic_new_filenames) - len(set_heic_new_filenames.intersection(set_all_files))} will be converted, continue y/n:')
    if useranswer != 'y':
        print('converting dismissed, exiting')
        exit()

for i, filefpath in enumerate(heic_files):
    filename = os.path.splitext(filefpath)[0]
    if f'{filename}_h{date_str}.jpg' in set_all_files:
        print('WARNING!!! For file', filename, 'jpg file already exists', to_filefpath)
    elif os.path.isfile(os.path.join(folder_path, filefpath)):
        heic_image = Image.open(os.path.join(folder_path, filefpath))
        to_filefpath = os.path.join(folder_path, f'{filename}_h{date_str}.jpg')
        if not(os.path.isfile(to_filefpath)):
            heic_image.save(to_filefpath, 'JPEG', quality=jpg_qulity)
        else:
            print('WARNING!!! For file', filename, 'jpg file already exists', to_filefpath)
        print(f'{filename}_h{date_str}.jpg', i+1, f'{round((i+1)*100 / l_heic_files, 1)}%')
