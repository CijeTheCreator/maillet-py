from datetime import datetime, timezone
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, DynamicTemplateData

from dotenv import load_dotenv

load_dotenv()


ethtousd = os.environ["ETH_RATE"]


def send_balance_email(recipient_email: str, address: str, eth_amount: str, date: str):
    eth_value = ethtousd * float(eth_amount)
    date = get_date()
    message_data = {
        "address": address,
        "eth_amount": f"{eth_amount} ETH",
        "eth_value": eth_value,
        "date": date,
        "network": "Sepolia Testnet"
    }

    message = Mail(
        from_email=From("transactions@maillet.tech",
                        name="Maillet"),
        to_emails=To(recipient_email),
    )

    message.template_id = "d-345032b89250417291e75411e5d5a118"
    message.dynamic_template_data = message_data

    try:
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")


def send_confirmation_email(recipient_email: str, sender_address: str, beneficiary_address: str, eth_amount: str, transaction_id: str):

    message_data = {
        "amount": f"{eth_amount} ETH",
        "to": beneficiary_address,
        "txid": transaction_id,
        "date": get_date(),
        "network": "Sepolia Testnet"
    }

    message = Mail(
        from_email=From("transactions@maillet.tech",
                        name="Maillet"),
        to_emails=To(recipient_email),
    )

    message.template_id = "d-e7e3b35d0cbd4f8faab7b3620e7a30a2"
    message.dynamic_template_data = message_data

    try:
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")


def send_failure_email(recipient_email: str, sender_address: str, beneficiary_address: str, eth_amount: str, transaction_id: str, reason: str):

    message_data = {
        "amount": f"{eth_amount} ETH",
        "to": beneficiary_address,
        "txid": transaction_id,
        "reason": reason,
        "date": get_date(),
        "network": "Sepolia Testnet"
    }

    message = Mail(
        from_email=From("transactions@maillet.tech",
                        name="Maillet"),
        to_emails=To(recipient_email),
    )

    message.template_id = "d-df42ce379fe64144841c15a8ffb06178"
    message.dynamic_template_data = message_data

    try:
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")


def get_date():
    now_utc = datetime.now(timezone.utc)
    formatted = now_utc.strftime('%B %-d, %Y, %H:%M UTC')
    return formatted
