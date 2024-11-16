from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import magic

app = FastAPI(title="File Format Identifier API")

# Initialize libmagic
magic_instance = magic.Magic(mime=True)

@app.post("/identify-file")
async def identify_file(file: UploadFile = File(...)):
    try:
        # Read file content
        file_content = await file.read()
        # Determine MIME type
        mime_type = magic_instance.from_buffer(file_content)
        # Determine File type
        file_type = magic.Magic().from_buffer(file_content)
        return {
            "file_name": file.filename,
            "mime_type": mime_type,
            "file_type": file_type,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
