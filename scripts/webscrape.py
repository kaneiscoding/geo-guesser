from selenium import webdriver

# Initialize the Chrome WebDriver (provide the path to your Chrome WebDriver executable)
driver = webdriver.Chrome(executable_path=r'C:\Users\pvshc\Desktop\Repositories\geo-guesser')

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

