from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/postmark-webhook', methods=['POST'])
def postmark_webhook():
    """
    Endpoint to receive Postmark webhooks and print the request body
    """
    try:
        # Get the raw request data
        raw_data = request.get_data(as_text=True)

        # Print the raw body
        print("=== Postmark Webhook Received ===")
        print("Raw body:")
        print(raw_data)
        print("=" * 35)

        # Try to parse as JSON for prettier output
        try:
            json_data = request.get_json()
            if json_data:
                print("Parsed JSON:")
                print(json.dumps(json_data, indent=2))
                print("=" * 35)
        except Exception as e:
            print(f"Could not parse as JSON: {e}")

        # Print headers for debugging
        print("Headers:")
        for header, value in request.headers:
            print(f"{header}: {value}")
        print("=" * 35)

        # Return a success response
        return jsonify({"status": "success", "message": "Webhook received"}), 200

    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
