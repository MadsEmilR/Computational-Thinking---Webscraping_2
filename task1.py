import requests # Import requests library to send get requests
import json # Import json library to parse JSON files to Python

url = "https://www.scrapethissite.com/pages/ajax-javascript" # Set URL to the hidden API
payload = "" # Define empty payload (no payload is needed for the get request (this could also be deleted here and in line 11))

movies = [] # Create empty list to store all movies
 
for year in range(2010, 2016): # Iterate over the available years on the website
    querystring = {"ajax":"true","year":f"{year}"} # Define the query string (parameters to send to the hidden API)
    response = requests.get(url, data=payload, params=querystring) # Get the response of the API
    data = json.loads(response.text) # Parse the response from JSON to a list of dictionaries in Python
    movies += data # Add the movies of the given year to the list that stores all movies

# Print the results
print('Title\tYear\tAwards\tNominations\tBest Picture'.expandtabs(30))
for movie in movies:
    if 'best_picture' in movie.keys():
        print(f"{movie['title'][:15]}\t{movie['year']}\t{movie['awards']}\t{movie['nominations']}\t{movie['best_picture']}".expandtabs(30))
    else:
        print(f"{movie['title'][:15]}\t{movie['year']}\t{movie['awards']}\t{movie['nominations']}".expandtabs(30))