#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base_page import BasePage
# from .locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()

    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
    #         "Login link is not presented"

