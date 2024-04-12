import os


class CommonSteps:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, filename="streamer_screenshot.png"):
        # Ensure dir exists
        screenshot_dir = "data/screenshot"
        os.makedirs(screenshot_dir, exist_ok=True)
        # Construct full file path
        file_path = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(file_path)
