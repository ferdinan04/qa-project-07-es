import data
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string. Utilízalo cuando
    la aplicación espere el código de confirmación para pasarlo a tus pruebas. El código de confirmación del
    teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu "
                            "aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    order_taxi_button = (By.XPATH, '//button[contains(text(),"Pedir un taxi")]')
    selected_tariff_tcard_title = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')

    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_field = (By.ID, 'phone')
    next_button_in_phone_window = (
        By.XPATH, '//div[@class="section active"]//button[@class="button full"][contains(text(),"Siguiente")]')

    code_sms_field = (By.ID, 'code')
    confirm_button_in_sms_window = (
        By.XPATH, '//div[@class="section active"]//button[@class="button full"][contains(text(),"Confirmar")]')
    close_button_in_sms_window = (
        By.XPATH, '//div[@class="section active"]//button[@class="close-button section-close"]')

    pay_method_button = (
        By.XPATH, '//div[@class="pp-button filled"]//div[@class="pp-text"][contains(text(),"Método de pago")]')
    add_card_option = (By.XPATH, '//div[@class="pp-title"][contains(text(),"Agregar tarjeta")]')
    card_number_field = (By.XPATH, '//input[@class="card-input"][@id="number"]')
    card_code_field = (By.XPATH, '//input[@class="card-input"][@id="code"]')
    add_card_title = (By.XPATH, '//div[@class="head"][contains(text(),"Agregar tarjeta")]')
    add_card_button = (
        By.XPATH, '//div[@class="pp-buttons"]//button[@class="button full"][contains(text(),"Agregar")]')
    close_button_in_pay_window = (
        By.XPATH, '(//div[@class="section active"]//button[@class="close-button section-close"])[2]')

    comment_field = (By.ID, 'comment')

    requests_to_driver_header = (By.CLASS_NAME, 'reqs-arrow')

    switch_manta_y_panuelos = (By.XPATH, '(//span[@class="slider round"])[1]')

    ice_cream_add_button = (By.XPATH, '(//div[@class="r-counter-container"])[1]//div[@class="counter-plus"]')
    ice_cream_counter = (By.XPATH, '(//div[@class="r-counter-container"])[1]//div[@class="counter-value"]')

    reserve_taxi_button = (By.XPATH, '//button[@class="smart-button"]')

    modal_searching_message = (By.XPATH, '//div[@class="order-header-title"]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Set_route combina métodos de las direcciones ingresadas en from y to para practicidad
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def wait_for_seconds(self, seconds):
        sleep(seconds)

    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_taxi_button).click()

    def click_tariff_option(self, chosen_tariff_option):
        self.driver.find_element(By.XPATH,
                                 f'//div[@class="tcard-title"][contains(text(),"{chosen_tariff_option}")]').click()

    def get_selected_option_tariff(self):
        return self.driver.find_element(*self.selected_tariff_tcard_title).text

    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def click_next_in_phone_window(self):
        self.driver.find_element(*self.next_button_in_phone_window).click()

    def set_code_sms(self, code_sms):
        self.driver.find_element(*self.code_sms_field).send_keys(code_sms)

    def click_confirm_in_sms_window(self):
        self.driver.find_element(*self.confirm_button_in_sms_window).click()

    def click_close_sms_window(self):
        self.driver.find_element(*self.close_button_in_sms_window).click()

    def click_pay_method(self):
        self.driver.find_element(*self.pay_method_button).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card_option).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def set_card_details(self, card_number, card_code):
        self.set_card_number(card_number)
        self.set_card_code(card_code)

    def click_add_card_title(self):
        self.driver.find_element(*self.add_card_title).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def click_close_in_pay_method_window(self):
        self.driver.find_element(*self.close_button_in_pay_window).click()

    def set_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.comment_field).send_keys(message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.comment_field).get_property('value')

    def click_requests_to_driver(self):
        self.driver.find_element(*self.requests_to_driver_header).click()

    def get_slider_color_manta_y_panuelos(self):
        slider_element = self.driver.find_element(*self.switch_manta_y_panuelos)

        # Extrae el color del fondo del atributo de estilo
        color = slider_element.value_of_css_property('background-color')
        return color

    def click_request_manta_y_panuelos(self):
        self.driver.find_element(*self.switch_manta_y_panuelos).click()

    def set_n_ice_creams(self, n_ice_creams):
        for _ in range(int(n_ice_creams)):
            self.driver.find_element(*self.ice_cream_add_button).click()

    def get_n_ice_creams(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def click_reserve_taxi_button(self):
        self.driver.find_element(*self.reserve_taxi_button).click()

    def check_modal_searching_message(self):
        return self.driver.find_element(*self.modal_searching_message).text


class TestUrbanRoutes:
    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        # Configuración inicial para las pruebas. Inicializa el controlador de Chrome y habilita el registro de
        # eventos de rendimiento.

        from selenium.webdriver import DesiredCapabilities

        capabilities = DesiredCapabilities.CHROME

        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        cls.driver = webdriver.Chrome()

        # Abre la página de la aplicación
        cls.driver.get(data.urban_routes_url)
        # Crea una clase de objeto de página
        cls.routes_page = UrbanRoutesPage(cls.driver)

        return cls.routes_page

    # Prueba 1. Configurar la ruta desde 'from' hasta 'to'
    def test_set_route(self):
        # Se llaman los datos
        address_from = data.address_from
        address_to = data.address_to

        self.routes_page.wait_for_seconds(2)
        # Se ingresan los datos address_from y address_to en los campos 'from' y 'to' respectivamente
        self.routes_page.set_route(address_from, address_to)

        # Se comprueba que el valor del campo de texto 'from' sea el mismo ingresado en la data
        assert self.routes_page.get_from() == address_from
        # Se comprueba que el valor del campo de texto 'to' sea el mismo ingresado en la data
        assert self.routes_page.get_to() == address_to

    # Prueba 2. Seleccionar la tarifa Comfort
    def test_select_comfort_tariff(self):
        # Se llaman los datos
        tariff_option = data.tariff_option

        self.routes_page.wait_for_seconds(2)
        # Click en el botón 'Pedir taxi'
        self.routes_page.click_order_taxi_button()

        # Se hace click a la opción de tarifa escogida según el dato tariff_option
        self.routes_page.click_tariff_option(tariff_option)

        # Comprueba que el texto de la tarifa seleccionada sea la misma que la tarifa a la que se hizo click
        assert self.routes_page.get_selected_option_tariff() == tariff_option

    # Prueba 3. Rellenar el número de teléfono
    def test_fill_number_phone(self):
        phone_number = data.phone_number

        # Click en el botón 'Número de teléfono'
        self.routes_page.click_phone_number_button()

        # Se ingresa el número de teléfono en su campo respectivo
        self.routes_page.set_phone_number(phone_number)

        # Clic en el botón 'Siguiente' para enviar el número de teléfono
        self.routes_page.click_next_in_phone_window()

        # Llamada al método retrieve_phone_code
        code = retrieve_phone_code(self.routes_page.driver)
        print("Código de confirmación del teléfono:", code)
        # Se coloca el código en el campo SMS
        self.routes_page.set_code_sms(code)

        # Clic en el botón 'Confirmar' de la ventana de SMS
        self.routes_page.click_confirm_in_sms_window()

        # Se comprueba que el valor del campo de texto 'phone' sea el mismo ingresado en la data
        assert self.routes_page.get_phone_number() == phone_number

    # Prueba 4. Agregar una tarjeta de crédito
    def test_add_credit_card(self):
        card_number = data.card_number
        card_code = data.card_code

        # Click en el botón 'Método de pago'
        self.routes_page.click_pay_method()
        # Click en la opción 'Agregar tarjeta' en ventana Método de pago
        self.routes_page.click_add_card()

        # Se ingresan los datos de número de la tarjeta y su código
        self.routes_page.set_card_details(card_number, card_code)

        # Click en el título de la ventana de pago, para activar botón 'Agregar'
        self.routes_page.click_add_card_title()

        # Click en el botón 'Agregar' de la ventana de pago
        self.routes_page.click_add_card_button()

        # Clic en el botón X para cerrar la celda
        self.routes_page.click_close_in_pay_method_window()

        # Se comprueba que el valor del campo de número de tarjeta 'number' sea el mismo ingresado en la data
        assert self.routes_page.get_card_number() == card_number
        # Se comprueba que el valor del campo de código de tarjeta 'code' sea el mismo ingresado en la data
        assert self.routes_page.get_card_code() == card_code

    # Prueba 5. Escribir un mensaje para el conductor
    def test_message_to_driver(self):
        # Se llaman los datos
        message_for_driver = data.message_for_driver

        # Escribir mensaje al conductor
        self.routes_page.set_message_for_driver(message_for_driver)

        # Se comprueba que el valor del campo de mensaje al conductor sea el mismo ingresado en la data
        assert self.routes_page.get_message_for_driver() == message_for_driver

    # Prueba 6. Pedir Manta y pañuelos
    def test_request_manta_and_panuelos(self):
        # Se obtiene la posición inicial del slider
        color_inicial = self.routes_page.get_slider_color_manta_y_panuelos()

        # Habilitar el switch para solicitar manta y pañuelos
        self.routes_page.click_request_manta_y_panuelos()

        self.routes_page.wait_for_seconds(3)
        # Se obtiene la posición final del slider
        color_final = self.routes_page.get_slider_color_manta_y_panuelos()

        # Se comprueba que la posición final del slider sea mayor y por tanto indique que se activó
        assert color_final != color_inicial

    # Prueba 7. Pedir 2 helados
    def test_add_2_ice_creams(self):
        # Se llaman los datos
        n_ice_creams = data.n_ice_creams

        # Añadir helados
        self.routes_page.set_n_ice_creams(n_ice_creams)

        # Se comprueba que el valor del campo de mensaje al conductor sea el mismo ingresado en la data
        assert self.routes_page.get_n_ice_creams() == n_ice_creams

    # Prueba 8
    def test_modal_taxi_appears(self):
        # Se llaman los datos
        modal_searching_message = data.modal_searching_message

        # Click en el botón de 'Solicitar taxi'
        self.routes_page.click_reserve_taxi_button()

        # Aparece el modal de búsqueda de taxi
        assert self.routes_page.check_modal_searching_message() == modal_searching_message

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
