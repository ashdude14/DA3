# Best 11 Players Selector

This project aims to select  the **Best 11 Players** for a cricket team using data scraped from ESPN Cricinfo. The team composition adheres to the following structure:

- **5 Batters**
- **1 Finisher**
- **1 All-Rounder**
- **4 Bowlers**

The data is scraped from ESPN Cricinfo's records section for the ICC Men's T20 World Cup 2024, focusing on player performances.

---

## Project Features

1. **Data Scraping**:
   - Scrapes player data (names, runs, strike rate, wickets, etc.) from ESPN Cricinfo.
   - Organizes data into categories like batters, finishers, all-rounders, and bowlers.

2. **Team Composition**:
   - Automatically selects players based on their performance metrics.
   - Ensures the team follows the required structure: 5 batters, 1 finisher, 1 all-rounder, and 4 bowlers.

3. **Output**:
   - Saves the selected team as a CSV file.
   - Provides a readable summary of the team.

---

## Requirements

Before running the script, ensure the following:

- **Python 3.x** installed on your system.
- The following Python libraries:
  - `requests`
  - `BeautifulSoup` from `bs4`
  - `pandas` for data handling (optional but recommended)

Install missing libraries with:
```bash
pip install requests beautifulsoup4 pandas
