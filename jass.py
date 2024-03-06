import requests  # Import the requests library to make HTTP requests
import csv  # Import the csv library to work with CSV files
import sys  # Import the sys module to access command-line arguments


# Function to fetch menu data from Swiggy API using restaurant ID
def fetch_menu_data(restaurant_id):
    # Construct the URL for fetching menu data for the given restaurant ID
    url = f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId={restaurant_id}"

    # Define user-agent headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        # Send a GET request to the Swiggy API with the constructed URL and headers
        response = requests.get(url, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and return the menu data
            return response.json()
        else:
            # Print an error message if the request was not successful
            print(f"Failed to fetch menu data. Status Code: {response.status_code}, Response: {response.content}")
            return None
    except requests.RequestException as e:
        # Print an error message if there's an exception during the request
        print(f"Error fetching menu data: {e}")
        return None


# Function to extract menu items from menu data
def extract_menu_items(menu_data):
    menu_items = []  # Initialize an empty list to store menu items
    sections = menu_data.get('sections', [])  # Get the list of sections from the menu data

    # Iterate through each section
    for section in sections:
        # Iterate through each item in the section
        for item in section.get('items', []):
            # Extract name, price, and category of the item and append it to the menu_items list
            menu_items.append({
                'name': item.get('name', ''),
                'price': item.get('prices', [])[0].get('price', ''),
                'category': section.get('sectionName', '')
            })
    return menu_items  # Return the list of extracted menu items


# Function to save menu items to a CSV file
def save_to_csv(menu_items, restaurant_id):
    filename = f"{restaurant_id}_menu.csv"  # Construct the filename for the CSV file

    try:
        # Open the CSV file in write mode and specify encoding as UTF-8
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Define fieldnames for the CSV file
            fieldnames = ['name', 'price', 'category']

            # Create a DictWriter object to write data to the CSV file
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row to the CSV file
            writer.writeheader()

            # Iterate through each menu item and write it to the CSV file
            for item in menu_items:
                writer.writerow(item)

        # Print a message indicating that menu data has been saved to the CSV file
        print(f"Menu data saved to {filename}")
    except IOError as e:
        # Print an error message if there's an IOError (e.g., file not found or permission denied)
        print(f"Error saving menu data to CSV: {e}")


# Main function to orchestrate the script execution
def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <restaurant_id>")
        sys.exit(1)  # Exit the script with an error code

    # Extract the restaurant ID from the command-line arguments
    restaurant_id = sys.argv[1]

    # Fetch menu data for the specified restaurant ID
    menu_data = fetch_menu_data(restaurant_id)

    # If menu data is retrieved successfully
    if menu_data:
        # Extract menu items from the menu data
        menu_items = extract_menu_items(menu_data)

        # Save menu items to a CSV file
        save_to_csv(menu_items, restaurant_id)


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
