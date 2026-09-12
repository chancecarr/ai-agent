import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write provided content to the specified file. This will overwrite pre-existing content.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Filepath of the file to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to be written to the specified file",
                },
            },
            "required": [
                "file_path",
                "content",
            ],
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        is_target_valid = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        is_target_a_dir = os.path.isdir(target_path)
        if not is_target_valid:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif is_target_a_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"