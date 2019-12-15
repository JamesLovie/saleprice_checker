import json
from bs4 import BeautifulSoup
import requests
import boto3
import os

def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = os.environ['topic_arn']
    number = os.environ['phonenumber']
    url = os.environ['url']
    itemprice = os.environ['itemprice']
    page_link = url
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    html = page_content.prettify("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    price_box = soup.find('div', attrs={"class":"dynamic_sku_price"})
    price = price_box.text
    price = price.replace(' ', '')
    postPrice = price.split("\n",2)[2];
    postPrice = price.replace("\r","")
    postPrice = price.replace("\n","")
    postPrice = postPrice[1:4]
    int(postPrice)
    if postPrice == itemprice:
        print('No price change')
        return {
        'statusCode': 200,
        'body': json.dumps('Code ran sucessfully, no price changes.')
    }
    elif postPrice < itemprice:
        sns.publish(PhoneNumber=number, Message='Price has decreased!')
        return {
        'statusCode': 200,
        'body': json.dumps('Code ran sucessfully, price has decreased.')
    }
    elif postPrice > itemprice:
        sns.publish(PhoneNumber=number, Message='Price has increased!')
        return {
        'statusCode': 200,
        'body': json.dumps('Code ran sucessfully, price has increased.')
    }
