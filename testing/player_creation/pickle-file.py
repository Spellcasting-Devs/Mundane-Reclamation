import pickle


player_data = {
    'name': 'username',
    'health' : 100,
    'mana': 100,
    'strentgh': 100,
    }

with open("player_file.pickle", 'wb') as f:
    pickle.dump(player_data, f)