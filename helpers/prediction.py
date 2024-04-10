import torch
from torch.nn.functional import softmax

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
        if len(data) > 1:
            confidence = None
            prediction = None
            return prediction, confidence

        # Means it receives a single image
        else:
            img_tensor = data[0].to(device)
            logits = model(img_tensor)
            confidence = softmax(logits, dim=1)
            _, label = torch.max(logits, 1)

            print(confidence[0])
            print(label.item())
            print(confidence)
            confidence = confidence[0][label.item()]

            label = "False" if label.item() == 0 else "True"
            return label, confidence
