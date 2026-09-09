import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        is_target_valid = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        is_target_a_file = os.path.isfile(target_path)
        if not is_target_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not is_target_a_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(target_path, "r") as f:
                content = f.read(MAX_CHARS)
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return content
    except Exception as e:
        return f"Error: {e}"
