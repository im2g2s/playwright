import importlib
import inspect
from utils.config import ENV
import sys
import os

def test_copy_profile_data(source_env, target_file="Profiles/ENTProfile.py"):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    # Dynamically import the source module
    source_module = importlib.import_module(f"Profiles.{source_env}")

    # Extract non-dunder, non-module attributes
    attributes = {
        name: value for name, value in vars(source_module).items()
        if not name.startswith("__") and not inspect.ismodule(value)
    }

    # Write attributes to the target file
    with open(target_file, "w") as f:
        f.write("# Auto-generated profile file\n\n")
        for name, value in attributes.items():
            if isinstance(value, str):
                f.write(f'{name} = "{value}"\n')
            else:
                f.write(f"{name} = {value}\n")

    print(f"✅ Copied data from {source_env} to {target_file}")


# Execute the function
test_copy_profile_data(ENV)
