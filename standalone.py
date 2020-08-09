#!/usr/bin/env python3

from PIL import Image
import glob
import os
import sys

sys.path.append('waifu2x_chainer')
from doom.graphic import data_to_image, xbrz_scale, waifu_scale

def mock_superscale(filename, scale):
    return Image.open(filename)

def superscale(filename, scale):
    with open(filename, 'rb') as fin:
        data = fin.read()

    xbrz_data = xbrz_scale(data, scale, 128)
    xbrz_img = data_to_image(xbrz_data)

    data = waifu_scale(data, scale, 0, 'ResNet10')

    img = data_to_image(data)
    img.putalpha(xbrz_img.split()[-1])

    return img


if len(sys.argv) == 1:
    in_dir = 'in'
    out_dir = 'out'
elif len(sys.argv) == 3:
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
else:
    sys.stderr.write('usage: standalone.py [in_dir out_dir]\n')
    sys.exit(1)

if not os.path.isdir(in_dir):
    raise Exception(f'{in_dir} does not exist or not a directory')

print(f'in dir: {in_dir}', flush=True)
print(f'out dir: {out_dir}', flush=True)
sys.stdout.flush()

for in_path in glob.iglob(f'{in_dir}/**/*.png', recursive=True):
    print(f'processing: {in_path}', flush=True)
    rel_path = os.path.relpath(in_path, in_dir)
    out_path = os.path.join(out_dir, rel_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img = superscale(in_path, 2)
    img.save(out_path)
    print(f'finished: {out_path}', flush=True)
