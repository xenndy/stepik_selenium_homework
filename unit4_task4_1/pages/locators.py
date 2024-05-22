#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
        

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1)")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    TOTAL_BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3)")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")

class BasketPageLocators():
    TEXT_ABOUT_ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")




