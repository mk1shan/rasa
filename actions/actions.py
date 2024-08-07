from typing import Any, Dict, List, Text, Optional
from rasa_sdk import Action, FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ValidateSurveyForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_survey_form"

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],  # Updated type hint
    ) -> Optional[List[Text]]:
        return slots_mapped_in_domain

class ActionShowAnswers(Action):
    def name(self) -> Text:
        return "action_show_answers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        answer1 = tracker.get_slot("answer1")
        answer2 = tracker.get_slot("answer2")
        answer3 = tracker.get_slot("answer3")
        answer4 = tracker.get_slot("answer4")
        answer5 = tracker.get_slot("answer5")

        # Print the answers in the console
        print(f"Answer 1: {answer1}")
        print(f"Answer 2: {answer2}")
        print(f"Answer 3: {answer3}")
        print(f"Answer 4: {answer4}")
        print(f"Answer 5: {answer5}")

        dispatcher.utter_message(text="Thank you for completing the survey!")

        return []
