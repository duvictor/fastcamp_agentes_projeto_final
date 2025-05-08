import streamlit as st
import src.Util as utils



# from openai import OpenAI

def main():
    st.set_page_config("Chat Laudo")
    st.header("RAG De Laudos Médicos")

    textUtil = utils.TextUtil()

    user_question = st.text_input("Faça uma pergunta sobre os laudos médicos")

    if user_question:
        a = 45
        # user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_doc = st.file_uploader("Adicione seu laudo e clique no botão submeter", accept_multiple_files=False)
        if st.button("Submete"):
            with st.spinner("Processando o laudo..."):

                try:

                    for x in pdf_doc:
                        print(x)
                        temp_file = "./temp.pdf"
                        with open(temp_file, "wb") as file:
                            file.write(x.getvalue())
                            print(temp_file)

                            textUtil.process_pdf(temp_file, x.name)



                except Exception as e:
                    print(f'Interrupted by: {e}')
                    st.error(f'Interrupted by: {e}')

                st.success("Laudo Classificado com sucesso!")

if __name__ == "__main__":
    main()