import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute the python file at the provided filepath",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Filepath of the python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Optional arguments given as strings",
                },
            },
            "required": [
                "file_path",
            ],
        },
    },
}

def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None
    ) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        is_target_valid = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        is_target_a_file = os.path.isfile(target_path)
        if not is_target_valid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not is_target_a_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", target_path]
            if args is not None: command.extend(args)
            completed_process = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
            output = ""
            if completed_process.returncode != 0: 
                output += f"Process exited with code {completed_process.returncode}\n"
            if completed_process.stdout == "" and completed_process.stderr == "":
                output += "No output produced\n"
            else:
                output += f"STDOUT: {completed_process.stdout}\n"
                output += f"STDERR: {completed_process.stderr}\n"
            return output
    except Exception as e:
        return f"Error: executing Python file: {e}"