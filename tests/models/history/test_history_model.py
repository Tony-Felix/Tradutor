import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    result_list_json = HistoryModel.list_as_json()
    result_list_python = json.loads(result_list_json)

    assert len(result_list_python) == 2
    assert result_list_python[1]["text_to_translate"] == "Do you love music?"
    assert result_list_python[1]["translate_from"] == "en"
    assert result_list_python[1]["translate_to"] == "pt"
