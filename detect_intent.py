from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, texts, language_code, sm='tg'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    if type(texts) is str:
        texts = [texts,]

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
        if sm == 'vk':
            if response.query_result.intent.is_fallback:
                return
            else:
                return response.query_result.fulfillment_text
        else:
            return response.query_result.fulfillment_text
