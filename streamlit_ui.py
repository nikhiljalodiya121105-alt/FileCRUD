from pathlib import Path
import os
import streamlit as st

st.set_page_config(page_title="CRUD File Manager", layout="centered")

st.title("📂 CRUD File Manager")

# ---------------- SHOW FILES ---------------- #

def show_files():
    p = Path('')
    items = list(p.rglob('*'))

    st.subheader("Files & Folders")

    for index, file in enumerate(items):
        st.write(f"{index+1} - {file}")

# ---------------- CREATE FILE ---------------- #

def create_file():
    st.subheader("Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("FILE ALREADY EXISTS!")

        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("FILE CREATED!")

# ---------------- READ FILE ---------------- #

def read_file():
    st.subheader("Read File")

    file_name = st.text_input("Enter file name to read")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists() and p.is_file():

            with open(file_name, 'r') as file:
                st.text(file.read())

        else:
            st.error("FILE NOT FOUND!")

# ---------------- UPDATE FILE ---------------- #

def update_file():
    st.subheader("Update File")

    file_name = st.text_input("Enter file name to update")

    option = st.radio(
        "Choose update type",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            if option == "Overwrite":

                with open(file_name, 'w') as file:
                    file.write(content)

            elif option == "Append":

                with open(file_name, 'a') as file:
                    file.write("\n" + content)

            st.success("FILE UPDATED!")

        else:
            st.error("FILE NOT FOUND!")

# ---------------- DELETE FILE ---------------- #

def delete_file():
    st.subheader("Delete File")

    file_name = st.text_input("Enter file name to delete")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)

            st.success("FILE DELETED!")

        else:
            st.error("FILE NOT FOUND!")

# ---------------- RENAME FILE ---------------- #

def rename_file():
    st.subheader("Rename File")

    old_name = st.text_input("Enter old file name")

    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)

            st.success("FILE RENAMED!")

        else:
            st.error("FILE NOT FOUND!")

# ---------------- CREATE FOLDER ---------------- #

def create_folder():
    st.subheader("Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():

            st.error("FOLDER ALREADY EXISTS!")

        else:

            p.mkdir()

            st.success("FOLDER CREATED!")

# ---------------- DELETE FOLDER ---------------- #

def delete_folder():
    st.subheader("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            p.rmdir()

            st.success("FOLDER DELETED!")

        else:
            st.error("FOLDER NOT FOUND!")

# ---------------- SIDEBAR MENU ---------------- #

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Show Files",
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

if menu == "Show Files":
    show_files()

elif menu == "Create File":
    create_file()

elif menu == "Read File":
    read_file()

elif menu == "Update File":
    update_file()

elif menu == "Delete File":
    delete_file()

elif menu == "Rename File":
    rename_file()

elif menu == "Create Folder":
    create_folder()

elif menu == "Delete Folder":
    delete_folder()