from collections import defaultdict
import random

game_scores = defaultdict(list)

friends = ['Etaash','Fabian','Jayden']

for g in friends:
    for x in range(0,10):
        score = random.randrange(100000)
        game_scores[g].append(score)

print(game_scores)

for k,v in game_scores.items():
    if k == 'Etaash':
        print(f'The highest score for Etaash is...{max(v)}')







