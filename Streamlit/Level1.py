
'''
Getting started with streamlit
st.write, st.text, st.markdown
Displaying code with st.code, st.latex
'''

import streamlit as st
import asyncio
import time


async def main():
    st.title("My first streamlit app")


    # st.text
    st.text("This is plain text using st.text")

    #st write
    st.write("This is how st.write gets displayed")


    # st.markdown
    st.markdown("# This is a markdown header")
    st.markdown("You can use **bold** or *italic* text.")
    st.markdown("- List item 1\n- List item 2\n- List item 3")



    # st.code
    code_example = '''
    def hello_world():
        print("Hello, World!")

    hello_world()
    '''
    st.code(code_example, language='python')


if __name__ =="__main__":
    asyncio.run(main())