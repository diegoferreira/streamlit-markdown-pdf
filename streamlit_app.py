import streamlit as st
from fpdf import FPDF
import markdown2
from io import BytesIO

# Configuração da página do Streamlit
st.title("Conversor de Markdown para PDF")

# Entrada de texto em Markdown
markdown_text = st.text_area("Insira seu texto em Markdown aqui:")

# Função para converter Markdown em PDF
def convert_markdown_to_pdf(md_text):
    try:
        # Converter Markdown para HTML
        html = markdown2.markdown(md_text)

        # Criar um objeto PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Adicionar o conteúdo HTML ao PDF
        pdf.write_html(html)  # Usar write_html para adicionar o conteúdo formatado

        # Salvar o PDF em um buffer
        pdf_buffer = BytesIO()
        pdf_bytes = pdf.output(dest='S')  # Retorna um bytearray
        pdf_buffer.write(pdf_bytes)  # Escreve o bytearray no buffer
        pdf_buffer.seek(0)  # Volta ao início do buffer
        return pdf_buffer
    except Exception as e:
        st.error(f"Erro ao converter Markdown para PDF: {e}")
        return None

# Botão para gerar o PDF
if st.button("Gerar PDF"):
    if markdown_text:
        pdf_buffer = convert_markdown_to_pdf(markdown_text)
        if pdf_buffer:
            st.download_button(
                label="Baixar PDF",
                data=pdf_buffer,
                file_name="output.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Por favor, insira algum texto em Markdown.")
