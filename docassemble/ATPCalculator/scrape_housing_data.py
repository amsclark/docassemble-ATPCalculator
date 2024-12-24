import requests
from bs4 import BeautifulSoup
import csv

def url_to_filename(url):
	#remove everything until the last /
	filename = url.split('/')[-1]
	# Remove "-local-standards-housing-and-utilities" from the end
	filename = filename.replace("-local-standards-housing-and-utilities", "")
	# Add ".csv" at the end
	filename += ".csv" 
	return filename 

def extract_table_to_csv(url): 
	try: 
		response = requests.get(url)
		soup = BeautifulSoup(response.content, 'html.parser')

		# Find the first table in the HTML
		table = soup.find_all('table')[0]

		# Extract table rows
		rows = table.find_all('tr')

		# Open a CSV file to write the table data
		#filename = url_to_filename(url) 
		#with open(filename, 'w', newline='') as csvfile:
			#csvwriter = csv.writer(csvfile)
		#for row in rows: 
		#	cols = row.find_all(['td', 'th']) 
		#	cols = [col.text.strip() for col in cols] 
		#	csvwriter.writerow(cols)

		# Display the table data
		for row in rows:
			cols = row.find_all(['td', 'th'])
			cols = [col.text.strip() for col in cols]
			print("\t".join(cols))
		print(f"Succesfully scraped and displayed data from {url}")

	except IndexError:
		print(f"No table found in {url}, skipping...")
	except Exception as e:
		print(f"An error occurred while processing {url}: {e}")

# Read URLs from the file
with open('urls.txt', 'r') as file: 
	urls = [line.strip() for line in file]
# Iterate over each URL and extract table data to CSV
for url in urls: 
	print(f"Scraping {url}...")
	extract_table_to_csv(url)
print("Table data has been extracted and saved as CSV files.")
