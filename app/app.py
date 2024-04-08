from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Ensure there's a folder to save the uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)

    
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        # Now you can use the file path to process the file using your ML model
        return jsonify({'message': 'File successfully uploaded'}), 200


if __name__ == '__main__':
    # Create the upload folder if it doesn't exist

    # video_formats = ['mp4', 'avi', 'mov', 'flv', 'wmv', 'mkv']
    image_formats = ['png', 'jpg', 'jpeg']
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
