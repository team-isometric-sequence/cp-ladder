from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from tailwind import get_config
from tailwind.utils import is_path_absolute


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "is_debug": settings.DEBUG,
            "tailwind": {
                "is_static_path": not is_path_absolute(get_config("TAILWIND_CSS_PATH")),
                "css_path": get_config("TAILWIND_CSS_PATH"),
            },
        }
    )
    return env
