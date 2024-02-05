import subprocess

prerequisites = ["pandas", "tqdm", "tkinter", "customtkinter", "ntscraper", "openpyxl"]

try:
    for i in prerequisites:
        subprocess.call(f"pip install {i}")
        print(f"installing package {i}")

except Exception as ex:
    print(ex)

print("INSTALLATION(S) COMPLETED")
