
def read_conll_data(filepath):

    sentences = []
    tags = []
    
    sentence = []
    tag_seq = []

    with open(filepath , 'r') as f:

        for line in f:

            if line.strip() == "":

                if sentence:
                    sentences.append(sentence)
                    tags.append(tag_seq)

                    sentence = []
                    tag_seq = []

            else :
                sent = line.strip().split()
                word = sent[0]
                tag = sent[1]
                sentence.append(word)
                tag_seq.append(tag)

    for i , (s,t) in enumerate(zip(sentences,tags)):
        if len(s) != len(t):
            print(f'Mismatch in sent {i} : {len(s)} tokens , {len(t)} tags')

    return sentences , tags


def word2features(sent, i ):
    word = sent[i]

    features = {
            'bias':1.0,

            'suffix3':word[-3:],
            'suffix4':word[-4:],
            'wordlen':len(word),
            
            'word.isdigit()':word.isdigit(),
            }
    
    if i > 0:
        wordl = sent[i-1]
        features.update({
            '-1:word':wordl,
            })
    else:
        features['BOS'] =True

    if i < len(sent) -1:
        wordl = sent[i+1]
        features.update({
            '+1:word':wordl,
            })
    else:
        features['EOS'] = True

    return features

def sent2features(sent):
    return [word2features(sent,i) for i in range(len(sent)) ]

def sent2labels(tags):
    return tags

if __name__ == '__main__':
    filepath = 'data.txt'

    read_conll_data(filepath)

