import shutil
import os
import subprocess
import keyboard

folder = "/files"

keyboard.add_hotkey("ctrl+alt+z", lambda: delete_folder(folder))
keyboard.wait()

def delete_folder(folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
        print(f"{folder} was successfully deleted")
        subprocess.run(["python", "2del.py"])
    else:
        print(f"{folder} does not exist")
