# XSLT transformer
> XSLT transformer helps us to convert xml files to one xml file that contains all fortnight hero names.

## Table of contents
* [How it work](#How-it-work)
* [Sequence diagram](#sequence-diagram)
* [Technologies and libraries ](#technologies-and-libraries)
* [How to use](#how-to-use)

## How it works
For first the user provides several files, then XSLT transformer iterates over the files, and for each file performing the following steps: <br/>
1. Validating the current file.
	1. We first check if the file exists.
	2. Then we check if the file is xml file, which have the same format like heros.xml.
2. Then we start converting each file to xml object with the same format as the character.xml.
3. For last we aggregate the transformed files to a single output.xml file.

XSLT transformer can be easily changed in future, for example if your xml file would change or if we decide to extract another value from the files.

## Sequence diagram
![alt text](https://github.com/ShmulikReihani/XSLT-transformer/blob/master/Diagram/diagram.png)

## Technologies and libraries 
* Tech 1 - Python 3.7
* library 1 - argparse
* library 2 - logging
* library 3 - xml
* library 4 - os

## How to use
In cmd:<br/>
`
  python fortnight.py heros1.xml heros2.xml
`
