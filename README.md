Code for ranking top N (1-3) ngrams of a given corpus

# Installation

1- Create a *python 3* virtualenv for the project

    $ mkvirtualenv top_n -p /usr/bin/python3

3- Install the required dependencies

    (top_n)$ pip install -r requirements.txt

3- Run the script with the right arguments: path of the directory containing the corpus, top N to look for

    (top_n)$ PYTHONPATH=. python top_n/run.py -i /path/to/corpus/directory -n 20
