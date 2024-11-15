import requests

# Replace with the path to your local Flask app's transform URL
url = 'http://127.0.0.1:5000/transform'

# Prepare a file to send in the request (use an existing file path)
file_path = 'abc.txt'  # Replace with your file's path
format = 'pdf'  # Desired output format (change as needed)

# Open the file and send a POST request
with open(file_path, 'rb') as file:
    response = requests.post(url, files={'file': file}, data={'format': format})

# Print the response from the Flask app
print(response.json())
