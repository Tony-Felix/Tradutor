from deep_translator import GoogleTranslator
from flask import Blueprint, render_template, request

from models.language_model import LanguageModel
from models.history_model import HistoryModel


render_template_controller = Blueprint("render_template_controller", __name__)


@render_template_controller.route("/", methods=["GET", "POST"])
def index():
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"
    text_to_translate = "O que deseja traduzir?"

    if request.method == "POST":
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        text_to_translate = request.form.get("text-to-translate")
        translated = GoogleTranslator(
            source="auto", target=translate_to).translate(text_to_translate)
        HistoryModel(
            {
                "text": text_to_translate,
                "from": translate_from,
                "to": translate_to,
            }
        ).save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@render_template_controller.route("/reverse", methods=["POST"])
def index_reverse():
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    text_to_translate = request.form.get("text-to-translate")
    translated = GoogleTranslator(
        source="auto", target=translate_to).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
