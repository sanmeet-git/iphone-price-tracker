import os
from playwright.sync_api import sync_playwright

# Ignore the bad system path
os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)

def run():
    print("🤖 Robot starting (Sanity Check)...")
    
    with sync_playwright() as p:
        print("🚀 Launching browser...")
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-gpu"
            ]
        )
        page = browser.new_page()

        # Target: A lightweight practice site
        print("🌐 Visiting 'Books to Scrape'...")
        try:
            page.goto("http://books.toscrape.com/", timeout=30000)
            print("✅ Page loaded!")
        except Exception as e:
            print(f"❌ Failed: {e}")
            browser.close()
            return

        # 📸 SNAPSHOT!
        page.screenshot(path="evidence.png")
        print("📸 Screenshot taken!")

        # Find book titles
        # The selector for titles on this site is 'h3 a'
        titles = page.locator("h3 a").all_inner_texts()
        
        print(f"👀 Found {len(titles)} books.")
        
        if len(titles) > 0:
            print("📝 First 3 results:")
            for i in range(min(3, len(titles))):
                print(f" - {titles[i]}")
        
        browser.close()
        print("✅ Mission Complete.")

if __name__ == "__main__":
    run()