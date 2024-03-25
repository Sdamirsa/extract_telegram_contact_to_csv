# [NO CODING IS NEEDED] Extract Contacts from Telegram html and save it as CSV (in 13 mins)
This repo is created for other people looking to convert their telegram exported contacts to CSV (so they can import in in google account or elsewhere).
This code is for windows users.

### Step 1: install python, please [4 min]
Follow this guide: https://www.digitalocean.com/community/tutorials/install-python-windows-10

### Step 3: Export contacts from Telegram [4 min]
For doing this you need to use Telegram Web.
- Go to settings
- Go to Advanced
- At the bottom you will find 'Export Telegram Data'
- Make sure to check Contacts

### Step 3: find the path to contacts.html [1 min]
In the exported folder open the folder named lists, and find the path to contacts.html
For example mine is: "C:\Users\LEGION\Downloads\Telegram Desktop\DataExport_2024-03-25\lists\contacts.html"

### Step 4: Get the code [1 min]
download the file you can see at the top of this page named extract_telegram_contact_to_csv.py
Find the downloaded file and get the path to this file (you can press ctrl+shift+C)
For example, mine is: C:\Users\LEGION\Desktop\extract_telegram_contact_to_csv.py
If you don't know how to install a single file [follow this](https://zapier.com/blog/how-to-download-from-github/#single)

### Step 5: run the code [3 min]
- Open 'Command prompt' by searching it on the Windows search bar
- type this:
    python [PATH TO THE CODE FILE]
  for example
    python C:\Users\LEGION\Desktop\extract_telegram_contact_to_csv.py
- if you faced this issue 'Failed to install BeautifulSoup.' It means that I failed to install it. You should do it yourself, and then run the code again. For this, [follow this instruction](https://www.listendata.com/2019/04/install-python-package.html) or just try this:
-   pip install BeautifulSoup
- when you run the code it will ask you for two things: The path to HTML file, and your desired path to save the CSV

### [Optional] Prepare it for Google
Follow this instruction to rename the column headers, so google can read this file:
https://www.wikihow.com/Add-Contacts-to-Gmail-Using-a-CSV-File
