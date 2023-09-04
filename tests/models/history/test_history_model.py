import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_data = HistoryModel.list_as_json()
    parsed = json.loads(history_data)

    assert len(parsed) == 2
    assert parsed[0]["text_to_translate"] == "Hello, I like videogame"
    assert parsed[0]["translate_to"] == "pt"
    assert parsed[0]["translate_from"] == "en"
