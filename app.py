import streamlit as st
import src.Util as utils
import src.QdrantConection as qc


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
        if st.button("Submeter"):
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

        try:
            a = 45
            count_especialidade = qc.get_count("especialidade")
            count_modalidade = qc.get_count("modalidade")
            count_total = qc.get_count("id")
        except Exception as e:
            print(f'Interrupted by: {e}')
            st.error(f'Interrupted by: {e}')

        # st.markdown("# Seção Principal 1")
        # st.markdown("## Seção Principal 2")
        st.markdown(f"### Quantidade de Laudos: {count_total}")
        # opcao1 = st.checkbox("Opção 1")
        # opcao2 = st.selectbox("Escolha uma opção", ["A", "B", "C"])
        #
        # st.markdown("---")  # Adiciona uma linha divisória
        #
        # st.markdown("**Filtros Avançados**")
        # slider1 = st.slider("Faixa de valores", 0, 100, (25, 75))


if __name__ == "__main__":
    main()