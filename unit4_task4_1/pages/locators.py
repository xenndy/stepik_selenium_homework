#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

# class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
        

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1)")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    TOTAL_BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3)")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")




