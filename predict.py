# predict.py

import torch
from transformers import BertTokenizer, BertForSequenceClassification
import torch.nn.functional as F

tokenizer = BertTokenizer.from_pretrained("sarkararnab/toxic_bert_model")
model = BertForSequenceClassification.from_pretrained("sarkararnab/toxic_bert_model")

model.eval()

labels = ['non-toxic', 'toxic']

def predict_comment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        pred_label = torch.argmax(probs, dim=1).item()
    return {
        "label": labels[pred_label],
        "probability": round(probs[0][pred_label].item(), 4)
    }
