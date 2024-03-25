import csv
import sys
from bs4 import BeautifulSoup

# Check if BeautifulSoup is installed, install it if not
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup package not found. Installing...")
    try:
        import pip
        pip.main(['install', 'beautifulsoup4'])
        from bs4 import BeautifulSoup
    except Exception as e:
        print("Failed to install BeautifulSoup. Please install it manually and try again.")
        sys.exit(1)
    try:
        import pip
        pip.main(['install', 'csv'])
        import csv
    except Exception as e:
        print("Failed to install CSV. Please install it manually and try again.")
        sys.exit(1)



def extract_contacts(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    contacts = []

    for entry in soup.find_all(class_='entry'):
        name = entry.find(class_='name').text.strip()
        phone = entry.find(class_='details_entry').text.strip()
        phone = str(phone)
        contacts.append((name, phone))

    return contacts

def write_to_csv(contacts, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Phone'])
        writer.writerows(contacts)

def main():
    html_file = input(r'please give the exact path of the html file with name contacts.html for example C:\Users\LEGION\Downloads\Telegram Desktop\DataExport_2024-03-25\lists\contacts.html: ')  # Update with your HTML file name/path
    csv_file = input(r'give the path to store the csv file for example C:\Users\LEGION\Desktop\contacts.csv: ')  # Name of the CSV file to be created

    contacts = extract_contacts(html_file)
    write_to_csv(contacts, csv_file)

    print(f"CSV file generated successfully and saved at: {csv_file}.")

if __name__ == "__main__":
    main()
