# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



"""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import logging 
from datetime import datetime

import requests
import json
from api import handoff
import reports 
#import rationing
# import apis
#rom bill import Bills_API

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk import sqlite3
#from rasa_sdk import EntityFormField, FormAction
#from sqlite3 import Error
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused, ConversationResumed, AllSlotsReset

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

class ActionKB(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        knowledge_base.set_representation_function_of_object(
           "rationing", lambda obj: obj["Location"]  + " " + "(" + obj["Zone"] + " - " + obj["day"] + ")"
        )
        
        super().__init__(knowledge_base)

# Feedback action
class FeedBackForm(FormAction):
    def name(self):
        return "feedback_Form"
    @staticmethod
    def required_slots(tracker):
        return ["feedback", "negative_feedback_reason"]

# FAQS action    
class ActionFaqs(Action):
    def name(self):
        return "action_faqs"
    
    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        # retrive correct utterance dependent on the intent
        if intent in [
         "FAQS_billing",
         "FAQS_complaint",
         "FAQS_corruption",
         "FAQS_dirty_water",
         "FAQS_disconnections",
         "FAQS_expensive_reports",
         "FAQS_faulty_meter",
         "FAQS_new_connection",
         "FAQS_read_meter",
         "FAQS_reconnection",
         "FAQS_servicing",
         "FAQS_tanker",
         "FAQS_time_to_conn",
        ]:
            dispatcher.utter_template("utter_" + intent, tracker) 
        return []

# Report action
class ActionReports(Action):
    def name(self):
        return "action_reports"
    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        if intent in ["complaints"]:
            dispatcher.utter_template("utter_comp", tracker)
            if intent in action_water:
                dispatcher.utter_message("call this")
                
                elif intent in action_billing:
            
                    elif intent in action_meter:
            
                        elif intent in action_leak:

                            elif intent in action_accounts
                
            return []
        


# Action human handoff
class ActionHandoff(Action):
    def name(self):
        return "action_human_handoff"
    
    def run(self, dispatcher, tracker, domain):
        response = "Reaching out to a human agent[{}]...".format(tracker.sender_id)
        dispatcher.utter_message(response)

        tracker._paused = True
        message = " "

        while message != "/unpause":
            url = "http://127.0.0.1:5000/handoff/{}".format(tracker.sender_id)
            req = requests.get(url)
            resp = json.loads(req.text)
            if "error" in resp:
                raise Exception("Error fetching message: " + repr(resp["error"]))
            message = resp["message"]
            if message != "/unpause":
                dispatcher.utter_message("Human agent: {}".format(message))
        
        tracker._paused = False
        
    

class ActionSlot(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]

"""