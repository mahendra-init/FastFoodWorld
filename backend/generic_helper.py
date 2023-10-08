# Author: Dhaval Patel. Codebasics YouTube Channel

import re
import logging

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""


def intent_log(session_id: str, intent: str):
    # Configure logging
    logging.basicConfig(filename='intentfile.log', level=logging.INFO, format='%(asctime)s | %(message)s')

    # Log the message with timestamp, session ID, and intent
    log_message = f'{session_id} | {intent}'
    logging.info(log_message)