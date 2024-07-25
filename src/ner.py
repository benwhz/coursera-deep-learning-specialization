from transformers import pipeline

model_name = "tsmatz/xlm-roberta-ner-japanese"
classifier = pipeline("token-classification", model=model_name, from_pt=True)
result = classifier("鈴木は4月の陽気の良い日に、鈴をつけて熊本県の阿蘇山に登った")
print(result)
