import random

# Define a seed
seed = 12345
random.seed(seed)

# Agora os números aleatórios serão sempre os mesmos
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.choice(['espada', 'arco', 'escudo']))