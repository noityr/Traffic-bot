import time, random, requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

URL = "https://your-website.com"  # <- CHANGE THIS

PROXY_LIST_URL = "https://www.proxy-list.download/api/v1/get?type=https"

def get_random_proxy():
    try:
        proxies = requests.get(PROXY_LIST_URL).text.splitlines()
        return random.choice(proxies)
    except:
        return None

def run_bot():
    proxy = get_random_proxy()
    options = uc.ChromeOptions()
    user_agent = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        "Mozilla/5.0 (Linux; Android 11)...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)..."
    ])
    options.add_argument(f"user-agent={user_agent}")
    if proxy:
        options.add_argument(f'--proxy-server=https://{proxy}')
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")

    try:
        driver = uc.Chrome(options=options)
        driver.get(URL)
        time.sleep(random.randint(5, 10))
        driver.execute_script("window.scrollBy(0, window.innerHeight / 2);")
        time.sleep(random.randint(5, 10))
        try:
            btn = driver.find_element(By.TAG_NAME, "button")
            btn.click()
        except:
            pass
        time.sleep(random.randint(40, 65))
        driver.quit()
    except Exception as e:
        print("Error:", e)

# Run 4 bots in parallel
for _ in range(4):
    run_bot()
