from os import listdir
from os.path import isfile, join
from random import sample
import sys


if __name__ == '__main__':
    ds_path = str(sys.argv[1])
    files = [f for f in listdir(ds_path) if isfile(join(ds_path, f))]
    jpgs = [f for f in files if f.split('.')[1] == 'jpg']
    txts = [f for f in files if f.split('.')[1] == 'txt']

    """
    print(len(jpgs), len(txts))
    for f in jpgs:
        txtf = join(ds_path, f.split('.')[0] + '.txt')
        jpgf = join(ds_path, f)
        if not isfile(txtf):
            print(jpgf)
    """
    for f in txts:
        try:
            files.remove(f)
            files.remove(f.split('.')[0] + '.jpg')
        except ValueError:
            print(f + ' is messing with you')
        jpgf = join(ds_path, f.split('.')[0] + '.jpg')
        txtf = join(ds_path, f)
        if not isfile(jpgf):
            print(txtf)

    print(files)
