# Wadsnip
Formerly:
A bunch of python scripts that do cool stuff with Doom wads and PK3 archives.
Now:
Python script [standalone] that 2x upscales PNG images with transparency. No Doom port or WAD files required.

### Standalone
Generate your own high resolution PNG & alpha with the help of Neural Net upscaling!
Uses waifu2x with xbrz(ScalerTest) to determine the alpha layer. See [STANDALONE](STANDALONE.md) for details and pre-built releases.

```
standalone can be launched with arguments:
python standalone.py in out
```
where 'in' is input file or directory, 'out' is output file or directory.
directories can be nested, output file\directory order is same as in input;
also standalone can be launched without arguments, but folder 'in' should be presend and not empty;

## Setup
*Tested on Windows with Python3.8*
```
git clone https://github.com/rev3n4nt/wadsnip.git
git submodule update --init --recursive
pip3 install pillow
pip3 install chainer
pip3 install cupy101
pip3 install pyinstaller
```
cupy101 - optional
pyinstaller - for executable from python
* for running image conversion - xbrzscale executable need to be downloaded & placed in same folder with standalone script or executable (which one you running).

## For Windows:
compiling into executable file by following command:
pyinstaller.exe --onefile --paths '/[path to Python3]/Lib/site-packages/;waifu2x_chainer/' standalone.py

i.e :
pyinstaller.exe --onefile --paths '/c/Program\ Files\ \(x86\)/Python38-32/Lib/site-packages/;waifu2x_chainer/' standalone.py

standalone executable can be launched with arguments or without, same as python file;

[xbrzscale] (executables from https://sourceforge.net/projects/xbrz/files/HqMAME/) originally (https://github.com/atheros/xbrzscale) and [waifu2x-chainer](https://github.com/tsurumeso/waifu2x-chainer) only needed for hires functionality.
Cupy is only needed if you want to speed up generation of hires packages with the use of a GPU (currently turned off). See [waifu2x-chainer](https://github.com/tsurumeso/waifu2x-chainer) for details.

## TODO
* Define keywords and expected structure for info parsing (regex findall tuples?)
* Determine wad graphics by whatever is an image type that is not in pnames
* Use photogrammetry to generate more sprite rotations.

## Licensing
Wadsnip is licensed under GPL v3.

## Contributions
There is a core set of functionality under [doom](doom/) that is at least somewhat extensible, and plenty of interesting things you can do with the code that are not fully demonstrated.
Please feel free to fork this(or former) project to add new functionality and scripts. Make a pull request if you think your code is universally useful and follows the following vague rules:
1. The project structure is such that user interactable scripts should be short and sweet, mostly just argument parsing for a function in [doom.util](doom/util.py).
2. All functions in [doom.util](doom/util.py) should provide their own imports to avoid unnecessary dependencies. (A user shouldn't be forced to install PIL or chainer for a simple lump extraction for example).