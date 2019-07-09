import argparse
from Utils.XSLTParser import XSLTParser
from argparse import RawTextHelpFormatter

'''
 fortnight.py is the entry point of our program.
 fortnight.py use argparse library for parsing command line.
 In the main method we define our parser which helps the user understand how execute our program.
 Then we pass several variables which define what kind of file we want to parse and what to extract form it.
'''


def description():
    return """
You should pass file names as follows: 
   heros1.xml         - the FIRST file
   heros2.xml         - the SECOND file
   ...
   herosN.xml         - the Nth file
"""


def main():
    parser = argparse.ArgumentParser(prog="PROG", formatter_class=RawTextHelpFormatter, epilog=description())
    parser.add_argument('files', metavar='N', type=str, nargs='+',
                        help='Input several xml file names to transform them to one xml file')

    args = parser.parse_args()
    parser_xml = XSLTParser(args.files)

    root_tag = "fortnight"
    root_children = "hero"
    list_of_tags = ["name", "characters", "rarities"]
    tag_name_to_extract = "characters"

    parser_xml.transform_xml_files(root_tag, root_children, list_of_tags, tag_name_to_extract)


if __name__ == "__main__":
    main()
