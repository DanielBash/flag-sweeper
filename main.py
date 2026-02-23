"""- Main launch file
-- Core launch
-- Flask server launch"""

# - importing modules
import core
import settings


# - app initialization
app = core.main.create_app()

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
