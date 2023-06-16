import requests
from datetime import datetime
import pytz

def to_pst(ts):
	try:
		dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%f%z")

		# Convert the datetime object to PST timezone
		pst = pytz.timezone('America/Los_Angeles')
		pst_dt = dt.astimezone(pst)

		# Format the PST datetime as a string
		pst_timestamp = pst_dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
		return pst_timestamp[0:16]
	except Exception:
		return "Time fetch error"
	
# TODO: FILL THESE OUT
CHANNEL_ID = 0
AUTHORIZATION = ""

URL = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=100"

headers = {
	'Authorization': AUTHORIZATION,
}

all_messages = []
has_more_messages = True

while has_more_messages:
	response = requests.get(URL, headers=headers)
	data = response.json()

	if len(data) > 0:
		all_messages.extend(data)
		last_message_id = data[-1]["id"]
		URL = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=100&before={last_message_id}"
	else:
		has_more_messages = False

all_messages.reverse()

for message in all_messages:
	print(f'{message["author"]["global_name"]} | {to_pst(message["timestamp"])}', end="")
	if message["content"] != "":
		print(f' | {message["content"]}')
	else:
		print()
	for attachment in message['attachments']:
		print(attachment["url"])