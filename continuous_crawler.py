import uiautomator2 as u2
from uiautomator2.exceptions import UiObjectNotFoundError
import time
import random

d = u2.connect("e8fbb12d")

google_task = "com.google.android.apps.tasks"

def print_all_tasks_batch():
    while True:
        printed_items = set()
        d.app_start(google_task)
        time.sleep(5)

        while True:
            tasks = d(resourceId="com.google.android.apps.tasks:id/task_name")
            for task in tasks:
                task_text = task.info['text']
                if task_text not in printed_items:
                    print(task_text)
                    printed_items.add(task_text)

            previous_tasks = d(resourceId="com.google.android.apps.tasks:id/task_name").info

            d(scrollable=True).scroll.vert.forward(steps=10)

            try:
                d(resourceId="com.google.android.apps.tasks:id/task_name").wait(timeout=10)
            except UiObjectNotFoundError:
                break

            current_tasks = d(resourceId="com.google.android.apps.tasks:id/task_name").info
            if previous_tasks == current_tasks:
                break

        d.app_stop(google_task)
        print("No more items to print. Stopping the application.")
        
        # Wait between 10-20 seconds before repeating
        time.sleep(random.randint(10, 20))

def print_all_tasks_sequential():
    while True:
        printed_items = set()
        d.app_start(google_task)
        time.sleep(5)

        while True:
            try:
                task = d(resourceId="com.google.android.apps.tasks:id/task_name")
                task_text = task.info['text']
                if task_text not in printed_items:
                    print(task_text)
                    printed_items.add(task_text)
                
                previous_tasks = d(resourceId="com.google.android.apps.tasks:id/task_name").info
                d.swipe(500, 800, 500, 600, 1.0)  

                current_tasks = d(resourceId="com.google.android.apps.tasks:id/task_name").info
                if previous_tasks == current_tasks:
                    d.app_stop(google_task)
                    break
            except UiObjectNotFoundError: 
                d.app_stop(google_task)
                break

        d.app_stop(google_task)
        print("No more items to print. Stopping the application.")
        
        # Wait between 10-20 seconds before repeating
        time.sleep(random.randint(10, 20))

# Call the desired function
# print_all_tasks_sequential()
# or
print_all_tasks_batch()