from functions import *

load_dotenv()

devices = load_json('devices')
print("Getting Screenshots...")
for device in devices:
   print(f"Getting screenshot for {device['name']}")
   get_screenshots(device)
   print(f"Screenshot saved as {device['name']}.png")
print("")

people = json.loads(os.getenv('DEV'))

print("Sending emails...")
for person in people:
   print(f"Sending {person['device']}.png to {person['email']}")
   send_email(person)
   print(f"Email sent!")
print("")

print("Process complete!")