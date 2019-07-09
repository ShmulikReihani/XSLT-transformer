import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
from Utils.Logger import Logger as logger
from Utils.InputValidator import InputValidator

'''
 XSLTParser receives a list of heros.xml files, then converts each file to xml object.
 After that XSLTParser combine all the xml objects to one xml file(output.xml).
'''


class XSLTParser:

    def __init__(self, files_names):
        self.logger = logger('XSLTParser', __name__)
        self.input_validator = InputValidator()
        self.files_names = files_names
        self.characters_list = []

    '''
     Iterate over each file and check if file is valid. 
     Then each file convert to xml object with the same format as character.xml, and store in a list.
    '''
    def __extract_character(self, root_tag, root_children, list_of_tags, tag_name_to_extract):
        for file_name in self.files_names:
            path = os.path.join(os.path.abspath("input_files"), file_name)
            self.logger.logger.info("Start parsing - {}.".format(file_name))
            if self.input_validator.is_valid_file(path, root_tag, root_children, list_of_tags):
                self.logger.logger.info("The File {} is valid.".format(file_name))
                dom = ET.parse(path)
                heros = dom.findall(root_children)
                for hero in heros:
                    characters = hero.find(tag_name_to_extract)
                    list_of_characters = characters.text.split(',')
                    for name in list_of_characters:
                        self.__build_character_xml_files(name)
            else:
                self.logger.logger.error("The File {} is not valid.".format(file_name))
                return False
        return True

    # For each character name create character.xml object.
    def __build_character_xml_files(self, name):
        characters = ET.Element('characters')
        character = ET.SubElement(characters, 'character')
        character.set('name', 'character')
        character.text = name
        self.characters_list.append(character)
        self.logger.logger.info('Create characters.xml object to {} hero.'.format(name))

    # Iterate over each character.xml objects and combine them to one xml file with the require format.
    def __build_output_file(self):
        characters = ET.Element('characters')
        for character in self.characters_list:
            name = character.text
            character = ET.SubElement(characters, 'character')
            character.set('name', 'character')
            character.text = name
        characters_xml = ET.tostring(characters)
        reparsed = minidom.parseString(characters_xml)
        xml_pretty = reparsed.toprettyxml(indent="  ")
        output_file = open("output.xml", "w")
        output_file.write(xml_pretty)

    '''
     Extracting all the xml input files.
     If we succeed to extract them then we should build a output.xml file.
    '''
    def transform_xml_files(self, root_tag, root_children, list_of_tags, tag_name_to_extract):
        if self.__extract_character(root_tag, root_children, list_of_tags, tag_name_to_extract):
            self.__build_output_file()
            self.logger.logger.info('Finished parsing files and create output.xml file.')
