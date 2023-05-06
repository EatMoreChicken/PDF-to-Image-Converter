import fitz
import os
import logging
import configparser
from datetime import datetime

def load_config():
    # Load configuration from INI file
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def setup_logging(config):
    # Set up logging
    enable_log_file = config.getboolean('PDFS', 'enable_log_file', fallback=False)
    log_file = config.get('PDFS', 'log_file', fallback='pdf-to-png.log')
    log_level = logging.DEBUG if enable_log_file else logging.INFO

    logging.basicConfig(filename=log_file, level=log_level, format='%(asctime)s [%(levelname)s] %(message)s')

def get_input_and_output_dirs(config):
    # Set input and output directories
    input_dir = config.get('PDFS', 'import_directory', fallback='pdfs')
    output_dir = config.get('PDFS', 'output_directory', fallback='exports')
    return input_dir, output_dir

def get_pdf_files(input_dir):
    # Get PDF files in input directory
    pdf_files = [pdf_file for pdf_file in os.listdir(input_dir) if pdf_file.endswith('.pdf')]
    return pdf_files

def process_pdf_file(pdf_file, input_dir, output_dir):
    # Open the PDF file
    pdf_path = os.path.join(input_dir, pdf_file)
    doc = fitz.open(pdf_path)

    # Generate the PNG directory name
    png_dir_name = os.path.splitext(pdf_file)[0]
    png_dir = os.path.join(output_dir, png_dir_name)

    # Check if the PNG directory already exists
    if os.path.exists(png_dir):
        # If the directory exists, find the next available directory name with a number suffix
        i = 2
        while True:
            new_png_dir_name = f"{png_dir_name}-{i}"
            new_png_dir = os.path.join(output_dir, new_png_dir_name)
            if not os.path.exists(new_png_dir):
                png_dir = new_png_dir
                break
            i += 1

    # Create the PNG directory
    os.makedirs(png_dir, exist_ok=True)

    # Loop through each page of the PDF file and save it as a PNG image
    for page_idx in range(doc.page_count):
        # Get the current page
        page = doc[page_idx]

        # Render the page as a PNG image
        pix = page.get_pixmap()

        # Generate the output file name
        output_file = os.path.join(png_dir, f"{png_dir_name}-{page_idx+1}.png")

        # Save the image as a PNG file
        pix.save(output_file)

        # Log the file save operation
        logging.info(f'Saved PNG file: {output_file}')

        # Print progress to the screen
        progress = (page_idx + 1) / doc.page_count * 100
        print(f'{pdf_file}, page {page_idx+1}/{doc.page_count}: {progress:.1f}%')

    # Close the PDF file
    doc.close()

    # Log the completion of the PDF processing
    logging.info(f'Completed processing PDF file: {pdf_file}')

def process_all_pdf_files(input_dir, output_dir):
    # Loop through all PDF files in the input directory
    for idx, pdf_file in enumerate(get_pdf_files(input_dir)):
        process_pdf_file(pdf_file, input_dir, output_dir)

    # Log the completion of the script
    logging.info('Completed processing all PDF files.')

def main():
    config = load_config()
    setup_logging(config)
    input_dir, output_dir = get_input_and_output_dirs(config)
    process_all_pdf_files(input_dir, output_dir)

if __name__ == '__main__':
    main()