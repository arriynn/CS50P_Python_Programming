import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link:=re.search(r"www\.youtube\.com/embed/(.*?)\"", s):
        return f"https://youtu.be/{link.group(1)}"
    
    else:
        return None


if __name__ == "__main__":
    main()
