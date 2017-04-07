""" Example of API requesting and JSON parsing using ISS data.

Source: https://www.dataquest.io/blog/python-api-tutorial/

API Docs: http://open-notify.org/Open-Notify-API/

"""

import requests

def get_iss_now():
    """ Request and print the current status of the ISS.

    """
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print response.status_code
    print response.content

def get_iss_somewhere(parameters):
    """ Request and print ISS data at certain location.

    Input: dictionary with lat and lon keys

    Output: API Response
    """
    response = requests.get("http://api.open-notify.org/iss-pass.json", parameters)

    print response.status_code
    # Decode just formats the string
    print response.content.decode("utf-8")

    return response

def get_iss_astros():
    """ Request astronauts on the ISS.

    Print the number of astraunauts on ISS and then their Names

    API Endpoint: "http://api.open-notify.org/astros.json"

    Exercise:

    print the astronauts names and other stuff about them

    """
    response = requests.get("http://api.open-notify.org/astros.json")

    json = response.json()

    print 'Number of austronauts: {0}'.format(json['number'])

    people = json['people']

    for person in people:
        print person['name']


if __name__ == '__main__':
    # get_iss_now()
    get_iss_astros()

    # ny_coordinates = {"lat": 40.71, "lon": -74}
    #
    # somewhere_data = get_iss_somewhere(ny_coordinates)
    #
    # somewhere_json = somewhere_data.json()
    #
    # print somewhere_data
    # print somewhere_json['response']
    #
    # data_headers = somewhere_data.headers
    #
    # print data_headers
    # print data_headers['content-type']
    #
