##version: "2.0"

stories:

- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy

- story: sad path 1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy

- story: sad path 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_did_that_help
  - intent: deny
  - action: utter_goodbye

- story: happy path 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_employment
  - action: utter_faqs_employment
  - intent: affirm
  - action: utter_affirm

- story: employment
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_employment
  - action: utter_faqs_employment

- story: certificates
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_certificates
  - action: utter_faqs_certificates

- story: appointments
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_appointments
  - action: utter_faqs_appointments

- story: accommodation
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_accommodation
  - action: utter_faqs_accommodation

- story: International 
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_international_students
  - action: utter_faqs_international_students


- story: remote learning
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_remote_learning
  - action: utter_faqs_remote_learning

- story: core
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_core
  - action: utter_faqs_core

- story: job
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_job
  - action: utter_faqs_job

- story: financial_aid
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_financial_aid
  - action: utter_faqs_financial_aid

- story: programming
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_programming
  - action: utter_faqs_programming

- story: scholarship
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_scholarship
  - action: utter_faqs_scholarship

- story: cert
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_cert_completion 
  - action: utter_faqs_cert_completion 

- story: diff
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_diff
  - action: utter_faqs_diff

- story: classes
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_classes
  - action: utter_faqs_classes

- story: moringa
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_moringa
  - action: utter_faqs_moringa

- story: payments
  steps:
  - intent: greet
  - action: utter_greet
  - intent: pay
  - action: utter_pay

- story: faqs payments
  steps:
  - intent: greet
  - action: utter_greet
  - intent: faqs_payments
  - action: utter_faqs_payments

- story: installments
  steps:
  - intent: greet
  - action: utter_greet
  - intent: installments
  - action: utter_faqs_payment_installments

- story: full paymemt
  steps:
  - intent: greet
  - action: utter_greet
  - intent: full_
  - action: utter_faqs_payment_full

- story: classes 
  steps:
  - intent: faqs_classes
  - action: utter_faqs_classes

- story: employment 1
  steps:
  - intent: faqs_employment
  - action: utter_faqs_employment

- story: certificates 1
  steps:
  - intent: faqs_certificates
  - action: utter_faqs_certificates

- story: appointments 1
  steps:
  - intent: faqs_appointments
  - action: utter_faqs_appointments

- story: accommodation 1
  steps:
  - intent: faqs_accommodation
  - action: utter_faqs_accommodation

- story: International 1
  steps:
  - intent: faqs_international_students
  - action: utter_faqs_international_students


- story: remote learning 1
  steps:
  - intent: faqs_remote_learning
  - action: utter_faqs_remote_learning

- story: core 1
  steps:
  - intent: faqs_core
  - action: utter_faqs_core

- story: job 1
  steps:
  - intent: faqs_job
  - action: utter_faqs_job

- story: financial_aid 1
  steps:
  - intent: faqs_financial_aid
  - action: utter_faqs_financial_aid

- story: programming 1
  steps:
  - intent: faqs_programming
  - action: utter_faqs_programming

- story: scholarship 1
  steps:
  - intent: faqs_scholarship
  - action: utter_faqs_scholarship

- story: cert 1
  steps:
  - intent: faqs_cert_completion 
  - action: utter_faqs_cert_completion 

- story: diff 1
  steps:
  - intent: faqs_diff
  - action: utter_faqs_diff

- story: moringa 1
  steps:
  - intent: faqs_moringa
  - action: utter_faqs_moringa

- story: payments 1
  steps:
  - intent: pay
  - action: utter_pay

- story: faqs payments 1
  steps:
  - intent: faqs_payments
  - action: utter_faqs_payments

- story: installments 1
  steps:
  - intent: installments
  - action: utter_faqs_payment_installments

- story: full paymemt 1
  steps:
  - intent: full_
  - action: utter_faqs_payment_full
