#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Basket should be empty"

    def shoud_be_message_about_empty_basket(self):
        basket_text = self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_ITEMS_IN_BASKET).text
        print("\ntext about items:", basket_text)
        msg_ru = "Ваша корзина пуста"
        msg_en = "Your basket is empty"
        assert msg_ru or msg_en in basket_text, f"Should be message '{msg_en}'"


