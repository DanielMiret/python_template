import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    dev_name = os.getenv("DEV_NAME")
    print(f"Dev name: {dev_name}")


if __name__ == "__main__":
    main()
