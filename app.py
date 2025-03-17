import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

score = 0
messages = []

if password:
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password must be **at least 8 characters** long.")  

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Password should contain **both uppercase and lowercase** letters.")
    
    if re.search("[0-9]", password):
        score += 1
    else:
        messages.append("❌ Password should contain **at least one number (0-9)**.")   

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include **at least one special character** (!@#$%^&*).")

 
    if messages:
        st.markdown("### 🔍 Suggestions:")
        for msg in messages:
            st.markdown(f"- {msg}")

    
    if score == 4:
        st.success("✅ **Strong Password!** Your password meets all security requirements.")
    elif score == 3:
        st.warning("⚠️ **Fair Password** – Consider making it stronger by adding special characters, numbers, or increasing its length.")
    else:
        st.error("❌ **Weak Password** – Improve security by using a mix of uppercase, lowercase, numbers, and symbols.")

else:
    st.info("🔹 **Enter a password to check its strength.**")
