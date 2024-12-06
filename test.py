import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

# URLs for the stats pages
url_batting = "https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946"
url_bowling = "https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2024-15946"
url_strike_rate = "https://www.espncricinfo.com/records/tournament/batting-highest-career-strike-rate/icc-men-s-t20-world-cup-2024-15946"
url_wicket_keeper = "https://www.espncricinfo.com/records/tournament/keeping-most-dismissals-career/icc-men-s-t20-world-cup-2024-15946"

# Fetch HTML responses
response = requests.get(url_batting).text
soup = BeautifulSoup(response, "html.parser")
response2 = requests.get(url_bowling).text
soup2 = BeautifulSoup(response2, "html.parser")
response3 = requests.get(url_strike_rate).text
soup3 = BeautifulSoup(response3, "html.parser")
response4 = requests.get(url_wicket_keeper).text
soup4 = BeautifulSoup(response4, "html.parser")

# Find all <tr> elements for each table
rows_batting = soup.find_all("tr")
rows_bowling = soup2.find_all("tr")
rows_strike_rate = soup3.find_all("tr")
rows_wicket_keeper = soup4.find_all("tr")

# Function to save data to a file
def saveData(path, text):
    with open(path, "a") as f:  # Open file in append mode
        f.write(text)

# Variables to handle data batching
batch_batting = []
batch_size = 15
batch_bowling = []
batch_size2 = 15
batch_strike_rate = []
batch_size3 = 15
batch_wicket_keeper = []
batch_size4 = 9

# Extract and save data from batting page
for row in rows_batting:
    cells = row.find_all("td")  # Find all <td> elements in the row
    if cells:
        row_data = [cell.text.strip() for cell in cells]
        batch_batting.append(",".join(row_data))

        if len(batch_batting) >= batch_size:
            saveData("batters_data.csv", "\n".join(batch_batting[:batch_size]) + "\n")
            batch_batting = batch_batting[batch_size:]

if batch_batting:
    saveData("batters_data.csv", "\n".join(batch_batting) + "\n")

# Extract and save data for bowling page
for row in rows_bowling:
    cells = row.find_all("td")
    if cells:
        row_data = [cell.text.strip() for cell in cells]
        batch_bowling.append(",".join(row_data))

        if len(batch_bowling) >= batch_size2:
            saveData("bowlers_data.csv", "\n".join(batch_bowling[:batch_size2]) + "\n")
            batch_bowling = batch_bowling[batch_size2:]

if batch_bowling:
    saveData("bowlers_data.csv", "\n".join(batch_bowling) + "\n")

# Extract and save data for strike rate page
for row in rows_strike_rate:
    cells = row.find_all("td")
    if cells:
        row_data = [cell.text.strip() for cell in cells]
        batch_strike_rate.append(",".join(row_data))

        if len(batch_strike_rate) >= batch_size3:
            saveData("strike_rate_data.csv", "\n".join(batch_strike_rate[:batch_size3]) + "\n")
            batch_strike_rate = batch_strike_rate[batch_size3:]

if batch_strike_rate:
    saveData("strike_rate_data.csv", "\n".join(batch_strike_rate) + "\n")

# Extract and save data for wicket-keeper stats page
for row in rows_wicket_keeper:
    cells = row.find_all("td")
    if cells:
        row_data = [cell.text.strip() for cell in cells]
        batch_wicket_keeper.append(",".join(row_data))

        if len(batch_wicket_keeper) >= batch_size4:
            saveData("wicket_keeper_data.csv", "\n".join(batch_wicket_keeper[:batch_size4]) + "\n")
            batch_wicket_keeper = batch_wicket_keeper[batch_size4:]

if batch_wicket_keeper:
    saveData("wicket_keeper_data.csv", "\n".join(batch_wicket_keeper) + "\n")

print("Data saved successfully.")
