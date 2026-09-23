from langchain_community.document_loaders import PyPDFLoader, TextLoader
from streamlit import pdf
pdf_loader = PyPDFLoader("docs/Mechatronics_tutorials.pdf")
pdf_docs = pdf_loader.load()
# One document per page , with page number in metadata

# text_loader = TextLoader("how.txt")
# text_docs = text_loader.load()
print(f"Loaded {len(pdf_docs)} pages from the PDF")
print(pdf_docs[0].metadata)
print(f"Printing the pdf docs: {pdf_docs}")