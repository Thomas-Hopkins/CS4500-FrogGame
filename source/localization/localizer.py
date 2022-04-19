AVAILABLE_LANGS = {"en": "English"}
CHOSEN_LANG = "en"
DEFAULT_LANG = "en"

__LANG_MODULES = {}
for lang in AVAILABLE_LANGS:
    __LANG_MODULES[lang] = __import__(
        f"localization.localizer_{lang}", {}, {}, ["localization"]
    )


def get(attr, lang=None):
    if not lang:
        # TODO: Replace with configuration lookup
        lang = CHOSEN_LANG

    try:
        text = getattr(__LANG_MODULES[lang], attr)
    except:
        text = getattr(__LANG_MODULES[DEFAULT_LANG], attr)
    return text
