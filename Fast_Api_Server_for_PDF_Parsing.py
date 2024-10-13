from typing import Annotated

from fastapi import FastAPI, File, UploadFile

import pdf_parsing as pp

app = FastAPI()

##This block will give the size if someone hits url http:127.0.0.1/files/
##app is the name of the application.
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

##This block will give the filename if someone hits url http:127.0.0.1/get_uploaded_file_name/
##app is the name of the application.
@app.post("/get_uploaded_file_name/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


##This block will receive the pdf file and write its content to a temporary file which will be consumed by downsteam application.
##In our case the downstream apllication id pdf_parding with the name pp.
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    ##Read File content ansynchronous manner else it will fail for large files
    content=await file.read()
    ##Get the filename of the file that will be uploaded by the client
    filename=file.filename
    
    print("filename")
    print(filename)
    ##Read the content of PDF and write it back to another PDF file on client side
    ##This received PDF will sent to for parsing.
    with open(filename,'wb') as handle:
        handle.write(content)
        
   
    ##this function immported from pdf_parsing package.
    ##It will parse the pdf and return back the parsed content in form of a dictionary
    parsed_pdf=pp.extract_text_images_tables('./'+filename)
    
    return {"parsed_pdf": parsed_pdf}