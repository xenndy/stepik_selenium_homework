#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import pytest
from selenium import webdriver

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/"

# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


# def test_guest_should_see_login_link(browser):
#     # link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, LINK)
#     page.open()
#     page.should_be_login_link()


def test_guest_should_see_login_n_register_form(browser):
    login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, login_page_link)
    page.open()
    page.should_be_login_page()
