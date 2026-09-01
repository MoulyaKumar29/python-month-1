import os
import shutil


SOURCE_FOLDER = "OrganizedFiles"


def create_folders():
    folders = [
        "Images",
        "Documents",
        "TextFiles",
        "PythonFiles",
        "Others"
    ]

    for folder in folders:
        path = os.path.join(SOURCE_FOLDER, folder)
        os.makedirs(path, exist_ok=True)


def organize_files():
    create_folders()

    for filename in os.listdir(SOURCE_FOLDER):

        source_path = os.path.join(SOURCE_FOLDER, filename)

        if not os.path.isfile(source_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            destination_folder = "Images"

        elif extension in [".pdf", ".doc", ".docx", ".xlsx"]:
            destination_folder = "Documents"

        elif extension == ".txt":
            destination_folder = "TextFiles"

        elif extension == ".py":
            destination_folder = "PythonFiles"

        else:
            destination_folder = "Others"

        destination_path = os.path.join(
            SOURCE_FOLDER,
            destination_folder,
            filename
        )

        shutil.move(source_path, destination_path)

    print("Files organized successfully.")


if __name__ == "__main__":
    organize_files()