import argparse
import openai

parser = argparse.ArgumentParser(description='Translate a sentence into action and object.')
parser.add_argument('sentence', type=str, help='The sentence to translate.')
args = parser.parse_args()
sentence = args.sentence

openai.api_key = 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

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Translate the sentence into action and object, for example a sentence 'move that cup' should be 'Action: move; Object: cup'. Now please translate " + sentence,
  max_tokens=100
)

text = response['choices'][0]['text']

action = text.split("Action: ")[1].split(";")[0].strip()
obj = text.split("Object: ")[1].strip()
objf = obj.replace(".", "")

print(action)
print(objf)
cost = response['usage']['total_tokens']
print("cost would be " + str(cost))

