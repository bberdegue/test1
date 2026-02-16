import csv
import requests

API_KEY = 'YOUR_GOOGLE_PLACES_API_KEY'

def check_google_business(listings_file):
    with open(listings_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            restaurant_name = row[0]
            address = row[1]
            search_query = f"{restaurant_name}, {address}"
            url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={search_query}&inputtype=textquery&fields=place_id,name&key={{API_KEY}}"
            response = requests.get(url)
            result = response.json()
            if result.get('candidates'):
                print(f"{restaurant_name} has a Google Business listing.")
            else:
                print(f"{restaurant_name} does not have a Google Business listing.")

if __name__ == '__main__':
    check_google_business('listings.csv')
