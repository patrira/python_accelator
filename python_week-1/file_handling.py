import json
import datetime

data = {"name": "Patrick", "role": "Python Developer"}


with open("data.json", "w") as file:
    json.dump(data, file)


with open("data.json", "r") as file:
    loaded = json.load(file)

print("Loaded JSON:", loaded)


def log_user_action(username, action):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] {username}: {action}\n"

    with open("user_logs.txt", "a") as log_file:
        log_file.write(log_entry)



print(log_user_action("patrick", "Logged in"))
print(log_user_action("patrick", "Started watching 'Python for Pros'"))
