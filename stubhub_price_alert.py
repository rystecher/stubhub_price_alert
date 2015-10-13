import requests
from twilio.rest import TwilioRestClient

# Stubhub globals #
STUBHUB_TOKEN = None # (String) Stubhub API token
EVENT_ID = None # (String) The event id of the show you want
PRICE = 0.0 # (Float) Your preferred price
TICKETSPLIT = 0 # (Integer) Your preferred quantity of tickets
NUM_LISTINGS = 0 # (Integer) Number of listings you want to check

# Twilio globals #
TWILIO_SID = None # (String) Twilio SID
TWILIO_TOKEN = None # (String) Twilio API token
TWILIO_NUMBER = None # (String) Twilio number
PERSONAL_NUMBER = None # (String) Your personal number


def check_price():
	""" Checks if the price of a ticket has fallen below the user's specified price.
	Returns None if no tickets were found, or a string with a link to the desired ticket. """

	results = None

	url = "https://api.stubhub.com/search/inventory/v1?eventid=" + EVENT_ID + "&pricingsummary=true";

	headers = {"Authorization": "Bearer {0}".format(STUBHUB_TOKEN),
				"content-type": "application/json"}

	r = requests.get(url, headers=headers).json()

	listings = r["listing"]

	# Get first NUM_LISTINGS listings:
	for i in range(NUM_LISTINGS):
		ticket_id = listings[i]["listingId"]
		price = listings[i]["currentPrice"]["amount"]
		ticketsplit = listings[i]["ticketSplit"]

		if (price <= PRICE) and (int(ticketsplit) == TICKETSPLIT):
			# Generate link to ticket
			results_url = "https://www.stubhub.com/buy/?ticket_id=" + str(ticket_id) + "&quantity_selected=" + ticketsplit + "&event_id=" + EVENT_ID
			results = "Hurry! the price is " + str(price) + " " + results_url
			break

	return results

def notify(results):
	""" Send a SMS message to a user via Twilio """
	account_sid = TWILIO_SID
	auth_token = TWILIO_TOKEN
	client = TwilioRestClient(account_sid, auth_token)

	message = client.messages.create(to=PERSONAL_NUMBER, 
									from_=TWILIO_NUMBER,
		                            body=results)

def main():
	results = check_price()
	if results != None:
		notify(results)

if __name__ == "__main__":
	main()
