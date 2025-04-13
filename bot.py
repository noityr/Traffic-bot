
import time, random, requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

URL = "https://your-website.com"  # TODO: Change this to your real website URL

PROXY_LIST_URL = "https://www.proxy-list.download/api/v1/get?type=https"

def get_random_proxy():
    try:
        proxies = requests.get(PROXY_LIST_URL, timeout=10).text.splitlines()
        if proxies:
            return random.choice(proxies)
    except Exception as e:
        print("Failed to get proxy:", e)
    return None

def run_bot():
    proxy = get_random_proxy()
    options = uc.ChromeOptions()
    user_agent = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (Linux; Android 11)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ])
    options.add_argument(f"user-agent={user_agent}")
    if proxy:
        options.add_argument(f'--proxy-server=https://{proxy}')
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    try:
        print(f"Using proxy: {proxy}")
        driver = uc.Chrome(options=options)
        driver.set_page_load_timeout(30)
        driver.get(URL)
        print("Page loaded:", URL)

        time.sleep(random.randint(5, 10))
        driver.execute_script("window.scrollBy(0, window.innerHeight / 2);")
        time.sleep(random.randint(3, 6))

        # Try to click something if possible
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
        print("Session complete. Browser closed.")
    except Exception as e:
        print("Bot run error:", e)

# Run multiple sessions per execution
for i in range(4):  # Adjust this number for more/less bots
    print(f"--- Starting bot #{i+1} ---")
    run_bot()
