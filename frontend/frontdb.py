import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000/api/users"

st.title("User Management System")
menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Select Operation", menu)

if choice == "Create":
    st.subheader("Add Users")
    with st.form("add_user_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        submit_add = st.form_submit_button("Add User")

        if submit_add:
            payload = {
                "name": name,
                "email": email
            }
            res = requests.post(BASE_URL, json=payload)

            if res.status_code == 201:
                st.success("User added successfully")
                st.rerun()
            else:
                st.error("Failed to add user")

    st.divider()

if choice == "Read":
    st.subheader("View Users")
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        users = response.json()
        if users:
            for user in users:
                st.write(f"🆔 {user['id']} | 👤 {user['name']} | 📧 {user['email']}")
        else:
            st.info("No users found")
    else:
        st.error("Failed to fetch users")

    st.divider()

if choice == "Update":
    st.subheader("Update User")
    user_id = st.number_input("User ID", min_value=1, step=1)
    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")

    if st.button("Update User"):
        payload = {
            "name": new_name,
            "email": new_email
        }
        res = requests.put(f"{BASE_URL}/{user_id}", json=payload)
        if res.status_code == 200:
            st.success("User updated successfully")
            st.rerun()
        else:
            st.error("User not found or update failed")

    st.divider()

if choice == "Delete":
    st.subheader("Delete Employee")

    delete_id = st.number_input("User ID to Delete", min_value=1, step=1, key="delete")

    if st.button("Delete User"):
        res = requests.delete(f"{BASE_URL}/{delete_id}")

        if res.status_code == 200:
            st.success("User deleted successfully")
            st.rerun()
        else:
            st.error("User not found or delete failed")
