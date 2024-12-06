import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

# URL for the batting stats page
url_batting = "https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946"
url_bowling="https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2024-15946"

# Fetch HTML response
response = requests.get(url_batting).text
soup = BeautifulSoup(response, "html.parser")
response2 = requests.get(url_bowling).text
soup2= BeautifulSoup(response2, "html.parser")

# Find all <tr> elements
rows = soup.find_all("tr")
rows2 = soup2.find_all("tr")

# Function to save data to file
def saveData(path, text):
    with open(path, "a") as f:  # Open file in append mode
        f.write(text)

# Variables to handle data batching
batch = []
batch_size = 15
batch2 = []
batch_size2 = 15

# Extract and save data from each <tr>
for row in rows:
    cells = row.find_all("td")  # Find all <td> elements in the row
    if cells:
        # Get text from each cell and extend the batch
        row_data = [cell.text.strip() for cell in cells]
        batch.extend(row_data)

        # If batch reaches the required size, save to file
        if len(batch) >= batch_size:
            saveData("batters_data.csv", ",".join(batch[:batch_size]) + "\n")  # Save first 15 items
            batch = batch[batch_size:]  # Remove saved items from batch

# Save remaining data if batch is not empty
if batch:
    saveData("data.csv", ", ".join(batch) + "\n")

    
# Extract and save data for bowling from each <tr>
for row in rows2:
    cells = row.find_all("td")  # Find all <td> elements in the row
    if cells:
        # Get text from each cell and extend the batch
        row_data = [cell.text.strip() for cell in cells]
        batch2.extend(row_data)

        # If batch reaches the required size, save to file
        if len(batch2) >= batch_size2:
            saveData("bowlers_data.csv", ",".join(batch2[:batch_size2]) + "\n")  # Save first 15 items
            batch2 = batch2[batch_size2:]  # Remove saved items from batch

# Save remaining data if batch is not empty
if batch2:
    saveData("data2.csv", ", ".join(batch2) + "\n")

print("Data saved successfully.")

