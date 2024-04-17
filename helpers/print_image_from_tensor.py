import torch
from torchvision.transforms.functional import to_pil_image
from torchvision.transforms import transforms   
def denormalize(tensor, mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]):
    
    inv_normalize = transforms.Normalize(
        mean=[-m/s for m, s in zip(mean, std)],
        std=[1/s for s in std]
    )
    tensor = inv_normalize(tensor)
    return tensor


def tensor_to_pil(tensor):
    """ Convert a tensor to a PIL Image """
    back_to_img = transforms.ToPILImage()
    return back_to_img(tensor)

def print_image_from_tensor(tensor):
    if tensor.requires_grad:
        tensor = tensor.detach()

    tensor = tensor.cpu().squeeze()

    image = tensor_to_pil(denormalize(tensor))
    image.show()

    return image