from PIL import Image
from pillow_heif import register_heif_opener
import os

# Нужно найти все .heic фото
# Убедиться, что нет фотографий с .любым другим форматом, которые сейчас .heic (то есть одновременно уже есть и такая и такая фотка) --TODO сейчас тут
# Конвертировать их в .jpg
# удалить .heic фото
# Скопировать на диски

register_heif_opener()
folder_path = "Фото и видео из Яндекс.Диска"
heic_counter = 0

all_files = os.listdir(folder_path)

# for filename in os.listdir(folder_path):
    # if filename[-5:] == '.HEIC' and os.path.isfile(os.path.join(folder_path, filename)):
        # heic_counter += 1
        # # os.path.isfile(os.path.join(folder_path, filename))
        # print(filename, filename[:-5])

# heic_image = Image.open('2023-07-30 15-35-37.HEIC')
 # for i in range (1,11):
    # heic_image.save(f'2024-02-20 11-02-33_v{i}0.jpg','JPEG',quality=i*10)
    
print('start')
heic_files = [f for f in all_files if f.endswith('.HEIC')]
set_heic_files = set([os.path.splitext(f)[0] for f in heic_files])
dict_heic_files = {os.path.splitext(f)[0]:f for f in heic_files}
not_heic_files = [f for f in all_files if not(f.endswith('.HEIC'))]
set_not_heic_files = set([os.path.splitext(f)[0] for f in not_heic_files])
dict_not_heic_files = {f:[] for f in set_not_heic_files}
[dict_not_heic_files[os.path.splitext(f)[0]].append(f) for f in not_heic_files]
print(len(heic_files), len(all_files), len(not_heic_files))
print(len(set_heic_files), len(set_not_heic_files))
print(len(set_heic_files.intersection(set_not_heic_files)))
if len(set_heic_files.intersection(set_not_heic_files)) > 0:
    print('Присутствуют файлы, которые заканчиваются на .heic и любой другой формат')
    # print(len(set_heic_files.intersection(set_not_heic_files)))
    for f in set_heic_files.intersection(set_not_heic_files):
        print(f,':')
        print(' ',dict_heic_files[f])
        print(' ',dict_not_heic_files[f])
    exit()
print('end')

for heic_file in heic_files:
    file_name = os.path.splitext(heic_file)[0]
    # other_files = [f for f in all_files if f.startswith(file_name) and f != heic_file]
    
    # for other_file in other_files:
        # print(f'{heic_file} has a corresponding file {other_file}')
    if os.path.isfile(os.path.join(folder_path, filename)):
        print(f'{heic_file} has a corresponding file {other_file}')
    
# print('heic files found:', heic_counter)
print('heic files found:', len(heic_files))