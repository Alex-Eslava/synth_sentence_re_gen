import re 
import random 
import numpy as np
import pandas as pd

# Templating imports
from sentence_templates import *
from template_variables import LOCATION, NAME, QUESTION

config_file = 'config.yml'
# Setting defaults
seed = 2022
template_to_use = 'example_templates'
avg_repetitions = 10
variance = 3
out_path = 'synth.csv'
# Loading config if exists
try: 
    import yaml
    with open(config_file, "r") as stream:
        config = yaml.safe_load(config_file)
        seed = config.get("seed", seed)
        template_to_use = config.get("template_to_use", template_to_use)
        avg_repetitions = config.get("avg_repetitions", avg_repetitions)
        variance = config.get("variance", variance)
        out_path = config.get("out_path", out_path)
    print("Config loaded, non-specified values are set to default...")
except: 
    print("Couldn't load config, going for default values...")


np.random.seed(seed)
random.seed(seed)
synthesized = []

templates = eval(template_to_use)

for n in range(len(templates)):
    n_repetitions_per_template = randint(avg_repetitions-variance, avg_repetitions+variance)
    for j in range(n_repetitions_per_template):
        sentence = templates[n]
        keys_to_keep =[key.replace("$","") for key in re.findall("[$]\w+", sentence)]
        for key in keys_to_keep: 
            word_to_fill = np.random.choice(eval(key))
            sentence = sentence.replace(f"${str(key)}", word_to_fill)
        synthesized.append(sentence)

print(f"we generated {len(synthesized)} synthetic sentences---->")

df = pd.DataFrame(synthesized, columns=['sentences'])
df.to_csv(out_path, sep='|')