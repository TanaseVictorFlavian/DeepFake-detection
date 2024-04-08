import torch


def get_prediction(model, device, *args):
    """
    Returns the prediction and model's confidence in the prediction 
    For multiple images it aggregates the predictions into a single final 
    prediction
    """
    model.to(device)
    model.eval()
    with torch.no_grad():
        # Receives a list of images
        if len(args) > 1:
            confidence = None
            prediction = None
            return prediction, confidence

        # Means it receives a single image
        else:
            image = args[0]
            logits = model()
            confidence = None
            prediction = None
            return prediction, confidence
    return
