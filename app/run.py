"""File to run the app"""

from app import app

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
