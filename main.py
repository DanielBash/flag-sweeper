"""- Main launch file
-- Core launch
-- Flask server launch"""

# - importing modules
from core.core import create_app
import settings


# - app initialization
app = create_app(__name__)

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
