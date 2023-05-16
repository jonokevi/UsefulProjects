import requests  #requests library allows for requesting data on the internet.

import os    #os library allows for operating system interactivity.

dlUrl = "(INSERT URL PATH DESIRED HERE)"    #input a direct URL ending in a "." file format.

filename = dlUrl[dlUrl.rfind('/') + 1:]

if os.path.isfile(filename):               #checks if file is already downloaded locally before executing the download code below.
    print("File already exists.")

else: 

    try:
        request = requests.get(dlUrl)
        request.raise_for_status()

        content_size = int(request.headers.get('Content-Length', 0))
        file_size = round(content_size / 1024, 2)


        filename = request.url [dlUrl.rfind('/')+1:]


        with open(filename, 'wb') as f:
            for chunk in request.iter_content(chunk_size=8000):
                if chunk:
                    f.write(chunk)

 
        print(f"File downloaded successfully. File size: {file_size} KB")

    except requests.exceptions.RequestException as e:                       #error handling
        print (f"An error occurred during the download: {e}")

    except IOError as e:
        print(f"An error occurred while writing this file: {e}")
