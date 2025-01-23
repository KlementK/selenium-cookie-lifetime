# selenium-cookie-lifetime

This ~~project~~ script uses Selenium to interact with [Bing](https://www.bing.com/) and retrieve the lifetime of cookies set by the website.


## Installation Guide

Follow these steps to set up the project on your local machine:

### **1. Prerequisites**
- **Python**: Version 3.7 or higher.
- **Google Chrome Browser**: Ensure it's installed and up-to-date.
- **Matching ChromeDriver**:
  - Download the appropriate ChromeDriver for your Chrome version from [ChromeDriver Downloads](https://developer.chrome.com/docs/chromedriver/downloads).
  - Place the `chromedriver` executable in the `chromedriver/` folder of this repository.

---

### **2. Clone the Repository**
Clone this repository to your local machine.


### **3. Set Up a Virtual Environment**
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```


### **4. Install Dependencies**
Install the required Python packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```


### **5. Add ChromeDriver**
Move the `chromedriver` executable to the `chromedriver/` folder.


### **6. Run the Script**
Run the script to retrieve and display cookie lifetime details:
```bash
python get_cookie_lifetime.py
```


## License
This project is licensed under the MIT License.
