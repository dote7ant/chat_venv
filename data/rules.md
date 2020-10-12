## rule: Say goodbye anytime the user says goodbye
* goodbye
  - utter_goodbye

## rule: Say 'I am a bot' anytime the user challenges
* bot_challenge
  - utter_iamabot

## rule: Ask the user to rephrase whenever they send a message with low NLU confidence
* nlu_fallback
  - utter_ask_rephrase

## rule: out-of-scope
* out_of_scope
  - utter_out_of_scope
