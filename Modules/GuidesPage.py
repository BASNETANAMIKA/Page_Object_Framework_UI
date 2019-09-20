from PageObjectLibrary import PageObject
from robot.api import logger as log
from Common_Utils import Utils


class GuidesPage(PageObject):
    PAGE_URL = "/"

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
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def verify_goto_guides_page(self):
        self.utils.search("Guides")
        return self

