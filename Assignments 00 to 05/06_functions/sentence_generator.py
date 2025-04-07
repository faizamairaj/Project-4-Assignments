def make_sentence(word, partofspeech):
    sentence = [
    f"I am excited to add this {word} to my vast collection of them!",
    f"It's so nice outside today it makes me want to {word}!",
    f"Looking out my window, the sky is big and {word}!"
]

    print(sentence[partofspeech] if 0 <= partofspeech <= 2 else "part of speech must be 0, 1, 0r 2 can't make a sentence.")

def main():
    word = (input("Please type a noun, verb, or adjective: "))
    partofspeech = int (input("type 0 for noun, 1 for verb, or 2 for adjective:"))
    make_sentence(word, partofspeech)

main()


