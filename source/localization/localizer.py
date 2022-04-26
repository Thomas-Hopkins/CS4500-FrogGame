from configuration.config import Config

# Each key corresponds to a "localizer_XX.py" file in /localization/ The values are the user facing string
AVAILABLE_LANGS = {"en": "English"}
# Python doesn't have a 2-way mapping. Use this if you need to get lang abbrv from string
AVAILABLE_LANGS_REVERSED = dict((reversed(item) for item in AVAILABLE_LANGS.items()))
DEFAULT_LANG = "en"

__LANG_MODULES = {}
for lang in AVAILABLE_LANGS:
    __LANG_MODULES[lang] = __import__(
        f"localization.localizer_{lang}", {}, {}, ["localization"]
    )


def get(attr, lang=None):
    if not lang:
        lang = Config.get("language")

    try:
        text = getattr(__LANG_MODULES[lang], attr)
    except:
        text = getattr(__LANG_MODULES[DEFAULT_LANG], attr)
    return text
