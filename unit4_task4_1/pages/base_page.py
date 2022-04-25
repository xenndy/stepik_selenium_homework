#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

