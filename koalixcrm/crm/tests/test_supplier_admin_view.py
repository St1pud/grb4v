# -*- coding: utf-8 -*-
import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from koalixcrm.crm.factories.factory_user import AdminUserFactory
from koalixcrm.crm.contact.supplier import Supplier


class TestSupplierAdminView(LiveServerTestCase):

    def setUp(self):
        firefox_options = webdriver.firefox.options.Options()
        firefox_options.set_headless(headless=True)
        self.selenium = webdriver.Firefox(firefox_options=firefox_options)
        self.test_user = AdminUserFactory.create()

    def tearDown(self):
        self.selenium.quit()

    @pytest.mark.front_end_tests
    def test_supplier_admin(self):
        selenium = self.selenium
        # login
        selenium.get('%s%s' % (self.live_server_url, '/admin/crm/supplier/'))
        # the browser will be redirected to the login page
        timeout = 5
        try:
            element_present = expected_conditions.presence_of_element_located((By.ID, 'id_username'))
            WebDriverWait(selenium, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        username = selenium.find_element_by_xpath('//*[@id="id_username"]')
        password = selenium.find_element_by_xpath('//*[@id="id_password"]')
        submit_button = selenium.find_element_by_xpath('/html/body/div/article/div/div/form/div/ul/li/input')
        username.send_keys("admin")
        password.send_keys("admin")
        submit_button.send_keys(Keys.RETURN)
        try:
            element_present = expected_conditions.presence_of_element_located((By.ID,
                                                                               '/html/body/div/article/header/ul/li/a'))
            WebDriverWait(selenium, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        # find the form element
        selenium.get('%s%s' % (self.live_server_url, '/admin/crm/supplier/add'))

        try:
            element_present = expected_conditions.presence_of_element_located((By.ID, '//*[@id="id_name"]'))
            WebDriverWait(selenium, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        name = selenium.find_element_by_xpath('//*[@id="id_name"]')
        name.send_keys("This is the name of a supplier")
        submit_button = selenium.find_element_by_xpath('/html/body/div/article/div/form/div/footer/ul/li[1]/input')
        submit_button.send_keys(Keys.RETURN)
        try:
            element_present = expected_conditions.presence_of_element_located((By.ID,
                                                                               '/html/body/div/article/header/ul/li/a'))
            WebDriverWait(selenium, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        supplier = Supplier.objects.get(name="This is the name of a supplier")
        self.assertEqual(type(supplier), Supplier)

