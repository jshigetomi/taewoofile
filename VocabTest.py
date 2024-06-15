from VocabularyClass import Vocabulary
import os

foldername = "./VocabFiles"
files = os.listdir(foldername)

for file in files:
    vocab = Vocabulary()
    vocab.initlist(foldername + "/" + file)
    vocab.test()