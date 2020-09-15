#!/usr/local/bin/python3

import json
import requests

url = "https://api.chucknorris.io/jokes/random"
payload = {}
headers = {
  'Cookie': '__cfduid=dd34713313402996c546c6b774b957eb01600033165'
}
def get_chuck_joke(api):
    """
    Get a random joke from the Chuck Norris API and return the serial JSON
    :param api:
    :return:serial JSON
    """
    #  TASK 1 - use requests to get a joke.
    response = requests.request("GET", url, headers=headers, data = payload)
       #  TASK 2 - return the response in JSON format
   # print(response.json())
    return  response.json()
    

if __name__ == '__main__':
    #  TASK 3 - correct the json statement
    joke_output = get_chuck_joke(url)
    #  TASK 4 - print just a joke without any superfluous symbols
    print(joke_output['value'])  
