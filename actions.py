# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from corona_cases import Corona_cases

class ActionKoronaTurkey(Action):

    def name(self) -> Text:
        return "action_korona_turkey"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://www.worldometers.info/coronavirus/country/turkey/"

        cases = Corona_cases(url)
        dispatcher.utter_template('utter_korona_turkey', tracker, vaka=cases[0], olu=cases[1], iyilesen=cases[2])

        return []
