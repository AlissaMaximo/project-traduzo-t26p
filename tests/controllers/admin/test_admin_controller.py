from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    UserModel(
        {
            "name": "Mafumafu",
            "token": "mafuteru",
        }
    ).save()

    tl_history = HistoryModel(
        {
            "text_to_translate": "Bottle",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    app_test.delete(
        f"/admin/history/{tl_history.data['_id']}",
        headers={
            "Authorization": "mafuteru",
            "User": "Mafumafu",
        },
    )

    assert HistoryModel.find_one({"_id": tl_history.data["_id"]}) is None
