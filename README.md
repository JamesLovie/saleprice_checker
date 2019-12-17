# saleprice_checker
Checks the price of any item on Temple &amp; Webster website and returns either null or a message to Slack if there is a change in the price.

Created a lambda function to run daily and send a text message when the price of the item changes.

1. Created a lambda function with basic permissions.
2. Inserted python code from Github.
3. Included json library, inserted all code under lambda handler function.
4. Add environment variable for my phone number to send SMS, including item price to check against and the target url.
5. Created a virtual environment on local machine, installed custom libraries, zip contents of virtual environment installed libraries  and uploaded zip file to lambda (zip -r9 saleprice_checker.zip *).
6. Attached SNS Full Access policy to lambda function to allow the function to access SNS to send a message.
7. Created a scheduled rule in Cloudwatch to trigger lambda function every day. (Schedule	Cron expression 0 12 * * ? *)
