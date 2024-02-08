

from flask import Blueprint, request, jsonify
from model.chat import nlp, process_question, knowledge_base, identify_question_intent

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    """
    Processes user input from the chat interface and returns a response.

    Returns:
        JSON: A dictionary containing the chatbot's response.
    """

    # Get user input from the POST request
    user_input = request.form['message']
    print(user_input)

    # Process the user input using spaCy
    doc = nlp(user_input)

    # Identify the user's question intent
    question_intent = identify_question_intent(doc)
    print(question_intent)

    # Generate a response based on the intent and knowledge base
    response = process_question(doc, knowledge_base, question_intent)
    print(response)

    # Return the response as JSON
    return jsonify({'response': response})
