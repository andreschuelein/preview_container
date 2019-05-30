from preview_generator.manager import PreviewManager
import time


cache_path = '/var/preview-cache'
source_document = '/var/data/MARBLES.TIF'

manager = PreviewManager('/var/preview-cache/', create_folder=True)

# preview_path = manager.get_pdf_preview(
# source_document, force=True)
preview_path = manager.get_jpeg_preview(
    source_document, height=1000, width=1000, force=True)

# has_pdf_preview
# get_pdf_preview

# has_jpeg_preview
# get_jpeg_preview
# get_jpeg_preview(source_document,height=100,width=50)

# has_text_preview
# get_text_preview

# has_json_preview
# get_json_preview

# has_html_preview
# get_html_preview

# get_page_nb
# get_mimetype
print('')
print('original document : ', source_document)
print('has_pdf_preview  : ', manager.has_pdf_preview(source_document))
print('has_jpeg_preview : ', manager.has_jpeg_preview(source_document))
print('has_text_preview : ', manager.has_text_preview(source_document))
print('has_json_preview : ', manager.has_json_preview(source_document))
print('has_html_preview : ', manager.has_html_preview(source_document))
print('Preview created at path : ', preview_path)
