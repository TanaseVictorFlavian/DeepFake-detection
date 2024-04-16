import torch
from torch.nn.functional import softmax
import numpy as np
def get_prediction(model, device, data):
    """
    Returns the prediction and model's confidence in the prediction 
    For multiple images it aggregates the predictions into a single final 
    prediction
    """

    print(len(data))
    model.to(device)
    model.eval()
    with torch.no_grad():
        # Receives a list of images

        
        if len(data) > 1:
            prediction_logits = []
            
            for image in data:
                img_cuda = image.to(device)
                logits = model(img_cuda)
                confidence = softmax(logits, dim=1)
                
                prediction_logits.append(logits.detach().cpu().tolist())
            
            prediction_logits = np.array([i for l1 in prediction_logits for l2 in l1 for i in l2]).reshape(len(data), 2)

            avg_logits = np.mean(prediction_logits, axis=0)

            logits_tensor = torch.from_numpy(avg_logits)
            scores_tensor = softmax(logits_tensor.float(), dim=0)
            scores = scores_tensor.numpy()

            predicted_class = np.argmax(avg_logits)
            confidence = f"{scores[predicted_class] *100:.2f}%"
            label = "True" if predicted_class == 0 else "False"

        # Means it receives a single image
        else:
            print("Predicting for a single image")
            img_tensor = data[0].to(device)
            logits = model(img_tensor)
            confidence = softmax(logits, dim=1)
            _, label = torch.max(logits, 1)
            confidence = confidence[0][label.item()].item()
            confidence = f"{confidence * 100:.2f}%"
            label = "True" if label.item() == 0 else "False"

    return label, confidence