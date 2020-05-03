import random
from typing import Dict, List

LIFE: Dict[str, List[str]] = {  # Copyright: Wikipedia
    'Born': ['Michael Joseph Jackson', 'August 29, 1958', 'Gary, Indiana, U.S.'],
    'Died': ['June 25, 2009 (aged 50)', 'Los Angeles, California, U.S.'],
    'Cause of death': ['Cardiac arrest induced by acute propofol and benzodiazepine intoxication', 'Buried',
                       'Forest Lawn Memorial Park, Glendale, California, U.S.'],
    'Other names': ['Michael Joe Jackson'], 'Occupation': ['Singer', 'Songwriter', 'Dancer'],
    'Spouse(s)': ['Lisa Marie Presley', '(m. 1994; div. 1996)', 'Debbie Rowe', '(m. 1996; div. 1999)'],
    'Children': ['Michael Jr', 'Paris', 'Prince', 'Michael II'], 'Parent(s)': ['Joe Jackson', 'Katherine Jackson'],
    'Family': ['Jackson family'],
    'Awards': ['https://en.wikipedia.org/wiki/List_of_awards_and_nominations_received_by_Michael_Jackson'],
    'Genres': ['Pop', 'Soul', 'Funk', 'Rhythm and blues', 'Rock',
               'Disco', 'Post-disco', 'Dance-pop', 'New jack swing'],
    'Instruments': ['Vocals'], 'Years active': ['1964–2009'],
    'Labels': ['Steeltown', 'Motown', 'Epic', 'Legacy', 'Sony', 'MJJ Productions'],
    'Associated acts': ['The Jackson 5'], 'Website': ['www.michaeljackson.com']
}


def get_random_info() -> str:
    key = random.choice(list(LIFE.keys()))
    value = ' '.join(LIFE[key])
    return f'{key}: {value}'
