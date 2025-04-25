import pyautogui
import webbrowser
import os
from speech import speak, listen

def handle_action(action):
    action = action.lower()

    # Web Apps
import time  # Importing time for adding delays

def handle_action(action):
    action = action.lower()

    import pyautogui
import webbrowser
import time
from speech import speak, listen  # Assuming 'speak' and 'listen' are your custom functions for text-to-speech and speech recognition

def handle_action(action):
    action = action.lower()

   # Web Apps
    if "open youtube" in action or "youtube" in action:
        # Ask for the search query before opening YouTube
        speak("What would you like to search for on YouTube?")
        
        # Listen to the user's input for the search query
        search_query = listen()
        
        if search_query:
            speak(f"Opening YouTube and searching for {search_query}.")
            
            # Open YouTube in the browser
            webbrowser.open("https://www.youtube.com")
            
            # Wait for the page to load (adjust time if needed)
            time.sleep(5)
            
            # Focus on the YouTube search bar (coordinates might need adjustment based on your screen)
            pyautogui.click(x=800, y=300)
            time.sleep(1)  # Wait for a second to make sure the search bar is active
            
            # Type the search query and press enter
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")


    elif "open facebook" in action or "facebook" in action:
        speak("What would you like to search for on Facebook?")
        search_query = listen()
        if search_query:
            speak(f"Opening Facebook and searching for {search_query}.")
            webbrowser.open("https://www.facebook.com")
            time.sleep(5)
            pyautogui.click(x=500, y=200)  # Adjust this based on the actual search bar location
            time.sleep(1)
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")
    
    elif "open instagram" in action or "instagram" in action:
        speak("Opening Instagram. What would you like to search for?")
        webbrowser.open("https://www.instagram.com")
        search_query = listen()
        if search_query:
            speak(f"Searching for {search_query} on Instagram.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open spotify" in action or "spotify" in action:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")

        
        # Wait for the page to load
        time.sleep(3)
        
        # Focus on the search bar or use keyboard shortcuts if applicable
        pyautogui.click(x=800, y=300)  # Adjust the coordinates as needed

        search_query = listen()  # Capture the search query
        if search_query:
            speak(f"Searching for {search_query} on Spotify.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")


    elif "open twitter" in action or "twitter" in action:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
        search_query=listen()
        if search_query:
            speak(f"Searching for {search_query} on Twitter.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open linkedin" in action or "linkedin" in action:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        search_query=listen()
        if search_query:
            speak(f"Searching for {search_query} on LinkedIn.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open reddit" in action or "reddit" in action:
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")
        search_query=listen()
        if search_query:
            speak(f"Searching for {search_query} on Reddit.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open gmail" in action or "gmail" in action:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
        search_query=listen()
        if search_query:
            speak(f"Searching for {search_query} on Gmail.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open drive" in action or "drive" in action:
        speak("Opening Google Drive")
        webbrowser.open("https://drive.google.com")
        search_query=listen()
        if search_query:
            speak(f"Searching for {search_query} on Google Drive.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open github" in action or "github" in action:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
        search_query=listen()
        if search_query:
            speak(f"Searching for {search_query} on GitHub.")
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")
    
    # System Apps
    # Notepad
    if "open notepad" in action or "notepad" in action:
        speak("Notepad is opening now.")
        os.system("notepad")

        speak("Would you like to write in Notepad? Please say yes or no.")
        user_response = listen()

        # if user_response=="yes" or user_response=="y":
        if user_response and "yes" in user_response.lower() or user_response and "y" in user_response.lower():
            speak("Okay, I will start writing. Please speak what you'd like to write. Say 'stop' when you're done.")
            
            while True:
                # Listen to what the user wants to write
                text_to_write = listen()

                if text_to_write:
                    if "stop" in text_to_write.lower():
                        speak("Okay, stopping writing. What would you like to do next?")
                        break
                    else:
                        # Write the spoken text in Notepad
                        pyautogui.write(text_to_write)
                        pyautogui.press('enter')  # Simulate pressing 'Enter' to start a new line
                else:
                    speak("I couldn't hear anything. Please speak clearly.")
                    continue

        elif user_response and "no" in user_response.lower():
            speak("Notepad is open. What would you like to do next?")
        else:
            speak("I couldn't understand. Notepad is open. What would you like to do next?")


    elif "open calculator" in action or "calculator" in action:
        speak("Opening Calculator")
        os.system("calc")
        text_to_write=listen()
        if text_to_write:
            pyautogui.write(text_to_write)
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open word" in action or "word" in action:
        speak("Opening Word")
        os.system("start winword")
        text_to_write=listen()
        if text_to_write:
            pyautogui.write(text_to_write)
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open excel" in action or "excel" in action:
        speak("Opening Excel")
        os.system("start excel")
        text_to_write=listen()
        if text_to_write:
            pyautogui.write(text_to_write)
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open powerpoint" in action or "powerpoint" in action:
        speak("Opening PowerPoint")
        os.system("start powerpnt")
        text_to_write=listen()
        if text_to_write:
            pyautogui.write(text_to_write)
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open chrome" in action or "chrome" in action:
        speak("What would you like to search for on Google?")
        search_query = listen()
        if search_query:
            speak(f"Opening Chrome and searching for {search_query}.")
            webbrowser.open("https://www.google.com")
            time.sleep(3)
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open edge" in action or "edge" in action:
        speak("Opening Edge")
        os.system("start msedge")
        text_to_write=listen()
        if text_to_write:
            pyautogui.write(text_to_write)
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open vlc" in action or "vlc" in action:
        speak("Opening VLC Media Player")
        os.system("start vlc")
        text_to_write=listen()
        if text_to_write:
            pyautogui.write(text_to_write)
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open steam" in action or "steam" in action:
        speak("Opening Steam")
        os.system("start steam")
        text_to_write=listen()
        if text_to_write:
            pyautogui.write(text_to_write)
        else:
            speak("No input detected. Waiting for your next command.")

    # File Explorer / Folder Operations
    # File Explorer
    elif "open file explorer" in action or "file explorer" in action:
        speak("What would you like to open in File Explorer?")
        os.system("explorer")
        search_query = listen()
        if search_query:
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")
    elif "open documents" in action or "documents" in action:
        speak("Opening Documents")
        os.system("explorer shell:::{FDD39EFC-8B47-11D9-A6A1-000D56A64B4F}")
        search_query = listen()
        if search_query:
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open downloads" in action or "downloads" in action:
        speak("Opening Downloads")
        os.system("explorer shell:::{374DE290-123F-4565-9164-39C4925E467B}")
        search_query = listen()
        if search_query:
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    elif "open pictures" in action or "pictures" in action:
        speak("Opening Pictures")
        os.system("explorer shell:::{3ADD1653-EB32-4CB0-BBD7-DFA0ABB5ACCA}")
        search_query = listen()
        if search_query:
            pyautogui.write(search_query)
            pyautogui.press('enter')
        else:
            speak("No input detected. Waiting for your next command.")

    # Opening System Utilities (Control Panel, Task Manager, etc.)
    elif "open control panel" in action or "control panel" in action:
        speak("Opening Control Panel. What would you like to adjust?")
        os.system("control")
        adjustment = listen()
        if adjustment:
            speak(f"Making adjustment: {adjustment}.")
            pyautogui.write(adjustment)
        else:
            speak("No input detected. Waiting for your next command.")
   # Task Manager
    elif "open task manager" in action or "task manager" in action:
        speak("Opening Task Manager")
        os.system("taskmgr")
        adjustment = listen()
        if adjustment:
            speak(f"Making adjustment: {adjustment}.")
            pyautogui.write(adjustment)
        else:
            speak("No input detected. Waiting for your next command.")

     # CMD (Command Prompt)
    elif "open cmd" in action or "cmd" in action:
        speak("Opening Command Prompt")
        os.system("cmd")
        adjustment = listen()
        if adjustment:
            speak(f"Making adjustment: {adjustment}.")
            pyautogui.write(adjustment)
        else:
            speak("No input detected. Waiting for your next command.")
            
    # Settings
    elif "open settings" in action or "settings" in action:
        speak("Opening Settings")
        os.system("start ms-settings:")
        adjustment = listen()
        if adjustment:
            speak(f"Making adjustment: {adjustment}.")
            pyautogui.write(adjustment)
        else:
            speak("No input detected. Waiting for your next command.")
            
    elif "open taskbar" in action or "taskbar" in action:
        speak("Toggling Taskbar visibility")
        pyautogui.hotkey("win", "d")  # Minimizing windows (example for showing taskbar)
        adjustment = listen()
        if adjustment:
            speak(f"Making adjustment: {adjustment}.")
            pyautogui.write(adjustment)
        else:
            speak("No input detected. Waiting for your next command.")
    

    # Other apps
    elif "open skype" in action or "skype" in action:
        speak("Opening Skype")
        os.system("start skype")
    elif "open discord" in action or "discord" in action:
        speak("Opening Discord")
        os.system("start discord")
    elif "open zoom" in action or "zoom" in action:
        speak("Opening Zoom")
        os.system("start zoom")
    elif "open teams" in action or "teams" in action:
        speak("Opening Microsoft Teams")
        os.system("start teams")
    elif "open slack" in action or "slack" in action:
        speak("Opening Slack")
        os.system("start slack")
    
    # Specific Folders/Shortcuts (Example: Desktop)
    elif "open desktop" in action or "desktop" in action:
        speak("Opening Desktop")
        os.system("explorer shell:::{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}")
    
    else:
        print("No predefined action found.")
