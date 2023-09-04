from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    text_to_translate = "O que deseja traduzir"
    translated_from = "PT"
    translate_to = "EN"
    translated = "Tradução"

    if request.method == "POST":
        translated_from = request.form["translate-from"]
        translate_to = request.form["translate-to"]
        text_to_translate = request.form["text-to-translate"]
        translated = GoogleTranslator(
            source=translated_from, target=translate_to
        ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translated_from=translated_from,
        translated_to=translate_to,
        translated=translated,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
