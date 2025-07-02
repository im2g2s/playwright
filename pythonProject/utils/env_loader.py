import importlib
from utils.config import ENV

def load_profile():
    try:
        profile_module = importlib.import_module(f"Profiles.{ENV}")
        return profile_module
    except ModuleNotFoundError:
        raise ImportError(f"Profile module for environment '{ENV}' not found.")
