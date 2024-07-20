import streamlit as st
import asyncio

async def main():
    st.markdown("# Taking inputs in Streamlit")
    st.markdown("### Also showing how a loading spinner works")

    # Text input
    text_input1 = st.text_input("Enter some text:", "Default text")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    text_input2 = st.text_input("Enter some text:")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Number input
    number1 = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    number2 = st.number_input("Enter a number:")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Slider
    slider_value1 = st.slider("Choose a value:", min_value=0, max_value=100, value=50)
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    slider_value2 = st.slider("Choose a value:")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space




    # Checkbox
    checkbox = st.checkbox("Check this box")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Radio buttons
    radio_option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Selectbox
    select_option = st.selectbox("Select from dropdown:", ["Choice A", "Choice B", "Choice C"])
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Multiselect
    multi_select = st.multiselect("Select multiple options:", ["Item 1", "Item 2", "Item 3", "Item 4"])
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Date input
    date = st.date_input("Select a date:")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Time input
    time = st.time_input("Select a time:")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # File uploader
    uploaded_file = st.file_uploader("Choose a file")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Color picker
    color = st.color_picker("Pick a color")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # Text area
    text_area1 = st.text_area("Enter multi-line text:", "Default\nmulti-line\ntext")
    text_area2 = st.text_area("Enter multi-line text:")
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space
    st.markdown("<br>", unsafe_allow_html=True)  # Add space

    # ... (rest of your input fields)

    # Button
    if st.button("Click me"):
        with st.spinner("Processing..."):  # Add a loading spinner
            await asyncio.sleep(2)  # Simulate some processing time
            st.success("Done!")

        # Display the inputs
        st.write("Text input 1:", text_input1)
        st.write("Text input 2:", text_input2)
        st.write("Number input 1:", number1)
        st.write("Number input 2:", number2)
        st.write("Slider value 1:", slider_value1)
        st.write("Slider value 2:", slider_value2)
        # ... (display other inputs)

if __name__ == "__main__":
    asyncio.run(main())