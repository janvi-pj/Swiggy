
Running the Script:

1.) Download the Script: First, download the Python script (let's call it menu_scraper.py) to your local machine.

2.) Install Required Packages: If you haven't already, install the required Python packages using pip. You can do this by running the following command in your terminal or command prompt:
pip install requests

3.) Run the Script: Open your terminal or command prompt, navigate to the directory where the menu_scraper.py script is located, and run the script using Python. Provide the restaurant ID as a command-line argument when running the script:
python menu_scraper.py <restaurant_id>
Replace <restaurant_id> with the ID of the restaurant whose menu you want to scrape.


Script Functionality:

The script menu_scraper.py fetches menu data from the Swiggy API for a given restaurant ID, extracts relevant information (such as menu item names, prices, and categories), and saves this data into a CSV file. It uses the requests library to make HTTP requests, the csv library to work with CSV files, and the sys module to access command-line arguments.

Necessary Setup Steps:
1.) Obtain Restaurant ID: You need to know the ID of the restaurant whose menu you want to scrape. This ID is typically available in the URL of the restaurant's page on the Swiggy website.

2.) API Key (if applicable): If the Swiggy API requires an API key for access, you'll need to obtain this key and set it up in the script. However, in the provided script, no API key is required as it directly fetches menu data from the Swiggy website.
