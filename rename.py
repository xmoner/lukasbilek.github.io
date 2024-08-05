import os
import fnmatch

script_dir = os.path.dirname(os.path.abspath(__file__))
print (script_dir)

images_path = script_dir + '/images/'
print(images_path)
def find_images(directory):
    # Seznam podporovaných přípon obrázků
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']

    # Seznam pro uložení nalezených obrázků
    images = []

    # Procházení souborů ve složce
    for root, dirnames, filenames in os.walk(directory):
        for extension in image_extensions:
            for filename in fnmatch.filter(filenames, extension):
                images.append(os.path.join(root, filename))
    return images
a=find_images(images_path)
#print (a)

def find_image_names(directory):
    # Seznam podporovaných přípon obrázků
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']

    # Seznam pro uložení nalezených obrázků
    images = []

    # Procházení souborů ve složce
    for root, dirnames, filenames in os.walk(directory):
        for extension in image_extensions:
            for filename in fnmatch.filter(filenames, extension):
                images.append( filename)
    return images
b=find_image_names(images_path)
for i in b:
    #os.rename(i,i.replace(' ','_'))
    print("![logo](./images/{})\n".format(i))