from functions.get_files_info import get_files_info

def main() -> None:
    tests = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../"),
    ]
    
    for test in tests:
        result = get_files_info(*test)
        print(f"Result for {"current" if test[1] == "." else f"'{test[1]}'"} directory:")
        if "Error" in result.split()[0]:
            print(f"    {result}")
        else:
            lines = result.split("\n")
            for line in lines:
                print(f"  {line}")

if __name__ == "__main__":
    main()