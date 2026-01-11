"""Retrieve iFixit guide"""

from typing import Optional
import requests

IFIXIT_API_URL = 'https://www.ifixit.com/api/2.0'

def retrieve_guide(guide_id: int) -> Optional[dict]:
    """
    Used to retrieve guide from the iFixit API

    The returning dictionary contains:

    - ``title`` (str): Guide title
    - ``steps`` (dict): Guide steps
    - ``summary`` (str): Summary of the guide
    - ``type`` (str): Type of the guide
    - ``conclusion`` (str): Guide conclusion
    - ``difficulty`` (str): Guide difficulty
    - ``introduction`` (str): Guide introduction
    - ``image_id`` (int): ID of main image in Guide
    - ``guide_id`` (int): Guide ID

    The ``steps`` dictionary contains:

    - ``title`` (str): Step title
    - ``text`` (str): The text of the step
    - ``image_id`` (list): List of image IDs the step uses

    :param guide_id: the ID of the guide to retrieve
    :type guide_id: int

    :return: guide dictionary
    :rtype: dict or None
    """

    request_url = f"{IFIXIT_API_URL}/guides/{guide_id}"

    response = requests.get(request_url, allow_redirects=False, timeout=5)

    if response.status_code != 200:
        return {}

    if 'application/json' not in response.headers.get('Content-Type', ''):
        return {}

    response_json = response.json()

    steps = []

    for _step in response_json.get('steps', []):
        lines = []
        image_ids = []
        for _line in _step.get('lines', []):
            if _line.get('text_raw'):
                lines.append(_line.get('text_raw'))

        step_data_type = _step.get('media').get('type')

        if step_data_type and step_data_type == 'image':
            for _data in _step.get('media').get('data', []):
                image_ids.append(_data.get('id'))

        step_instance = {"title": _step.get('title'),
                         "text": " ".join(lines),
                         "image_id": image_ids}

        steps.append(step_instance)


    return {
        "title": response_json.get("title"),
        "steps": steps,
        "summary": response_json.get("summary"),
        "type": response_json.get("type"),
        "conclusion": response_json.get("conclusion_raw"),
        "difficulty": response_json.get("difficulty"),
        "introduction": response_json.get("introduction_raw"),
        "image_id": response_json.get("image").get("id"),
        "guide_id": response_json.get("guideid")
    }
