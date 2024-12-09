from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timezone

# Set the WebDriver path and target URL
driver_path = "./chromedriver/chromedriver.exe"
url = "https://www.bing.com/"

# Initialize WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get(url)

# Retrieve and display cookies
cookies = driver.get_cookies()

print("\nCookie Lifetime Details:")
print(f"{'Cookie Name':<20} {'Expiry (UNIX)':<15} {'Expiry (Readable)':<25}")
print("-" * 60)

for cookie in cookies:
    name = cookie.get('name')
    expiry = cookie.get('expiry')  # UNIX timestamp
    readable_expiry = (
        datetime.fromtimestamp(expiry, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        if expiry else "Session"
    )
    print(f"{name:<20} {str(expiry) if expiry else 'N/A':<15} {readable_expiry:<25}")

# Close the browser
driver.quit()
