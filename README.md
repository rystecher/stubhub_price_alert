# Stubhub Price Alert
Get a text notification when an event you want to attend reaches a certain price on Stubhub! This script will check Stubhub for a ticket at a price you specify, and if it finds one, sends you a text message linking you directly to that ticket.

# Dependancies
To install dependencies run: <code>pip install -r requirements.txt</code>

You will also need an API token from <a href="https://developer.stubhub.com/store/site/pages/guides.jag?type=gettingstarted" >Stubhub</a> and <a href="https://www.twilio.com/help/faq/twilio-basics/what-is-the-auth-token-and-how-can-i-change-it">Twilio</a>.

Then run the program as a simple python script: <code>python stubhub_price_alert.py</code>

# Usage
First, fill out all the globals at the top of the file. This includes your API tokens, price, phone numbers (Twilio's and your own), etc.

You'll need to know the event id of the Stubhub event which can be found in the URL of the event:

![event id in url](url.png)

After you have all of the global fields filled out you're ready to go! I personally wanted to run this script to check Stubhub every 10 minutes so I ran this script as a cron job (which you read about <a href="http://askubuntu.com/questions/2368/how-do-i-set-up-a-cron-job">here</a>.)

Here's my experience using the script:

Receiving the text:

![Text message](text.jpg)

Tickets arrive:

![Tickets](tickets.jpg)

Take that scalpers