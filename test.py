import requests  # type: ignore
from bs4 import BeautifulSoup # type: ignore

url_batting="https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946"

response=requests.get(url_batting).text

soup=BeautifulSoup(response,"html.parser")
name=soup.find_all(class_="ds-text-tight-s ds-font-regular ds-text-typo-primary hover:ds-text-typo-primary-hover ds-block")

scoreText=soup.find_all(class_="ds-min-w-max ds-text-right")
count=0
def saveData(path, text):
    with open(path, "a") as f:  # Open file in append mode
        f.write(text + "\n")

for t in scoreText :
 #print(t.text)
 saveData("data.csv",t.text+" ")
 count+=1 
print(count/14)

for t in name :
   saveData("name.csv",t.text+" ")
# Combine and save data
# count = 0
# for div, text in zip(scoreDiv, scoreText):  # Combine corresponding elements
#     combined_text = f"{div.text.strip()} - {text.text.strip()}"  # Format data
#     saveData("data.csv", combined_text)  # Save to file
#     count += 1

# print(f"Data saved for {count} records.")



# if response.status_code==200:
#    print(response.text)


