import sys
import requests

def get_characters(movie_id):
    try:
        # Retrieve the film data from the Star Wars API
        response = requests.get(f"https://swapi.dev/api/films/{movie_id}/")
        response.raise_for_status()  # Check if request was successful
        film_data = response.json()

        # Loop through each character URL in the "characters" list
        for character_url in film_data['characters']:
            # Fetch the character's data
            character_response = requests.get(character_url)
            character_response.raise_for_status()
            character_data = character_response.json()
            
            # Print the character's name
            print(character_data['name'])
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Ensure a movie ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <movie_id>")
else:
    movie_id = sys.argv[1]
    get_characters(movie_id)
