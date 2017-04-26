import os
import argparse

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from top_n.utils.text import tokenize


def _get_text_files_in_path(input_corpus_path):
    everything = os.listdir(input_corpus_path)
    return [str(os.path.join(input_corpus_path, file_name)) for file_name in everything if file_name.endswith('.txt')]


def _fit_vectorizer(files):
    tf_idf = TfidfVectorizer(input='filename', ngram_range=(1, 3), stop_words='english', tokenizer=tokenize)
    tf_idf.fit(files)
    return tf_idf


def _generate_feature_name_lookup(vectorizer):
    feature_names = vectorizer.get_feature_names()
    features = pd.DataFrame(feature_names, columns=['feature_name'])
    return features


def main(input_corpus_path, top_n):
    files = _get_text_files_in_path(input_corpus_path)
    vectorizer = _fit_vectorizer(files)
    features = _generate_feature_name_lookup(vectorizer)
    for file in files:
        file_vectorized = vectorizer.transform([file, ])
        vectorization_array = file_vectorized.toarray()
        vectorization_df = pd.DataFrame(vectorization_array.T, columns=['rank'])
        display = vectorization_df.join(features).sort_values(by='rank', ascending=False)[:top_n]
        print(file, '\n', display, '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find top N (1-3) n-grams of a corpus')
    parser.add_argument('-i', '--input-path', type=str, help='Path to directory containing the corpus')
    parser.add_argument('-n', '--top-n', type=int, help='Number of top keywords to look for')
    args = parser.parse_args()
    main(args.input_path, args.top_n)
