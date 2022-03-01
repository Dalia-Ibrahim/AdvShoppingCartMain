import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdsSopCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.create_new_user()
        methods.user_navigator()
        methods.log_in(locators.new_username, locators.new_password)
        methods.delete_user()
        methods.log_in(locators.current_name, locators.current_password)
        methods.tearDown()

