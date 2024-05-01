teikums = "Skolā mācās daudz skolēni un strādā 223 skolotāji."
simbolu_skaits = len(teikums) - teikums.count(" ")
print(simbolu_skaits)

bez_atstarpēm = teikums.replace(" ", "")
bez_liekām_zīmēm = bez_atstarpēm.replace("," , "")
print
if bez_liekām_zīmēm.isdigit():
    print("Teikumā ir tikai cipari")
elif bez_liekām_zīmēm.isalpha():
    print("Teikumā ir burti.")
else:
    print("Teikumā ir cipari un burti.")

print(teikums)

vārds = "skola"
# Convert both the sentence and word to lowercase for case-insensitive comparison
lowercase_sentence = teikums.lower()
lowercase_word = vārds.lower()

# Check if the lowercase_word is in the lowercase_sentence
if lowercase_word in lowercase_sentence:
    print(f"'{vārds}' is in the sentence.")
else:
    print(f"'{vārds}' is not in the sentence.")

def find_first_and_last_occurrence(teikums, vārds):
    # Convert the sentence to lowercase to make the search case-insensitive
    teikums = teikums.lower()
    vārds = vārds.lower()

    first_occurrence = teikums.find(vārds)
    last_occurrence = teikums.find(vārds)

    if first_occurrence != -1:
        # Adjust the positions to match the original sentence
        first_occurrence = teikums[:first_occurrence].count(' ') + 1
        last_occurrence = teikums[:last_occurrence].count(' ') + 1

    return first_occurrence, last_occurrence

word_to_find = "skolā"
first, last = find_first_and_last_occurrence(teikums, word_to_find)

if first != -1:
    print(f"The first occurrence of '{word_to_find}' is at position {first}")
    print(f"The last occurrence of '{word_to_find}' is at position {last}")
else:
    print(f"'{word_to_find}' was not found in the sentence.")

def remove_diacritics(sentence):
    # Define a dictionary of diacritic characters and their replacements
    diacritics = {
        "ā":"a", "č":"c", "ē":"e", "ģ":"g", 
        "ī":"i", "ķ":"k","ļ":"l","ņ":"n","š":"s",
        "ū":"u","ž":"z",
    }

    # Replace diacritic characters with their ASCII equivalents
    for diacritic, replacement in diacritics.items():
        sentence = sentence.replace(diacritic, replacement)

    return sentence

# Example usage
modified_sentence = remove_diacritics(lowercase_sentence)

print(f"Orģinālais teikums: {lowercase_sentence}")
print(f"Izmainītais teikums: {modified_sentence}")

aizvietojamais_vards = "223"
aizvietojums = "400"

jauns_teikums = teikums.replace(aizvietojamais_vards,aizvietojums)
print(jauns_teikums)

def reverse_sentence(teikums):
    # Check if the sentence ends with a period
    if teikums.endswith("."):
        # Remove the period from the end of the sentence
        teikums = teikums[:-1]

        # Method 1: Reverse the sentence using slicing and 'cycle'
        reversed_sentence_cycle = teikums[::-1]

        # Method 2: Reverse the sentence using 'special team'
        words = teikums.split()
        reversed_sentence_special_comand = " ".join(words[::-1])

        return reversed_sentence_cycle, reversed_sentence_special_comand
    else:
        return "Teikums beidzās ar punktu."

reversed_cycle, reversed_special_team = reverse_sentence(teikums)

print("rģinālais teikums:", teikums)
if reversed_cycle != "Teikums nebeidzās ar punktu.":
    print("Apgriezts teikums (Cycle Method):", reversed_cycle)
    print("Apgriezts teikums (Special Comand Method):", reversed_special_team)
else:
    print(reversed_cycle)  # Sentence does not end with a period.


def reverse_and_replace(teikums):
    # Check if the sentence ends with a period
    if teikums.endswith("."):
        # Remove the period from the end of the sentence
        teikums = teikums[:-1]

        # Method 1: Reverse the sentence using slicing and 'cycle'
        reversed_sentence_cycle = teikums[::-1]

        # Method 2: Reverse the sentence using 'special team'
        words = teikums.split()
        reversed_sentence_special_team = " ".join(words[::-1])

        # Function to replace vowels with 'dog'
        def replace_vowels_with_dog(text):
            vowels = 'aeiouAEIOU'
            return ''.join('kaķis' if char in vowels else char for char in text)

        # Replace vowels with 'dog' in both reversed sentences
        reversed_sentence_cycle_dog = replace_vowels_with_dog(reversed_sentence_cycle)
        reversed_sentence_special_team_dog = replace_vowels_with_dog(reversed_sentence_special_team)

        return reversed_sentence_cycle_dog, reversed_sentence_special_team_dog
    else:
        return "Sentence does not end with a period."

# Example usage
reversed_cycle, reversed_special_team = reverse_and_replace(teikums)

print("Original Sentence:", teikums)

if reversed_cycle != "Sentence does not end with a period.":
    print("Reversed Sentence (Cycle Method):", reversed_cycle)
    print("Reversed Sentence (Special Team Method):", reversed_special_team)
else:
    print(reversed_cycle)  # Sentence does not end with a period.
