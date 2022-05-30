from dotenv import load_dotenv, find_dotenv, dotenv_values
import sys
import os

try:
    dotenv_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'ENV', '.env'))  # travels up a level to find the .env
    load_dotenv(dotenv_path)
except OSError:
    raise IOError('Failed open/read file: .env')
    sys.exit()
