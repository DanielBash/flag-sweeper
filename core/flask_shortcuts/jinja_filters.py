"""- Quick jinja filters"""

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

for name, obj in globals().items():
    if name.startswith("filter_") and callable(obj):
        jinja_filters[name[7:]] = obj
