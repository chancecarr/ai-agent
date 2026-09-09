from functions.run_python_file import run_python_file

def main() -> None:
    tests = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
        ("calculator", "lorem.txt"),
    ]
    for test in tests:
        result = run_python_file(*test)
        print(result)

if __name__ == "__main__":
    main()