import pathlib
from uuid import uuid4

def file_generate_name(original_file_name):
    extension = pathlib.Path(original_file_name).suffix

    return f"{uuid4().hex}{extension}"
