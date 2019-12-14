# James Lovie 2019
# Website Sale Price Checker
# Checks the price of any item on Temple & Webster website and returns either null or a message to Slack if there is a change in the price.

# Beautiful soup parses HTML.
# Requests library for HTML requests.
# Import slack api library.
# Import slack api key from local machine.
from bs4 import BeautifulSoup
import requests
from slacker import Slacker
import slack_api_constants

# Class names should follow the UpperCaseCamelCase convention.
class SlackAPI:
    def __init__(self, slacktoken=None):
        self.slacktoken = slacktoken
	# Constructor: Method names should be all lower case.
    def request_connection(self):
    	self.slacktoken = Slacker(slack_api_constants.API_KEY_SERVICE)

# Class names should follow the UpperCaseCamelCase convention.
class PriceChecker:

	def __init__(self, url):
            self.url = url
	# Constructor: Method names should be all lower case.
	def checkprice(self):
		# URL to pull HTML from.
		page_link = self.url
		# Get the HTML from the specified URL.
		page_response = requests.get(page_link, timeout=5)
		# Set up HTML parser to use beautiful soup.
		page_content = BeautifulSoup(page_response.content, "html.parser")
		# Make the HTML 'utf-8'.
		html = page_content.prettify("utf-8")
		# Set the soup variable to html in bs4.
		soup = BeautifulSoup(html, "html.parser")
		# Extract the tag that contains the price.
		price_box = soup.find('div', attrs={"class":"dynamic_sku_price"})
		# Extract only text, aka remove tags.
		price = price_box.text
		# Remove the whitespaces from the text.
		price = price.replace(' ', '')
		# Remove additional lines in the string that are not needed.
		postPrice = price.split("\n",2)[2];
		postPrice = price.replace("\r","")
		postPrice = price.replace("\n","")
		# Remove the cash symbol from the string.
		postPrice = postPrice[1:4]
		# Convert the string to an integer for comparison.
		int(postPrice)
		return postPrice

def main():
	apicall = SlackAPI()
	pricecheck = PriceChecker('https://www.templeandwebster.com.au/Tan-Brahm-3-Seater-Premium-Faux-Leather-Sofa-FRBRSFTN-TMPL1923.html')
	apicall.request_connection()
	postPrice = pricecheck.checkprice()

	if postPrice == '999':
		# Failed, do not notify on Slack.
		print('No price change')
	elif postPrice < '999':
		# Print sucess to Slack.
		slack.chat.post_message('#general', 'Price has decreased!')
	elif postPrice > '999':
		# Print sucess to Slack.
		slack.chat.post_message('#general', 'Price has increased!')

if __name__ == '__main__':
	main()
