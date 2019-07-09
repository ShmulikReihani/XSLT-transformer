import os
import xml.etree.ElementTree as ET
from Utils.Logger import Logger as logger

'''
 InputValidator class helps to check if a file exists.
 If file exist than we check the file format.
'''


class InputValidator:

    def __init__(self):
        self.logger = logger("input_validation", __name__)

    # Private method that check if file exists.
    def __is_file_exist(self, full_path):
        if os.path.isfile(full_path):
            self.logger.logger.info("File {} exists".format(os.path.basename(full_path)))
            return True
        else:
            self.logger.logger.error("File {} doesn't exist. Skipping".format(os.path.basename(full_path)))
            return False

    '''
      Private method that get data of a require xml format,
      Then check if the file is has the same format.
    '''

    def __is_xml_format(self, full_path, root_children, root_name, list_of_tags):
        try:
            tree = ET.parse(full_path)
            self.logger.logger.info("File {} is an xml".format(os.path.basename(full_path)))
        except ET.ParseError:
            self.logger.logger.error(
                "The file {} is not an valid xml file. Skipping".format(os.path.basename(full_path)))
            return False
        root = tree.getroot()
        if root.tag == root_name:
            children = tree.findall(root_children)
            if children is not None:
                for hero in children:
                    for tag in hero:
                        if tag.tag not in list_of_tags:
                            self.logger.logger.error(
                                "File {} is an xml file but not have all tags".format(os.path.basename(full_path)))
                            return False
            else:
                self.logger.logger.error(
                    "File {} is an xml, but dose not same as the require xml file".format(os.path.basename(full_path)))
                return False
            self.logger.logger.info(
                "File {} is an xml and same as the required format".format(os.path.basename(full_path)))
            return True
        else:
            self.logger.logger.error(
                "File {} is an xml file but dose not same as the required format".format(os.path.basename(full_path)))
            return False

    # Validating file.
    def is_valid_file(self, path, root_tag, root_children, list_of_tags):
        return self.__is_file_exist(path) and self.__is_xml_format(path, root_children, root_tag, list_of_tags)
