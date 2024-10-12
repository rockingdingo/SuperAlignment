import torch
import torch.nn as nn
import torch.nn.functional as F

def auxConfidentLoss(alpha, t, x_weak, x_strong):
    """
        AUXILIARY CONFIDENCE LOSS as in weak to strong generalization paper
    """
    ce_loss = nn.CrossEntropyLoss()
    x_strong_ind = torch.relu(x_strong - t)
    aux_loss = alpha * ce_loss(x_strong, x_weak) + (1-alpha) * ce_loss(x_strong, x_strong_ind)
    return aux_loss

