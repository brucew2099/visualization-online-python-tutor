'''
Input:

- sys.argv[1] - filename of a doctest pickle file like lab1_doctests.pickle

Output:

- a JSON blob representing its contents, printed to stdout
'''

import pickle
import sys
import json
import traceback

def encode_doctest(t):
    encoded_examples = []
    encoded_test = {
        'docstring': t.docstring,
        'name': t.name,
        'filename': t.filename,
        'examples': encoded_examples,
    }

    encoded_examples.extend(
        dict(
            source=e.source, want=e.want, options=e.options, exc_msg=e.exc_msg
        )
        for e in t.examples
    )

    return encoded_test


if __name__ == "__main__":
    try:
        fullpath = sys.argv[1]
        assert fullpath.endswith(".pickle")
        with open(fullpath, 'rU') as f: # use 'U' to work on Windows
            tests = pickle.load(f)
            all_encoded_tests = [encode_doctest(t) for t in tests]
            print(json.dumps(all_encoded_tests, indent=2))
    except:
        print(json.dumps("ERROR in doctest_reader.py")) # print JSON to stdout
        traceback.print_exc()
