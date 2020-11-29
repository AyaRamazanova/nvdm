from tqdm import tqdm

class Reader():
    def __init__(self, file_path: str, test: bool = False):
        self.test = test
        self.vocab = {}
        self.words_num = 0
        self.data = []
        self.word_count = []
        self.doc_ids = []
        print('READING')
        with open(file_path) as f:
            self.documents = f.read().split('\n')
        del self.documents[-1]
        print("SPLITTING TO WORDS")
        for i in tqdm(range(len(self.documents))):
            self.documents[i] = self.documents[i].split()
            self.doc_ids.append(self.documents[i][0])
            self.documents[i] = self.documents[i][1:]

        if self.test:
            with open('vocab.new') as f:
                vocab = f.read().split('\n')
            for pair in vocab:
                pair = pair.split()
                self.vocab[pair[0]] = int(pair[1])


    def covert2freq(self):
        print('CONVERTING TO FREQUENCIES')
        for document in tqdm(self.documents):
            doc = {}
            for word in document:
                if word not in self.vocab:
                    self.vocab[word] = self.words_num
                    self.words_num += 1
                vocab_index = self.vocab[word]
                doc[vocab_index] = 1 if vocab_index not in doc else doc[vocab_index] + 1
            self.data.append(doc)
            self.word_count.append(len(document))
        return self.data, self.word_count


    def dump(self, out_file):
        vocab = ''
        if not self.test:
            for word in self.vocab.keys():
                vocab += (word + ' ' + str(self.vocab[word]) + '\n')
            with open('vocab.new', 'w') as f_out:
                f_out.write(vocab)

        str_out = ''
        for document, doc_index in zip(self.data, self.doc_ids):
            str_out += doc_index
            for word_index in document.keys():
                str_out += (' ' + str(word_index) + ':' + str(document[word_index]))
            str_out += '\n'
        with open(out_file, 'w') as f_out:
            f_out.write(str_out)