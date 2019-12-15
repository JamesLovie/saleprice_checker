# saleprice_checker
Checks the price of any item on Temple &amp; Webster website and returns either null or a message to Slack if there is a change in the price.

Created a lambda function to run daily and send a text message when the price of the item changes.

1. Created a lambda function with basic permissions.
2. Inserted python code from Github.
3. Included json library, passed in event and handler objects and a “send 200” upon successfully running the main() function. This will populate Cloudwatch Logs.
4. Add environment variable for my phone number to send SMS.
5. Created a virtual environment on local machine, installed custom libraries, zip’d up folder and uploaded to lambda.
6. Zip contents of virtual environment installed libraries (zip -r9 saleprice_checker.zip *)
7. Attached SNS Full Access policy to lambda function to allow the function to access SNS to send a message.
8. Created a scheduled rule in Cloudwatch to trigger lambda function every day.
