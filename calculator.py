def main():
    print(convert("hello world"))


def convert(text):
    return text.lower().replace(" ", "...")

if __name__ == "__main__":
   main()