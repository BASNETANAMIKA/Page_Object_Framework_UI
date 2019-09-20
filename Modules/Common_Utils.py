import os,time
from robot.api import logger as log
from PageObjectLibrary import PageObject
from selenium.webdriver.common.keys import Keys


class Utils(PageObject):
    
    def get_selectors_from_obj_file(self, file_name):
        """
        used to resolve locators from ObjectRepo/obj_repo_*.py
        """
        file_path = os.path.join(os.getcwd(), "ObjectRepo",  file_name)
        objfile = open(file_path, "r").read()
        split_file = objfile.split("selectors =")[1]
        # page_dict = {}
        # # exec(objfile in page_dict)
        selectors = eval(split_file)
        
        return selectors

    def verify_element_visible(self, locator):
        """
        verify if element is visible
        """
        try:
            self.selib.element_should_be_visible(locator)
            return True
        except AssertionError as err:
            log.error("error is {0}".format(err))
            return False

    def search(self, search_text):
        """
        search for the text in the search text box
        """
        self.selib.get_webelement('css=a.search-button.desktop-show >img').click()
        time.sleep(5)
        self.selib.get_webelement('css=input#search-input').send_keys(search_text, Keys.RETURN)
        time.sleep(5)
        log.info("the search box text is done")
        return self
