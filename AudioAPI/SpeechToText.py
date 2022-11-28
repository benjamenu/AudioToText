import requests
import time


class AudioAPI:
    # This attribute is the endpoint for the RESTful API service.
    endpoint = "https://api.assemblyai.com/v2/transcript"

    # The audio_url and api_key are passed from user input
    # in the main method.
    def __init__(self, audio_url: str, api_key: str):
        self.audio_url = audio_url
        self.api_key = api_key

    """Return a String
    
    This method will send the provided audio url to the API
    and will extract and return the ID of the GET request.
    """
    def SendGetRequests(self) -> str:
        json = {
            "audio_url": self.audio_url
        }
        headers = {
            "authorization": self.api_key,
            "content-type": "application/json"
        }
        response = requests.post(self.endpoint, json=json, headers=headers)
        return response.json()['id']

    """
    This method will connect to the API with the endpoint
    and the id provided from the SendGetRequest method.
    The text is then extracted from the json and printed.
    """
    def SendPostRequest(self, id: str):
        url = self.endpoint + "/" + id
        headers = {
            "authorization": self.api_key
        }

        while True:
            response = requests.get(url, headers=headers)
            status = response.json()['status']
            print(status)
            if status == "completed" or status == "error":
                break

        print(response.json()['text'])
        time.sleep(1)


def main():
    url = str(input("URL of Audio File: "))
    api_key = str(input("Your API Key: "))
    a1 = AudioAPI(url, api_key)
    id = a1.SendGetRequests()
    a1.SendPostRequest(id)


if __name__ == "__main__":
    main()
