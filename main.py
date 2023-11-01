from selenium import webdriver

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# test
# Open a website in the Chrome window
driver.get("https://www.example.com")

# Close the window
driver.quit()
