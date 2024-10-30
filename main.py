# # from flask import Flask, jsonify, request
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # import time

# # app = Flask(__name__)

# # @app.route('/run-selenium', methods=['POST'])
# # def run_selenium():
# #     try:
# #         driver = webdriver.Chrome()

# #         driver.get("http://www.python.org")
# #         if "Python" not in driver.title:
# #             return jsonify({"error": "Python not found in title"}), 400
# #         elem = driver.find_element(By.NAME, "q")
# #         elem.clear()
# #         elem.send_keys("pycon")
# #         elem.send_keys(Keys.RETURN)
# #         if "No results found." in driver.page_source:
# #             return jsonify({"error": "No results found"}), 400

# #         time.sleep(10)
# #         driver.close()

# #         return jsonify({"status": "success", "message": "Selenium test ran successfully!"})

# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500

# # if __name__ == "__main__":
# #     app.run()






# from flask import Flask, jsonify, request
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import time

# app = Flask(__name__)

# @app.route('/run-selenium', methods=['POST'])
# def run_selenium():
#     try:
#         # Parse JSON input from Postman request body
#         data = request.json
#         name = data.get('Name')
#         email = data.get('Email')
#         phone_number = data.get('Phone_Number')
#         age = data.get('Age')
#         gender = data.get('Gender')
#         city = data.get('City')
#         state = data.get('State')

#         # Initialize Selenium WebDriver
#         driver = webdriver.Chrome()

#         # Navigate to the form page
#         driver.get("https://transformers.prodt.co/test/")

#         # Wait for the page to fully load
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

#         # Fill the form
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "name")))
#         driver.find_element(By.NAME, "name").send_keys(name)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
#         driver.find_element(By.NAME, "email").send_keys(email)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "phone")))
#         driver.find_element(By.NAME, "phone").send_keys(phone_number)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "age")))
#         driver.find_element(By.NAME, "age").send_keys(str(age))

#         # Gender selection using the input field
#         gender_input = driver.find_element(By.ID, "gender")
#         gender_input.click()  # Click to activate the dropdown

#         if gender.lower() == 'male':
#             gender_input.send_keys("Male")
#         elif gender.lower() == 'female':
#             gender_input.send_keys("Female")

#         # Confirm the selection
#         gender_input.send_keys(Keys.RETURN)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "city")))
#         driver.find_element(By.NAME, "city").send_keys(city)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "state")))
#         driver.find_element(By.NAME, "state").send_keys(state)

#         # Submit the form
#         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
#         # Wait for the number to be present in the modal (adjust selector as needed)
#         # generated_number = WebDriverWait(modal, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "number-class")))  # Adjust based on actual number element class
#         # generated_number_text = generated_number.text  # Get the text (the number)

#         # Wait for the form to process
#         time.sleep(15)
#         driver.quit()

#         # Return success response with generated number
#         return jsonify({"status": "success", "message": "Form submitted successfully!", "generated_number": "generated_number_text"})

#     except Exception as e:
#         print(f"Error occurred: {str(e)}")
#         driver.quit()
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, jsonify, request
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import time

# app = Flask(__name__)

# @app.route('/run-selenium', methods=['POST'])
# def run_selenium():
#     try:
#         data = request.json
#         name = data.get('Name')
#         email = data.get('Email')
#         phone_number = data.get('Phone_Number')
#         age = data.get('Age')
#         gender = data.get('Gender')
#         city = data.get('City')
#         state = data.get('State')


#         driver = webdriver.Chrome()


#         driver.get("https://transformers.prodt.co/test/")

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "name")))
#         driver.find_element(By.NAME, "name").send_keys(name)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
#         driver.find_element(By.NAME, "email").send_keys(email)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "phone")))
#         driver.find_element(By.NAME, "phone").send_keys(phone_number)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "age")))
#         driver.find_element(By.NAME, "age").send_keys(str(age))


#         gender_input = driver.find_element(By.ID, "gender")
#         gender_input.click()  

#         if gender.lower() == 'male':
#             gender_input.send_keys("Male")
#         elif gender.lower() == 'female':
#             gender_input.send_keys("Female")


#         gender_input.send_keys(Keys.RETURN)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "city")))
#         driver.find_element(By.NAME, "city").send_keys(city)

#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "state")))
#         driver.find_element(By.NAME, "state").send_keys(state)

#         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()

#         lot_number_element = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.ID, "lot_number"))
#         )
#         lot_number_text = lot_number_element.text 

#         return jsonify({"status": "success", "message": "Form submitted successfully!", "lot_number": lot_number_text})

#     except Exception as e:
#         print(f"Error occurred: {str(e)}")
#         driver.quit()
#         return jsonify({"error": str(e)}), 500

#     finally:
#         time.sleep(15)
#         driver.quit()

# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re

app = Flask(__name__)

def get_browser_from_user_agent(user_agent):
    if "chrome" in user_agent.lower():
        return "chrome"
    elif "firefox" in user_agent.lower():
        return "firefox"
    elif "edg" in user_agent.lower():
        return "edge"
    elif "brave" in user_agent.lower():
        return "brave"
    else:
        return "chrome"

@app.route('/run-selenium', methods=['POST'])
def run_selenium():
    try:
        user_agent = request.headers.get('User-Agent', '')
        browser_choice = get_browser_from_user_agent(user_agent)

        data = request.json
        name = data.get('Name')
        email = data.get('Email')
        phone_number = data.get('Phone_Number')
        age = data.get('Age')
        gender = data.get('Gender')
        city = data.get('City')
        state = data.get('State')

        if browser_choice == 'chrome':
            driver = webdriver.Chrome()
        elif browser_choice == 'firefox':
            driver = webdriver.Firefox()
        elif browser_choice == 'edge':
            driver = webdriver.Edge()
        elif browser_choice == 'brave':
            brave_path = "/path/to/brave"
            options = webdriver.ChromeOptions()
            options.binary_location = brave_path
            driver = webdriver.Chrome(options=options)
        else:
            return jsonify({"error": "Unsupported browser specified"}), 400

        driver.get("https://transformers.prodt.co/test/")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "name")))
        driver.find_element(By.NAME, "name").send_keys(name)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        driver.find_element(By.NAME, "email").send_keys(email)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "phone")))
        driver.find_element(By.NAME, "phone").send_keys(phone_number)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "age")))
        driver.find_element(By.NAME, "age").send_keys(str(age))

        gender_input = driver.find_element(By.ID, "gender")
        gender_input.click()  

        if gender.lower() == 'male':
            gender_input.send_keys("Male")
        elif gender.lower() == 'female':
            gender_input.send_keys("Female")
        gender_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "city")))
        driver.find_element(By.NAME, "city").send_keys(city)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "state")))
        driver.find_element(By.NAME, "state").send_keys(state)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        lot_number_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "lot_number"))
        )
        lot_number_text = lot_number_element.text 

        return jsonify({"status": "success", "message": "Form submitted successfully!", "lot_number": lot_number_text})

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

    finally:
        time.sleep(15)
        driver.quit()

if __name__ == "__main__":
    app.run(debug=True)
