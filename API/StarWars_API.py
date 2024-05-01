import requests
import json

def fetch_characters(character_urls):
    characters_data = []
    for url in character_urls:
        response = requests.get(url)
        if response.status_code == 200:
            character_data = response.json().get('result', {}).get('properties', {})
            characters_data.append((url, character_data))
    return characters_data

def find_shared_characters(movies_dict):
    character_appearances = {}
    for movie in movies_dict.values():
        for url, _ in movie['Characters']:
            character_appearances[url] = character_appearances.get(url, 0) + 1

    shared_characters_urls = [url for url, count in character_appearances.items() if count == len(movies_dict)]
    return shared_characters_urls

def fetch_star_wars_movies():
    url = "https://www.swapi.tech/api/films"
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to fetch data from the API."

    data = response.json()
    movies = data.get('result', [])
    movies_dict = {}
    all_characters = {}

    for movie in movies:
        movie_detail = movie['properties']
        title = movie_detail['title']
        release_date = movie_detail['release_date']
        character_urls = movie_detail['characters']
        characters = fetch_characters(character_urls)
        movies_dict[title] = {
            'Title': title,
            'Release Date': release_date,
            'Characters': characters
        }
        print(f"Movie: {title}, Release Date: {release_date}")

        for url, character in characters:
            all_characters[url] = character

    with open('movies.json', 'w') as file:
        json.dump(movies_dict, file, indent=4)

    with open('characters.json', 'w') as file:
        json.dump(all_characters, file, indent=4)

    shared_characters_urls = find_shared_characters(movies_dict)
    shared_characters_data = [fetch_characters([url])[0][1] for url in shared_characters_urls]

    shared_characters_info = []
    for character in shared_characters_data:
        character_info = {
            'Name': character.get('name', 'Unknown'),
            'Gender': character.get('gender', 'Unknown')
        }
        print(f"Shared Character - Name: {character_info['Name']}, Gender: {character_info['Gender']}")
        shared_characters_info.append(character_info)

    with open('shared_characters.json', 'w') as file:
        json.dump(shared_characters_info, file, indent=4)

    return movies_dict

star_wars_movies = fetch_star_wars_movies()
