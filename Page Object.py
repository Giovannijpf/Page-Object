from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class OpenCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://opencart.abstracta.us/")
        time.sleep(3)
        
    def test_opencart_automation(self):
        # Paso 2: Buscar "iPhone"
        search_input = self.driver.find_element(By.NAME, "search")
        search_input.send_keys("iPhone")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # Paso 3: Seleccionar la primera opción
        first_product_link = self.driver.find_element(By.CSS_SELECTOR, ".product-layout:first-child .product-thumb")
        first_product_link.click()
        time.sleep(3)

        # Paso 4: Agregar al carrito de compras
        add_to_cart_button = self.driver.find_element(By.ID, "button-cart")
        add_to_cart_button.click()
        time.sleep(3)

        # Paso 5: Ingresar al carrito de compras
        cart_button = self.driver.find_element(By.ID, "cart-total")
        cart_button.click()
        time.sleep(3)

        # Paso 6: Presionar "View Cart"
        view_cart_button = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        view_cart_button.click()
        time.sleep(3)

        # Paso 7: Validar que el iPhone esté en el carrito de compras
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".table-responsive .text-left a")
        item_names = [item.text for item in cart_items]
        self.assertIn("iPhone", item_names)
        time.sleep(3)

        # Paso 8: Remover el iPhone del carrito de compras
        remove_button = self.driver.find_element(By.NAME, "remove")
        remove_button.click()
        time.sleep(3)

        # Paso 9: Validar que el iPhone ya no esté en el carrito de compras
        empty_cart_message = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-warning")
        self.assertIn("Your shopping cart is empty!", empty_cart_message.text)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
    time.sleep(3)