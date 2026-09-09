from functions.get_file_content import get_file_content

def main() -> None:
    tests = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py"),

    ]
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    for test in tests:
        result = get_file_content(*test)
        print(result)

if __name__ == "__main__":
    main()