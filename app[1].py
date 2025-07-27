import streamlit as st
from password_checker import check_password_strength

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if password:
    strength, remarks = check_password_strength(password)

    st.subheader("Strength Score:")
    st.progress(strength / 5)

    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    st.write(f"**Rating:** {levels[strength-1] if strength > 0 else 'Very Weak'}")

    if remarks:
        st.warning("Suggestions to improve your password:")
        for remark in remarks:
            st.markdown(f"- {remark}")
    else:
        st.success("Your password is strong!")
