# backend/server.py
from flask import Flask, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/compute', methods=['POST'])
def compute():
    code = request.json.get('code')
    # Execute the code (this is a simple and unsafe eval, for production use a safer method)
    try:
        exec(code, globals())
        plt.savefig("output.png")
        with open("output.png", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read()).decode()
        return jsonify({"result": "success", "plot": b64_string})
    except Exception as e:
        return jsonify({"result": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
