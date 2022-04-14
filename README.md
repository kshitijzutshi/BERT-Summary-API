# BERT-Summary-API

Created BERT Text Summarization API deployed on AWS ECR

## Hugging Face model

Following Hugging face model was used : [mrm8488/t5-base-finetuned-summarize-news](https://huggingface.co/mrm8488/t5-base-finetuned-summarize-news) :rocket:

## Model Description

The T5 model was presented in Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu

## How to Use

To load and save the model - 

```

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-summarize-news")

model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-summarize-news")

```

To Invoke the model from Hugging face - 

```

import requests

API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-summarize-news"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": "The answer to the universe is",
})

```
# AWS deployed ECR - Lambda function

The API is deployed and REST POST call was 200 OK

![image](https://user-images.githubusercontent.com/13203059/163491424-da4954db-2dd2-49e4-9632-b12b5a772f34.png)
