# Store here all considered values

## Generic
LOCATION = ['Barcelona', 'London', 'Paris', 'Berlin']

NAME = ['James', 'Fam', 'Doe', 'John']

## larger Variable
sentence_start = [
    "Who",
    "What",
]
sentence_verb = [
        "does",
        "is",
        "combines",
]
sentence_end = [
        "this",
        "that",
]
first_cross = [' '.join([y, x]) for x, y in product(sentence_start, sentence_verb)]
all_questions =  [' '.join([y, x]) for x, y in product(first_cross, sentence_end)]
QUESTION = all_questions

    