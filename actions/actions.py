from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class TicketQueryAction(Action):

    def name(self) -> Text:
        return "action_ticket_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = []
        for entity in tracker.latest_message["entities"]:
            entities.append(
                {
                    'entity': entity['entity'],
                    'value': entity['value'],
                    'role': entity.get('role')
                }
            )

        msg = str(entities) + "\n"

        dispatcher.utter_message(text=msg)

        return []


class DrinkQueryAction(Action):

    def name(self) -> Text:
        return "action_drink_response"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        msg = ""
        entities = []
        for entity in tracker.latest_message["entities"]:
            if entity.get('group') == "1":
                entities.append(
                    {
                        "entity": entity["entity"],
                        "value": entity["value"],
                        "group": entity["group"]
                    }
                )

        msg += "group #1: " + str(entities) + "\n"
        entities = []

        for entity in tracker.latest_message["entities"]:
            if entity.get("group") == "2":
                entities.append(
                    {
                        "entity": entity["entity"],
                        "value": entity["value"],
                        "group": entity["group"]
                    }
                )
        msg += "group #2: " + str(entities)
        dispatcher.utter_message(text=msg)

        return []