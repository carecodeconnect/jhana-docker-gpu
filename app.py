from flask import Flask, jsonify, request
import subprocess
import torch

app = Flask(__name__)

@app.route('/gpu-info')
def gpu_info():
    try:
        # Run the `nvidia-smi` command and capture its output
        output = subprocess.check_output(['nvidia-smi'], stderr=subprocess.STDOUT)
        gpu_info_text = output.decode('utf-8')
    except Exception as e:
        gpu_info_text = f"An error occurred: {e}"

    # Return the GPU information as plain text
    return jsonify({'gpu_info': gpu_info_text})

@app.route('/gpu-multiply', methods=['POST'])
def gpu_multiply():
    # Ensure CUDA is available
    if not torch.cuda.is_available():
        return jsonify({'error': 'CUDA not available'}), 500

    # Get matrices from the POST request
    data = request.get_json()
    matrix_a = torch.tensor(data['matrix_a']).cuda().float()  # Convert to float after moving to CUDA
    matrix_b = torch.tensor(data['matrix_b']).cuda().float()  # Convert to float after moving to CUDA

    # Perform matrix multiplication
    result = torch.matmul(matrix_a, matrix_b)

    # Convert result back to a CPU tensor and then to a list for JSON serialization
    result_list = result.cpu().numpy().tolist()

    return jsonify({'result': result_list})

if __name__ == '__main__':
    # Run the Flask app on all available IPs on port 5000 (default Flask port)
    app.run(host='0.0.0.0')
