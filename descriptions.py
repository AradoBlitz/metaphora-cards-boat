import os

greeting_dir = os.getenv('GREETING_DIR')

greeting = ''
with open(greeting_dir + "/greeting.txt") as greetingFile:
    greeting = greetingFile.read()
    greetingFile.close()

method_description = ''
with open(greeting_dir + "/method_description.txt") as methodDescriptionFile:
    method_description = methodDescriptionFile.read()
    methodDescriptionFile.close()

how_to_form_question_description = ''
with open(greeting_dir + "/how_to_form_question_description.txt") as howToFormQuestionDescriptionFile:
    how_to_form_question_description = howToFormQuestionDescriptionFile.read()
    howToFormQuestionDescriptionFile.close()


how_to_interpitated_card_description = ''
with open(greeting_dir + "/how_to_interpitated_card_description.txt") as howToInterpitatedCardDescriptionFile:
    how_to_interpitated_card_description = howToInterpitatedCardDescriptionFile.read()
    howToInterpitatedCardDescriptionFile.close()
