# Star Wars Movie Data Fetcher

This Python script fetches data about Star Wars movies and their characters from the Star Wars API (SWAPI).

## Features

1. Fetches all Star Wars movies from the SWAPI.
2. Fetches all characters for each movie.
3. Finds characters that appear in all movies.
4. Saves the fetched data into JSON files.

## How to Run

You can run this script using Python 3. Make sure you have the `requests` and `json` libraries installed. If not, you can install them using pip:

\`\`\`bash
pip install requests
\`\`\`

Then, you can run the script:

\`\`\`bash
python script_name.py
\`\`\`

Replace `script_name.py` with the name of the script file.

## Output

The script prints the title and release date of each movie. It also prints the name and gender of characters that appear in all movies.

The script creates three JSON files:

1. `movies.json`: Contains data about all Star Wars movies.
2. `characters.json`: Contains data about all characters in the movies.
3. `shared_characters.json`: Contains data about characters that appear in all movies.

## Note

The script uses the SWAPI, which is a free, open API. The API might have rate limits or might be down sometimes, so please consider this while using the script.
