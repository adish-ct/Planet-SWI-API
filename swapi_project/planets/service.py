import requests
from .models import Planet


def fetch_and_store():
    endpoint = "https://swapi-graphql.netlify.app/.netlify/functions/index"
    query = """
    query {
      allPlanets {
        planets {
          name
          population
          terrains
          climates
        }
      }
    }
    """.strip()  # Remove extra whitespace

    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(endpoint, json={'query': query}, headers=headers)
        data = response.json()
        print(f"Response Data : {data}")
        # Defensive: check for 'data' key
        if 'data' in data:
            planets_list = data['data']['allPlanets']['planets']
            for item in planets_list:
                Planet.objects.create(
                    name=item.get('name'),
                    population=item.get('population') or 'unknown',
                    climates=", ".join(item.get('climates', [])),
                    terrains=", ".join(item.get('terrains', []))
                )
        else:
            print("Query failed: ", data)
    except Exception as e:
        print(f"Exception Raised during API call : {e}\n")

