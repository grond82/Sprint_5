from selenium.webdriver.common.by import By

class TestLocators:
    CONSTRUCTOR_FILLINGS = (By.XPATH, ".//span[contains(text(),'Начинки')]") #Локатор для клика на Начинки
    CONSTRUCTOR_FILLINGS_SELECT = (By.XPATH, ".//div[contains(@Class, 'tab_tab')][3]") #Локатор, если Начинки выбраны
    CONSTRUCTOR_SAUCES = (By.XPATH, ".//span[contains(text(),'Соусы')]") #Локатор для клика на Соусы
    CONSTRUCTOR_SAUCES_SELECT = (By.XPATH, ".//div[contains(@Class, 'tab_tab')][2]") #Локатор, если Соусы выбраны
    CONSTRUCTOR_BUNS = (By.XPATH, ".//span[contains(text(),'Булки')]") #Локатор для Булок
    CONSTRUCTOR_BUNS_SELECT = (By.XPATH,".//div[contains(@Class, 'tab_tab')][1]") #Локатор, если Булки выбраны
    BUTTON_ENTER_TO_ACCOUNT = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]") #Кнопка Войти в аккаунт
    LOGIN_EMAIL_FIELD = (By.NAME, "name") #Поле Email на странице Вход
    LOGIN_PASSWORD_FIELD = (By.NAME, "Пароль") #Поле Пароль на странице Вход
    BUTTON_ENTER_ON_LOGIN_PAGE = (By.XPATH, ".//button[text()='Войти']") #Кнопка Войти на странице Вход
    MY_CABINET = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]") #Локатор для входа в Личный кабинет
    EXIT_MY_CABINET = (By.XPATH, ".//button[contains(text(), 'Выход')]") #Локатор для выхода из Личного кабинета
    ENTER_TEXT_ON_LOGIN_PAGE = (By.XPATH, ".//h2[contains(text(),'Вход')]") #Локатор для проверки Login page
    CONSTRUCTOR_FROM_MY_CABINET_PAGE = (By.XPATH, ".//p[contains(text(),'Конструктор')]") #Локатор для перехода в Конструктор со страницы Личного кабинета
    LOGO_ON_MY_CABINET_PAGE = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") #Локатор для клика по лого на странице Личного кабинета
    BUTTON_ORDER = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]") #Кнопка Оформить заказ на homepage
    ENTER_ON_REGISTRATION_PAGE = (By.LINK_TEXT, "Войти") #Линк для входа на странице Регистрации
    FIELD_NAME_ON_REGISTRATION_PAGE = (By.XPATH, "(.//input[@name='name'])[1]") #Локатор для поля Имя на странице Регистрации
    FIELD_EMAIL_ON_REGISTRATION_PAGE = (By.XPATH, "(.//input[@name='name'])[2]") #Локатор для поля Email на странице Регистрации
    FIELD_PASSWORD_ON_REGISTRATION_PAGE = (By.XPATH, ".//input[@name='Пароль']") #Локатор для поля Password на странице Регистрации
    BUTTON_REGISTER_ON_REGISTRATION_PAGE = (By.XPATH, ".//button[text()='Зарегистрироваться']") #Кнопка Зарегистрироваться на странице Регистрации
    ERROR_ON_REGISTRATION_PAGE = (By.XPATH, ".//p[@class='input__error text_type_main-default']")
