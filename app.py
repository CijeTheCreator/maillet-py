from flask import Flask, request, jsonify
import json
from parser import graph

app = Flask(__name__)


def generate_system_message(sender):
    system_message = f"""
    You are an email-based crypto wallet assistant.

    Your role is to interpret and fulfill user requests using the tools available to you.
    Take the sender email as: {sender}
    """
    return system_message


@app.route('/postmark-webhook', methods=['POST'])
def postmark_webhook():
    """
    Endpoint to receive Postmark webhooks and print the request body
    """
    received_email = request.get_json()
    print(received_email)


@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
