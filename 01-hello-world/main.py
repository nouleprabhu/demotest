import platform
import datetime

def print_welcome_message():
    print("🚀 Welcomedfd to GitHub Actions Workshop!")
    print(f"📅 Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💻 Running on: {platform.system()} {platform.release()}")

if __name__ == "__main__":
    print_welcome_message()
