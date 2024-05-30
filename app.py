import streamlit as st

def add_suffix(names):
    # Check if the input is a list
    if not isinstance(names, list):
        raise ValueError("Input must be a list of names.")
    
    # Check if each item in the list is a string
    if not all(isinstance(name, str) for name in names):
        raise ValueError("All items in the list must be strings.")
    
    # Add the suffix "actual" to each name
    names_with_suffix = [name + "sexual" for name in names]
    return names_with_suffix

# Streamlit app
st.title("FIND ASHU'S SEXUALITY")
st.write("We know that you are eager to know Ashu's sexuality")

# Input from user
names_input = st.text_area("Enter your name to know Ashu's Sexuality:")

if st.button("know the answer"):
    # Split input by commas and strip any whitespace
    names = [name.strip() for name in names_input.split(",") if name.strip()]

    if names:
        # Process names
        try:
            result = add_suffix(names)
            st.write("Ashu is:")
            for name in result:
                st.write(name)
        except ValueError as e:
            st.error(str(e))
    else:
        st.error("Please enter at least one name.")
