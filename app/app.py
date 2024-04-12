import os
import sys

sys.path.insert(0, 'D:\AA_Licenta\DeepFake-detection')

from flask import Flask, request, render_template
from helpers.get_model import get_model
from werkzeug.utils import secure_filename
from helpers.prepare_data import prepare_image, prepare_video
from helpers.prediction import get_prediction
import torch
import time 

UPLOAD_FOLDER = './uploads'
VIDEO_FORMATS = {'mp4', 'avi', 'mov', 'flv', 'wmv'}
IMAGE_FORMATS = {'jpg', 'jpeg', 'png', 'bmp'}
ALLOWED_FORMATS = VIDEO_FORMATS.union(IMAGE_FORMATS)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def is_allowed(filename) -> bool:
    file_format =  filename.rsplit('.', 1)[1].lower() 
    allowed = '.' in filename and file_format in ALLOWED_FORMATS
    return allowed, file_format

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html')
        
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html')

        allowed, file_format = is_allowed(file.filename)

        if file and allowed:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            device = "cuda" if torch.cuda.is_available() else "cpu"

            model, transforms = get_model(
                model_name="effnet_b0_pretrained",
            )

            print(os.path.exists(UPLOAD_FOLDER))
            prepared_data = prepare_video(UPLOAD_FOLDER, transforms) if file_format in VIDEO_FORMATS \
                            else prepare_image(file_path, transforms)
            

            # deepfake, confidence = get_prediction(model, device, prepared_data)


            # try:
            #     os.remove(file_path)
            #     print("File Removed!")
            # except Exception as e:
            #     return(f"Error deleting file: {e}")
            return "worked"
            # return render_template('index.html', deepfake = deepfake, confidence = confidence, show_data = True)

    return render_template('index.html', deepfake = "n/a", confidence = "n/a", show_data = False)


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(host='0.0.0.0', debug=True)
