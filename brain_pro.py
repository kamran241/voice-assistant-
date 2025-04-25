import requests
from config import XER0BIT_API_KEY

# Memory structure with tagging
context_memory = []

# Predefined actions (direct commands)
action_keywords = [
    "open youtube", "open facebook", "open instagram", "open spotify", "play music", "open vs code",
    "open notepad", "open calculator", "open chrome", "open edge", "open vlc", "open word",
    "open powerpoint", "open excel", "open telegram", "open skype", "open whatsapp", "open steam",
    "open discord", "open minecraft", "open spotify", "open spotify web", "open twitch", "open reddit",
    "open linkedin", "open gmail", "open drive", "open twitter", "open github", "open docker", "open slack",
    "open zoom", "open teams", "open spotify desktop", "open music", "open spotify app", "open file explorer",
    "open folder", "open documents", "open pictures", "open downloads", "open my computer", "open task manager",
    "open control panel", "open taskbar", "open cmd", "open settings", "open desktop"
]

def is_follow_up(user_query):
    follow_up_words = ["he", "she", "it", "they", "where", "when", "how", "what about", "tell me more", "explain", "describe", "who is"]
    return any(user_query.lower().startswith(word) for word in follow_up_words)

def get_response(user_query):
    url = "https://bitchat.xer0bit.com/api/v1/generate"
    headers = {
        'accept': 'application/json',
        'X-API-Key': XER0BIT_API_KEY,
        'Content-Type': 'application/json'
    }

    # Check if it is a follow-up question
    follow_up = is_follow_up(user_query)

    # Add current query to memory
    context_memory.append(f"User: {user_query}")

    # Trim memory if it exceeds 5 interactions
    if len(context_memory) > 5:
        context_memory.pop(0)

    # Use full memory for follow-up, otherwise reset memory for new questions
    if follow_up:
        memory_context = "\n".join(context_memory)
    else:
        memory_context = f"User: {user_query}"

    # If user asked for an action (e.g., open YouTube), skip the response generation
    action = None
    for keyword in action_keywords:
        if keyword in user_query.lower():
            action = keyword.lower()
            break  # Exit the loop once we find the matching action

    # If action found, return the action for handling
    if action:
        return "", action

    # Construct the prompt for Jarvis (AI model) if no action
    prompt = (
        "Jarvis is an intelligent assistant. Answer each question in one sentence.\n"
        "Avoid examples or explanations unless asked. Just be clear and direct.\n"
        f"{memory_context}\nJarvis:"
    )

    data = {
        "model": "smollm:135m",
        "prompt": prompt
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # Debugging: Print the raw response
        print("Xer0bit response:", result)

        message = result.get('message', {}).get('content', 'Sorry mate, I couldn’t get a reply.')
        reply = message.split('.')[0] + '.'  # Keep only the first sentence

        # Save assistant's reply to memory
        context_memory.append(f"Jarvis: {reply}")

        return reply.strip(), None

    except Exception as e:
        print("API Error:", e)
        return "Sorry mate, something went wrong in my brain.", None
