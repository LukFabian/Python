"""
Long term project: Trying to simulate different encryptions and also their decryptions and possible attacks on them within python.
More encryption methods will be added in the future!
Uses built-in module: string
"""
import string


class Cypher:
    def __init__(self, key, plaintext):
        self.key = key
        self.plaintext = plaintext

    def choose_encryption(self):
        if encrypt == "c":
            key = input("Please enter the shift in the alphabet (1-25)\n")
            start_encrypt = Cypher(key, plain)
            print(Cypher.Caesar_cipher(start_encrypt))

    def Caesar_cipher(self):
        cyphertext = ""
        int_alphabet = CypherMethods.createDictionary(self)
        for word in single_word_plain:
            for letter in word:
                current_plain = int_alphabet.get(letter)
                try:
                    cipher_int = int(current_plain) + int(self.key)
                    if cipher_int > 25 and letter.islower():
                        cipher_int = cipher_int - 26
                    elif cipher_int > 51 and letter.isupper():
                        cipher_int = cipher_int - 26
                except TypeError:
                    cyphertext = cyphertext + letter
                    continue
                for key, value in int_alphabet.items():
                    if value == cipher_int:
                        cyphertext = cyphertext + key
            cyphertext = cyphertext + " "
        return cyphertext

    def choose_decryption(self):
        if decrypt_module == "c":
            key = input('If you already have the key (shift in the alphabet, number from 1-25), please enter it.\n'
                        'Otherwise, just press "Enter"\n')
            try:
                start_decrypt = Cypher(key, cipher_text)
                print(Cypher.Caesar_decrypt_key(start_decrypt))
            except ValueError:
                Cypher.Caesar_bruteforce(start_decrypt)
            except:
                print("Bad input.")
                Cypher.choose_decryption(decrypt_module)
        else:
            print("Bad input, exiting.")
            quit()

    def Caesar_decrypt_key(self):
        plaintext = ""
        int_alphabet = CypherMethods.createDictionary(self)
        for word in single_word_cipher:
            for letter in word:
                current_cipher = int_alphabet.get(letter)
                try:
                    plain_int = int(current_cipher) - int(self.key)
                    if plain_int < 0 and letter.islower():
                        plain_int = plain_int + 26
                    elif plain_int < 26 and letter.isupper():
                        plain_int = plain_int + 26
                except TypeError:
                    plaintext = plaintext + letter
                    continue
                for key, value in int_alphabet.items():
                    if value == plain_int:
                        plaintext = plaintext + key
            plaintext = plaintext + " "
        return plaintext

    def Caesar_bruteforce(self):
        print("Trying to bruteforce the Caesar Cipher")
        iteration = 0
        count = 0
        range_count = -1
        brute_plain = []
        nice_brute = []
        brute_results = ""
        # Create dictionary with numbered alphabet
        for word in single_word_cipher:
            iteration = iteration + 1
            bruteforce = CypherMethods.bruteforce(self, word)
            brute_plain.append(bruteforce)
        for brute_word in brute_plain:
            word_count = 0
            range_count = range_count + 1
            for i in range(len(brute_plain[range_count])):
                nice_brute.append(brute_word[word_count])
                word_count = word_count + 1
                # append to nice_brute the letters of brute_plain
        range_count = -1
        for brute_word in brute_plain:
            brute_results = brute_results + "\n{}.word: \n".format(range_count + 2)
            # for every word
            range_count = range_count + 1
            current_word = len(brute_plain[range_count]) / 25
            for i in range(25):
                # 25 times
                for c in range(int(current_word)):
                    brute_results = brute_results + nice_brute[count]
                    count = count + 1
                brute_results = brute_results + "\n"
        print(brute_results)


class CypherMethods:
    def __init__(self):
        self.self = self

    def createDictionary(self):
        count = 0
        int_alphabet = {}
        alphabet = string.ascii_letters
        for alphabet in list(alphabet):
            for letter in alphabet:
                int_alphabet.update({letter: count})
                count = count + 1
        return int_alphabet

    def bruteforce(self, word):
        plaintext = ""
        start_count = 0
        brute_count = 0
        capital_alphabet = string.ascii_uppercase
        lower_alphabet = string.ascii_lowercase
        capital_int_alphabet = {}
        lower_int_alphabet = {}
        for i in range(25):
            brute_count = brute_count + 1
            for letter in word:
                if str(letter).isupper() is True:
                    for alphabet_letter in list(capital_alphabet):
                        capital_int_alphabet.update({start_count: alphabet_letter})
                        start_count = start_count + 1
                    start_count = 0
                    for key, value in capital_int_alphabet.items():
                        if letter in value:
                            starting_key = key
                            try:
                                plaintext = plaintext + capital_int_alphabet.get(int(starting_key) + brute_count)
                            except TypeError:
                                modular = capital_int_alphabet.get(
                                    int(starting_key) + brute_count - len(capital_int_alphabet))
                                plaintext = plaintext + modular
                            break
                else:
                    for alphabet_letter in list(lower_alphabet):
                        lower_int_alphabet.update({start_count: alphabet_letter})
                        start_count = start_count + 1
                    start_count = 0
                    for key, value in lower_int_alphabet.items():
                        if letter in value:
                            starting_key = key
                            try:
                                plaintext = plaintext + lower_int_alphabet.get(int(starting_key) + brute_count)
                            except TypeError:
                                modular = lower_int_alphabet.get(int(starting_key) + brute_count - len(lower_int_alphabet))
                                plaintext = plaintext + modular
                            break
        return plaintext


Choose_module = input('Do you want to encrypt or decrypt a message?\n Please enter "e" to encrypt or "d" to decrypt:\n')
if Choose_module == "e":
    plain = input("Please enter the message you want to encrypt:\n")
    single_word_plain = plain.split()
    encrypt = input('Please enter "c" for the Caesar_cipher:\n')
    Cypher.choose_encryption(encrypt)
elif Choose_module == "d":
    cipher_text = input("Please enter/paste the message you want to decrypt:\n")
    single_word_cipher = cipher_text.split()
    decrypt_module = input('Please enter "c" if you want to decrypt with the "Caesar_cypher"\n')
    Cypher.choose_decryption(decrypt_module)

else:
    print('Please enter a correct message, exiting.', quit())
