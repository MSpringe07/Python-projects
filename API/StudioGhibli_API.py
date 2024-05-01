import requests
import json

def fetch_ghibli_movies():
    url_films = "https://ghibliapi.dev/films"
    response = requests.get(url_films)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Error: Received non-JSON response")
            return None
    else:
        print(f"Error: Failed to fetch data, status code {response.status_code}")
        return None

def display_movies(movies):
    if movies and isinstance(movies, list):
        for i, movie in enumerate(movies, start=1):
            if isinstance(movie, dict):
                title = movie.get('title', 'Unknown Title')
                description = movie.get('description', 'No description available')
                director = movie.get('director', 'Unknown Director')
                release_date = movie.get('release_date', 'Unknown Release Date')

                print("*" * 60)
                print(f"\n {i} : \"{title}\"\n*{description}\n- Director: {director}\n- Release date: {release_date}")
            else:
                print(f"Error: Unexpected data format for movie {i}")
    else:
        print("No movie data available or invalid format.")

def fetch_additional_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_resident_info(resident_url):
    resident_info = fetch_additional_info(resident_url)
    if resident_info:
        movies_urls = resident_info.get("films", [])
        movies_names = [fetch_additional_info(movie_url).get("title", "Unknown Movie") for movie_url in movies_urls]

        species_url = resident_info.get("species", "")
        species_name = "Unknown Species"
        if species_url:
            species_info = fetch_additional_info(species_url)
            species_name = species_info.get("name", "Unknown Species")

        return {
            "id": resident_info.get("id", "Unknown ID"),
            "name": resident_info.get("name", "Unknown Name"),
            "gender": resident_info.get("gender", "Unknown Gender"),
            "age": resident_info.get("age", "Unknown Age"),
            "eye_color": resident_info.get("eye_color", "Unknown"),
            "hair_color": resident_info.get("hair_color", "Unknown"),
            "movies": movies_names,
            "species": species_name
        }
    else:
        return "Unknown Resident"

def fetch_ghibli_locations():
    url = "https://ghibliapi.dev/locations"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")
        return []

def process_locations(locations):
    processed_locations = []
    for location in locations:
        if isinstance(location, dict):
            residents_urls = location.get('residents', [])
            residents_info = [fetch_resident_info(url) for url in residents_urls if url != "TODO"]
            processed_location = {
                'name': location.get('name', 'Unknown Name'),
                'climate': location.get('climate', 'Unknown Climate'),
                'terrain': location.get('terrain', 'Unknown Terrain'),
                'residents': residents_info
            }
            processed_locations.append(processed_location)
    return processed_locations

# Fetch and display movies
movies = fetch_ghibli_movies()
display_movies(movies)

# Fetch locations from the Ghibli API
locations = fetch_ghibli_locations()

# Process the locations to include detailed resident information
processed_locations = process_locations(locations)

# Save the processed locations to a JSON file
file_path = 'ghibli_locations_detailed.json'
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(processed_locations, file, indent=4)

print(f"Processed location data saved to {file_path}")
