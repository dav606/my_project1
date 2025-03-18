from selenium.webdriver.common.by import By

baseURL = 'https://www.laptopscreen.com/English/'
contactUsURL = 'section/contact-us/'
cartURL = 'cart/'
goodURL = 'model/HP/1000-1100~SERIES/'
search_input_locator = (By.XPATH, '//*[@id="ver-1"]/div[3]/div/div[1]/div/form/input')
contact_us_locator = (By.LINK_TEXT, "Contact Us")
add_to_cart_locator = (By.XPATH, "//button[text()='TO CART']") #finds add to cart button
cart_counter_locator = (By.XPATH, "//span[@class='data-qty']")#finds an element,that shows the quantity of goods
