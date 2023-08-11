import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer


# Load the model state dictionary
model_state_dict = torch.load("./pytorch_model.bin", map_location=torch.device('cpu'))

# Create an instance of the model using its class definition
model = AutoModelForQuestionAnswering.from_pretrained("HooshvareLab/bert-fa-base-uncased", state_dict=model_state_dict)

tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-fa-base-uncased")
