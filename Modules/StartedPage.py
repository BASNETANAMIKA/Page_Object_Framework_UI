from PageObjectLibrary import PageObject
from robot.api import logger as log
from robot.utils import asserts
from Common_Utils import Utils
import Messages


class StartedPage(PageObject):
    PAGE_URL = "/getting-started"
    Utils = Utils()
    selectors = Utils.get_selectors_from_obj_file("obj_repo_started_page.py")

    def __init__(self):
        PageObject.__init__(self)
        self.utils = Utils()

    def _is_current_page(self):
        # this site uses the same title for many pages,
        # so we can't rely on the default implementation
        # of this function. Instead, we'll check the page
        # location, and raise an appropriate error if
        # we are not on the correct page
        location = self.selib.get_location()
        log.info("location is {0}".format(location))
        if not (self.PAGE_URL in location):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def verify_started_page(self):

        header = self.selib.get_webelement(self.selectors['page_header']).text
        sub_header = self.selib.find_element(self.selectors['sub_header']).text
        log.info("Heading of page is \"{0} \" ".format(header))
        log.info("Heading of page is \"{0} \" ".format(sub_header))
        asserts.assert_equal("Getting Started", header, "The heading of getting started page does not match")
        asserts.assert_equal(Messages.SUB_HEADING_MESSAGE, sub_header, "The sub heading of getting started page does "
                                                                       "not match")
        return self
    
    def verify_tab_options(self, options):
        log.info(options)
        log.info(type(options))
        options_list = []
        options_list_temp = options.split("Getting Started ")
        options_list.append("Getting Started")
        log.info(options_list_temp)
        options_list.extend(options_list_temp[1].split(" "))
        log.info("options_list is {0}".format(options_list))
        # log.info(options_list_temp)
        for tab_name in options_list:
            locator_name = self.selectors['tab_option']
            log.info("locator_name is {0}".format(locator_name))
            if tab_name == "Getting Started":

                locator_name = locator_name.replace('{n}', 'getting-started')
            #     locator_name = (self.selectors['tab_option'], n="getting-started")
            else:
                locator_name = locator_name.replace('{n}', str(tab_name).lower())

            log.info(locator_name)
            tab_found = self.utils.verify_element_visible(locator_name)
            asserts.assert_true(tab_found, "tab %s not found" % tab_found)
        return self


