import streamlit as st



def main():
    st.set_page_config(page_title="Hỏi đáp với kho tài liệu PDFs", page_icon=":books:")

    st.header("Hỏi đáp với kho tài liệu PDFs :books:")
    st.text_input("Hỏi đáp với tài liệu")

    with st.sidebar:
        st.subheader("Tài liệu của bạn")
        st.file_uploader("Tải tài liệu của bạn và nhấn 'Xử lý'")
        st.button("Xử lý")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
