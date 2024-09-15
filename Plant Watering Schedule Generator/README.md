# Plant Watering Schedule Generator

## Overview

This Python program generates a schedule for watering plants, ensuring that no person is assigned to water plants on consecutive days. It reads data from a CSV file, processes the schedule, and outputs the result to another CSV file.

## Requirements

- Python 3.x
- `csv` module (comes pre-installed with Python)

## Files

1. **`file.csv`**: Input CSV file containing the names of people and the number of days they are responsible for watering plants.
2. **`queue.csv`**: Output CSV file containing the generated schedule.

### Example `file.csv`

```csv
name,flowers
Alex,4
Bob,3
Charlie,6
David,3
Eva,2

### How It Works

Read Data: The program reads the data from file.csv, which includes names of people and the number of days each person is responsible for watering plants.
Generate Schedule: The QueueGenerator class generates a random schedule ensuring that no person is assigned to water plants on consecutive days. It uses the random module to shuffle the days and verify that there are no consecutive assignments.
Write Output: The generated schedule is written to queue.csv with each row indicating the day and the person responsible.

### Running the Program
Place the file.csv in the same directory as the script.

Run the Python script: python watering_schedule.py

Check the queue.csv file for the generated schedule.


### Code Structure
Person: Represents an individual person with a name and number of days they are responsible for.
CSVHandler: Handles reading from and writing to CSV files.
QueueGenerator: Generates a schedule while ensuring no person is assigned to consecutive days.

#### Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements for the program.
