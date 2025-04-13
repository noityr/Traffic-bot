
import time, random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

URL = "https://www.chachi.fun/"  # TODO: Change this to your actual site

def run_bot():
    options = uc.ChromeOptions()
    user_agent = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (Linux; Android 11)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ])
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    try:
        print("Starting browser...")
        driver = uc.Chrome(options=options)
        driver.set_page_load_timeout(30)
        driver.get(URL)
        print("Page loaded:", URL)

        time.sleep(random.randint(5, 10))
        driver.execute_script("window.scrollBy(0, window.innerHeight / 2);")
        time.sleep(random.randint(3, 6))

        try:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            if buttons:
                random.choice(buttons).click()
                print("Clicked a button.")
        except Exception as e:
            print("No clickable button found or click failed.")

        stay_time = random.randint(40, 65)
        print(f"Staying on page for {stay_time} seconds...")
        time.sleep(stay_time)
        driver.quit()
        print("Session complete.")
    except Exception as e:
        print("Bot run error:", e)

for i in range(4):  # You can change this number
    print(f"--- Running bot #{i+1} ---")
    run_bot()
