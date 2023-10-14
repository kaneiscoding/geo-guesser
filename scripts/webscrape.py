from selenium import webdriver


# Specify the path to the Chrome WebDriver executable
chrome_driver_path = r'C:\Users\pvshc\Desktop\Repositories\geo-guesser\chromedriver.exe'

# Initialize the Chrome WebDriver with the executable path
webdriver.chrome.driver = chrome_driver_path

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://google.com')

# Interact with the page, e.g., click a button
#element = driver.find_element_by_id('my-button')
#element.click()

# Extract data after the interaction
#result = driver.find_element_by_id('result-element').text
#rint('Result:', result)

# Close the browser
driver.quit()

