# from transformers import AutoModelForQuestionAnswering, AutoTokenizer

from transformers import AutoTokenizer, AutoModelWithLMHead

# tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-summarize-news")

# model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-summarize-news")

def get_model(model):
  """Loads model from Hugginface model hub"""
  try:
    model = AutoModelWithLMHead.from_pretrained(model)
    model.save_pretrained('../model')
  except Exception as e:
    raise(e)

def get_tokenizer(tokenizer):
  """Loads tokenizer from Hugginface model hub"""
  try:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer)
    tokenizer.save_pretrained('../model')
  except Exception as e:
    raise(e)

get_model('mrm8488/t5-base-finetuned-summarize-news')
get_tokenizer('mrm8488/t5-base-finetuned-summarize-news')