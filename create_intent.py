import argparse
import json

from google.cloud import dialogflow


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This script adds more intents to the Agent'
    )
    parser.add_argument('json_file', help="enter your json file")
    args = parser.parse_args()
    with open(args.json_file, 'r') as file:
        questions_json = file.read()
    questions = json.loads(questions_json)
    for key, value in questions.items():
        create_intent(
            'tg-bot-lesson-3',
            key,
            value['questions'],
            [value['answer']]
        )
