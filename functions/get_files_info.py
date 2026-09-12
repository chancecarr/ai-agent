import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, directory))
        is_target_valid = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        is_target_a_dir = os.path.isdir(target_path)
        if not is_target_valid: 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not is_target_a_dir:
            return f'Error: "{directory}" is not a directory'
        else:
            files_info_lst: list[str] = []
            for item in os.listdir(target_path):
                item_path = os.path.join(target_path, item)
                size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                files_info_lst.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
            return "\n".join(files_info_lst)
    except Exception as e:
            return f"Error: {e}"
