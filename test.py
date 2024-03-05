import requests

url = "http://192.168.178.37:5000/gpu-multiply"
data = {
    "matrix_a": [[1, 2], [3, 4]],
    "matrix_b": [[5, 6], [7, 8]]
}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, json=data, headers=headers)  # Use 'json=data' for simplicity

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

# # URL to GPU info API
# url = "http://192.168.178.37:5000/gpu-info"
# # Send a GET request to the API
# response = requests.get(url)
# # Check if the request was successful
# if response.status_code == 200:
#     # Get the JSON data
#     gpu_info = response.json()
#     print(gpu_info)
# else:
#     print("Failed to retrieve GPU information")

