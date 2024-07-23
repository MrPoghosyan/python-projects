# MapQuest Directions API Script

This script allows users to get routes and directions between two points using the MapQuest Directions API. The script prompts for the starting and ending points of the route, then outputs route information such as travel time, distance, and fuel consumption.

## Requirements

Before using the script, ensure you have the following dependencies installed:

- Python 3.x
- requests library

You can install the requests library using pip:

```bash
pip install requests

# Setup

Insert your API key into the key variable in the script: key = "your_key_write"

# Usage

1. Run the script: python mapquest_directions.py
2. Enter the starting location when prompted: Starting location: [your starting location]
3. Enter the destination location: Destination: [your destination]

The script will output route information including travel time, distance, fuel consumption, and step-by-step directions.

To exit the script, type quit or q as the starting or destination location.

# Notes

The script defaults to using kilometers (unit="k") and the Russian locale (locale="ru_RU"). These parameters can be changed in the URL string.
Fuel consumption is calculated based on an average consumption of 8 liters of gasoline per 100 km. You can adjust this parameter as needed.
