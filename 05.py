def censor(text):
    censored_words = ["Java", "C#", "Ruby", "PHP"]
    words_in_text = text.split()
    ret = None

    for i in range(len(words_in_text)):
        for censored_word in censored_words:
            if words_in_text[i] == censored_word:
                words_in_text[i] = "****"

    return ' '.join(words_in_text)


print(censor("PHP on website, Ruby on rails..."))
