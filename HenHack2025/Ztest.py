import requests

def search_providers(postal_code, taxonomy_description, limit=10):
    """
    Searches for providers using the NPPES API given a postal_code and taxonomy description.
    """
    url = "https://npiregistry.cms.hhs.gov/api/"
    params = {
        "version": "2.1",
        # "city": city,
        # "state": state,
        "postal_code": postal_code,
        "taxonomy_description": taxonomy_description,
        "limit": limit
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Get user input for location and doctor type.
    location = input("Enter your location (postal_code): ")
    try:
        postal_code = location
    except ValueError:
        print("Please enter your location in the format 'postal_code' (e.g., '11111').")
        return

    taxonomy = input("Enter the type of doctor you are looking for (e.g., 'Family Medicine'): ")

    data = search_providers(postal_code, taxonomy)
    if data and "results" in data and data["results"]:
        print(f"\nFound {len(data['results'])} providers:\n")
        for provider in data["results"]:
            basic_info = provider.get("basic", {})
            first_name = basic_info.get("first_name", "")
            last_name = basic_info.get("last_name", "")
            full_name = f"{first_name} {last_name}".strip()
            
            # Get the primary address (first address in the array)
            addresses = provider.get("addresses", [])
            if addresses:
                primary = addresses[0]
                address_line = primary.get("address_1", "")
                city_addr = primary.get("city", "")
                state_addr = primary.get("state", "")
                postal_code = primary.get("postal_code", "")
                location_info = f"{address_line}, {city_addr}, {state_addr} {postal_code}"
            else:
                location_info = "No address provided."
            
            print("Name:", full_name)
            print("Location:", location_info)
            print("-" * 40)
    else:
        print("No providers found for the given criteria.")

if __name__ == "__main__":
    main()
