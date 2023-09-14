from dotenv import load_dotenv

from utils import load_ui, get_text_chunks, get_pdf_text

def main():
    load_dotenv()
    raw_text = get_pdf_text(path="./dataset")

if __name__ == "__main__":
    main()
