from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    UserModel(
        {
            "name": "Rogerio",
            "level": "admin",
            "token": "fdesded-dedsdwedwed-dwdwdwd",
        }
    ).save()
    HistoryModel(
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    id = HistoryModel.find_one(
        {
            "translate_to": "pt"
        }
    ).data["_id"]

    result = app_test.delete(
        f"/admin/history/{id}",
        headers={
            "Authorization": "fdesded-dedsdwedwed-dwdwdwd",
            "User": "Rogerio",
        },
    )
    assert result.status_code == 204
