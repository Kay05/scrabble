import json
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Load the word dictionary from a JSON file
with open('word_converter/word_dict.json', 'r') as f:
    word_dict = json.load(f)

def random_word(start, length):
    words = word_dict.get(start, {}).get(str(length), [])  # JSON keys are always strings
    return random.choice(words) if words else None

@csrf_exempt
def convert_sentence(request):
    if request.method == 'POST':
        # sentence = request.POST.get('sentence', '')
        data = json.loads(request.body)
        sentence = data['sentence']
        print(sentence);
        words = sentence.split()
        transformed_words = []
        for word in words:
            new_word = random_word(word[0].lower(), len(word))
            transformed_words.append(new_word if new_word else word)
        return JsonResponse({'original': sentence, 'converted': ' '.join(transformed_words)})
    return JsonResponse({'error': 'Invalid method'}, status=400)
