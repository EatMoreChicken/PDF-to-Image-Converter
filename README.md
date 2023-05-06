# 🖼 PDF to PNG Converter
## 📌 Description
This script converts PDF files to PNG images using the PyMuPDF library.

## 🔒 Prerequisites
- Python 3
- PyMuPDF library (installed automatically during the installation process)

## 🚀 Installation
1. Install [Python3](https://www.python.org/downloads/).
2. Install the required packages by running `pip install -r requirements.txt`.
3. Configure `config.ini` (see configuration explanation below).
4. Create the `import_directory` you specified in the configuration file (If you changed it from default).

## 🔧 Configuration
The script is configured using the `config.ini` file. This file contains the following options:

```ini
[PDFS]
import_directory = import-pdfs
export_directory = export-images
enable_log_file = true
log_file = pdf-to-png-converter.log
```

- `import_directory`: The directory where the PDF files to be converted are stored.
- `export_directory`: The directory where the resulting PNG images will be saved.
- `enable_log_file`: Whether to enable logging to a file. Valid values are `true` or `false`.
- `log_file`: The name of the file where the log will be saved (if `enable_log_file` is set to true). This file will be created in the same directory as the script.

## 🎉 Features
- Converts PDF files in a specified directory into PNG images.
- Images are stored in separate folders created for each PDF (configured in the `config.ini` file).
- The script will batch process all PDFs in the `import_directory` (configured in the `config.ini` file).

## ⚒ Usage
1. Add PDFs to the `import_directory` you specified in the configuration file (the default folder name is `import-pdfs`).
2. Run the script using the command `python pdf-to-png-converter.py`.
3. The resulting PNG images will be saved in the directory you specified in the `config.ini` file (the default folder name is `export-images`).

## 📃 To-Do
- [ ] Support more image formats

## 🤝 Contributing
Please feel free to contribute to this project by creating pull requests, filing bug reports, or providing feedback.