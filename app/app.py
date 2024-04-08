from flask import Flask, request, render_template
from helpers.get_model import get_model
from werkzeug.utils import secure_filename
from helpers.prepare_data import prepare_image, prepare_video
from helper.prediction import get_prediction
app = Flask(__name__)

VIDEO_FORMATS = {'mp4', 'avi', 'mov', 'flv', 'wmv'}
IMAGE_FORMATS = {'jpg', 'jpeg', 'png', 'bmp'}
UPLOAD_FOLDER = './uploads'
ALLOWED_FORMATS = VIDEO_FORMATS.union(IMAGE_FORMATS)


def is_allowed(filename) -> bool:
    file_format =  filename.rsplit('.', 1)[1].lower() 
    allowed = '.' in filename and file_format in ALLOWED_FORMATS
    return allowed, file_format

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', result='No file part')
        
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', result='No selected file')

        allowed, file_format = is_allowed(file.filename)

        if file and allowed:
            filename = secure_filename(file.filename)
            file_path = f'{UPLOAD_FOLDER}/{filename}'
            file.save(file_path)
            
            model, transforms = get_model(
                model_name="effnet_b0_pretrained",
            )
            
            if filename in VIDEO_FORMATS:
                prepared_data = prepare_video(file_path, transforms)
            else: 
                prepared_data = prepare_image(file_path, transforms)
            
            deepfake, confidence = get_prediction(model, prepared_data)

        return render_template('index.html', deepfake = deepfake, confidence = confidence)
    return render_template('index.html', deepfake = "n/a", confidence = "n/a")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
