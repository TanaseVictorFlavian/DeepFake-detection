import torch
from torch.nn.functional import softmax
import numpy as np
def get_prediction(model, device, data):
    """
    Returns the prediction and model's confidence in the prediction 
    For multiple images it aggregates the predictions into a single final 
    prediction
    """
    model.to(device)
    model.eval()
    with torch.no_grad():
        # Receives a list of images
        prediction_logits = np.array([])
        prediction_scores = np.array([])
        if len(data) > 1:
            for image in data:
                img_tensor = image.to(device)
                logits = model(img_tensor)
                confidence = softmax(logits, dim=1)
                
                prediction_logits = np.append(prediction_logits, logits)
                prediction_scores = np.append(prediction_scores, confidence)   
        
            print(prediction_logits)
            print(prediction_scores)
            
            return 

        # Means it receives a single image
        else:
            img_tensor = data[0].to(device)
            logits = model(img_tensor)
            confidence = softmax(logits, dim=1)
            _, label = torch.max(logits, 1)
            confidence = confidence[0][label.item()].item()
            confidence = f"{confidence * 100:.2f}%"
            print(label.item())
            label = "True" if label.item() == 0 else "False"
            return label, confidence
