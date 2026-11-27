"""Copies the phrases used on the guide pages out of the app's content.

Run after the app content changes:
    python export_phrases.py [path to vLearning/assets/content]
Writes guides_phrases.json, which build.py reads. No dependencies.
"""
import json
import os
import sys

from guides import GUIDES

DEFAULT_SRC = os.path.join('..', 'vLearning', 'assets', 'content')


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, DEFAULT_SRC)
    out = {}
    for g in GUIDES:
        for spec in g['tables']:
            mode, topic = spec[1], spec[2]
            key = f'{mode}/{topic}'
            if key in out:
                continue
            with open(os.path.join(src, mode, 'items', topic + '.json'), encoding='utf8') as f:
                items = json.load(f)
            out[key] = []
            for x in items:
                row = {'vi': x['vi'], 'en': x['en']}
                south = (x.get('dialectText') or {}).get('south')
                if south:
                    row['south'] = south
                out[key].append(row)
    with open(os.path.join(here, 'guides_phrases.json'), 'w', encoding='utf8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'exported {len(out)} topics')


if __name__ == '__main__':
    main()
