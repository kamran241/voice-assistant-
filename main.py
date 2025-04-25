from speech import listen, speak
from brain_pro import get_response
from control import handle_action

def main():
    speak("Hello mate, Jarvis is online. Ready for your commands!")

    while True:
        command = listen()
        if not command:
            continue

        command = command.lower()

        if command in ["exit", "quit", "shutdown"]:
            speak("Goodbye mate, powering down.")
            break

        # Get smart AI reply + check if it includes any action
        response, action = get_response(command)
        speak(response)

        if action:
            handle_action(action)  # Perform the action (like opening apps)
            
            # After executing an action, ask for further instructions (whether to continue or stop)
            speak("What would you like to do next?")
            follow_up_command = listen()
            if follow_up_command:
                handle_action(follow_up_command)  # Continue with the next action
            else:
                speak("No input detected. Waiting for your next command.")
                
        else:
            speak("No action detected. Please tell me what to do next.")

if __name__ == "__main__":
    main()

    