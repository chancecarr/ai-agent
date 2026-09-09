from functions.write_file import write_file

def main() -> None:
    tests = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed"),
    ]
    for test in tests:
        result = write_file(*test)
        print(result)

if __name__ == "__main__":
    main()