from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Document Transformation API!"})

@app.route('/transform', methods=['POST'])
def transform():
    file = request.files.get('file')
    format = request.form.get('format')
    if not file or not format:
        return jsonify({"error": "Missing file or format"}), 400

    # For simplicity, mock a transformation process
    transformed_filename = f"transformed_file.{format}"
    return jsonify({"message": "File transformed successfully", "output_file": transformed_filename})

if __name__ == '__main__':
    app.run(debug=True)
