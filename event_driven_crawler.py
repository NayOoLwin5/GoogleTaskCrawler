import uiautomator2 as u2
from uiautomator2 import UiObjectNotFoundError, ConnectError
import time
d = None
google_task = "com.google.android.apps.tasks"

def event_driven_task():
    global d
    try:
        d = u2.connect("e8fbb12d")
    except ConnectError as e:
        print(f"Failed to connect to device: {e}")
        return

    try:
        d.app_start(google_task)
        print("App started.")
        time.sleep(5)
    except UiObjectNotFoundError:
        print(f"Failed to start {google_task}. App might not be installed.")
        return

    placeholder_text = "Enter list title"
    text_field = d.xpath(f'//android.widget.EditText[@text="{placeholder_text}"]')
    
    while True:
        if text_field.exists:
            print("Text field found. Clicking...")
            try:
                text_field.click()
                d.send_keys("some random title")
                time.sleep(5)
                print("Event-driven task completed.")
                break
            except UiObjectNotFoundError:
                print("Failed to interact with text field. Retrying...")

    try:
        d.app_stop(google_task)
    except Exception as e:
        print(f"Error stopping the app: {e}")

try:
    event_driven_task()
except Exception as e:
    print(f"Unexpected error occurred: {e}")
finally:
    if d:
        d.app_stop(google_task)