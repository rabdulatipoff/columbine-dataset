from os import listdir, sep
from os.path import isfile, join
from random import sample
import sys


if __name__ == '__main__':
    try:
        ds_path = str(sys.argv[1])
    except IndexError:
        raise Exception("You have to provide a valid dataset directory path as an argument")

    files = [f for f in listdir(ds_path) if isfile(join(ds_path, f))]
    jpgs = [f for f in files if f.split('.')[1] == 'jpg']

    try:
        to_val = float(sys.argv[2])
    except IndexError:
        raise Exception("You have to provide a valid float number for validation data percentage")

    val = sample(jpgs, k=int(len(jpgs) * to_val))
    train = [f for f in jpgs if f not in val]

    with open('train.txt', 'w') as trainf:
        for f in train: trainf.write('./dataset/' + ds_path + sep + f + '\n')

    with open('val.txt', 'w') as valf:
        for f in val: valf.write('./dataset/' + ds_path + sep + f + '\n')
