from os import listdir
from os.path import isfile, join
from random import sample
import sys


if __name__ == '__main__':
    try:
        ds_path = str(sys.argv[1])
    except IndexError:
        raise Exception("You have to provide a valid dataset directory path as an argument")

    files = [f for f in listdir(ds_path) if isfile(join(ds_path, f))]
    txts = [f for f in files if f.split('.')[1] == 'txt']

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
