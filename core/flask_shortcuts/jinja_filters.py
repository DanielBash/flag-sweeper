""" - All filters for jinja
 -- All filters MUST start with filter_
 -- All filters MUST be callable"""

# - importing modules
import markdown
from markupsafe import Markup


# -- filters
# - markdown filter
def filter_markdown(text):
    html = markdown.markdown(
        text,
        extensions=[
            "fenced_code",
            "codehilite",
            "tables",
            "nl2br",
            "sane_lists"
        ]
    )

    return Markup(html)


# - getting all filters together
jinja_filters = {}

for name in list(globals().keys()):
    if name.startswith("filter_") and callable(globals()[name]):
        jinja_filters[name[7:]] = globals()[name]
