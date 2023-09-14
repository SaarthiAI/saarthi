from langchain.document_loaders import DirectoryLoader

def get_pdf_text(path: str) -> str:
    text = ""
    loader = DirectoryLoader(path, glob="*.pdf")
    for doc in loader.load():
        text += doc.page_content
    return text
