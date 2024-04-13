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
        prediction_logits = []
        prediction_scores = []


        if len(data) > 1:
            for image in data:
                img_tensor = image.to(device)
                logits = model(img_tensor)
                confidence = softmax(logits, dim=1)
                
                prediction_logits.append(logits.detach().cpu().tolist())
                prediction_scores.append(confidence.detach().cpu().tolist())  
            
            prediction_logits = np.array([item for sublist1 in prediction_logits for sublist2 in sublist1 for item in sublist2])
            prediction_scores = np.array([item for sublist1 in prediction_scores for sublist2 in sublist1 for item in sublist2])

            prediction_logits = prediction_logits.reshape(len(data), 2)
            prediction_scores = prediction_scores.reshape(len(data), 2)

            avg_logits = np.mean(prediction_logits, axis=0)
            avg_scores = np.mean(prediction_scores, axis=0)

            label = np.argmax(avg_logits)
            confidence = f"{avg_scores[label] *100:.2f}%"
            label = "True" if label == 0 else "False"
            print(label)
            print(confidence)

        # Means it receives a single image
        else:
            img_tensor = data[0].to(device)
            logits = model(img_tensor)
            confidence = softmax(logits, dim=1)
            _, label = torch.max(logits, 1)
            confidence = confidence[0][label.item()].item()
            confidence = f"{confidence * 100:.2f}%"
            label = "True" if label.item() == 0 else "False"

    return label, confidence