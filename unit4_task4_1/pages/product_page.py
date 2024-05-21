#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def should_be_messages(self):
        self.should_be_added_to_basket_message()
        self.message_should_contain_product_name()
        self.should_be_basket_total_price_message()
        self.message_should_contain_product_price()

    def should_be_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Message about adding product to basket is not presented"

    def message_should_contain_product_name(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print("\nprod name:", product)
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        print("product_in_basket:", product_in_basket)
        assert product == product_in_basket, f"Wrong name of product in basket! Should be '{product}'"

    def should_be_basket_total_price_message(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_BASKET_PRICE_MESSAGE), \
            "Message about total basket price is not presented"

    def message_should_contain_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # print("\nproduct price:", product_price)
        basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE).text
        # print("basket_price:", basket_price)
        assert product_price == basket_price, f"Wrong total basket price! Should be '{product_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
           "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Success message should disappear, but it's still here"

