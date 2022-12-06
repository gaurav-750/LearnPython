from selenium import webdriver

print("Selenium: Automation Testing Tool For Websites")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)
browser.get("https://github.com")

browser.maximize_window()  # For maximizing window

# Find the sign in element and click on it
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

browser.implicitly_wait(4)  # * gives an implicit wait for 20 seconds

# *send the username and password in appropriate textboxes
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("gaurav-750")

password_box = browser.find_element_by_id("password")
password_box.send_keys("Realme6750")
password_box.submit()


#! Verify if you are logged in perfectly:
assert 'gaurav-750' in browser.page_source
print("Sign In Successfull!")


# browser.implicitly_wait(10)

# profile_link = browser.find_element_by_class_name('user-profile-link')
# print('prpfilelink', profile_link)
# profile_name = profile_link.get_attribute("innerHTML")
# assert "gaurav-750" in profile_name
