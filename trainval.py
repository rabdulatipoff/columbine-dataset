from os import listdir
from os.path import isfile, join
from random import sample
import sys


if __name__ == '__main__':
    ds_path = str(sys.argv[1])
    files = [f for f in listdir(ds_path) if isfile(join(ds_path, f))]
    jpgs = [f for f in files if f.split('.')[1] == 'jpg']

    to_val = float(sys.argv[2])
    val = sample(jpgs, k=int(len(jpgs) * to_val))
    train = [f for f in jpgs if f not in val]

    with open('train.txt', 'w') as trainf:
        for f in train: trainf.write('./dataset/train_items/' + f + '\n')

    with open('val.txt', 'w') as valf:
        for f in val: valf.write('./dataset/train_items/' + f + '\n')
