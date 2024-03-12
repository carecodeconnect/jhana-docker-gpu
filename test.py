import requests

# # URL to GPU info API
# Local Network IPs
#url = "http://192.168.178.37:5000/gpu-multiply" # DSR IP
#url = "http://172.17.0.2:5000/gpu-info" # home ISP
url_gpu_multiply = "http://127.0.0.1:5000/gpu-multiply" # home ISP
url_gpu = "http://127.0.0.1:5000/gpu-info" # home ISP

# Try ngrok
# ngrok http http://localhost:5000
# Public internet IPs
url_gpu_multiply = "https://e32c-2a01-5241-804-d900-c873-d355-c6a8-a421.ngrok-free.app/gpu-multiply"
# Static Domain
# ngrok http --domain=promoted-yak-loosely.ngrok-free.app 5000

# Test GPU Information
# Send a GET request to the API
response = requests.get(url_gpu)
# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data
    gpu_info = response.json()
    print(gpu_info)
else:
    print("Failed to retrieve GPU information")

# Test Matrix Multiplication with GPU
data = {
    "matrix_a": [[1, 2], [3, 4]],
    "matrix_b": [[5, 6], [7, 8]]
}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url_gpu_multiply, json=data, headers=headers)  # Use 'json=data' for simplicity

    if response.status_code == 200:
        try:
            result = response.json().get('result')  # Use .get to avoid KeyError
            if result is not None:
                print("Result of Matrix Multiplication:", result)
            else:
                print("No result field in the response")
        except ValueError:  # Catch JSON decoding errors
            print("Error decoding JSON:", response.text)
    else:
        print("Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:  # Catch requests exceptions
    print("Request failed:", e)


