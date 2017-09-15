import json

import ananas
from posify import POSifiedText

class Wellsy(ananas.PineappleBot):
    def start(self):
        with open('corpus.json') as f:
            self.corpus = POSifiedText.from_json(json.load(f))

    @ananas.hourly(minute=48)
    def post(self):
        sentence = self.corpus.make_sentence()
        self.mastodon.toot(sentence)
