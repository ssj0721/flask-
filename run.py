from src import create_app
import os

app = create_app()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8808))
    app.run(port=port)
