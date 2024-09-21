def main(*no : list) -> int:
    return sum(*no)

values = [int(input("Enter Element: ")) for x in range(5)]



if __name__ == "__main__":
    print(main(values))