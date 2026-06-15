import fitz



with fitz.open("basic-text.pdf") as pdf:
    """ 
    # Printing page by page and seperating each one with -
    for page in pdf:
        print(20*'-')
        print(page.get_text())
    """
    # This is one page of text from the pdf
    text = ''
    for page in pdf:
        text = text + page.get_text()
        print(text)