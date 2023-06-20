# PDF-merger
A quick Python script made following a YT [tutorial](https://youtu.be/vEQ8CXFWLZU?list=PLMocEdgPD9hOcynpyCn4Zhl91O3PBE80t&t=566) with a few modifications that I think make it a bit more user friendly. This is a straightforward way for me to quickly merge PDF files together, without having to rely on sketchy websites that require uploading files. 

## Requirements 
* Python 3.x: Ensure that Python 3.x is installed on your system before running the script.
* PyPDF2 Library: This script relies on the PyPDF2 library for PDF manipulation. Make sure you have it installed. If not, you can install it by running the following command:
```
pip3 install PyPDF2
``` 
## Usage
* Clone or download the script from the repository.
* Install the required dependencies by running the command mentioned in the "Requirements" section.
* Change the directory path in both the `pdf_merger.py` and `pdf-merger.sh` files
* Place the PDF files you want to merge in the `/pdf-files-to-merge` folder.
* Open a terminal or command prompt and navigate to the script's directory.
* Run the script by executing the following command:
```
zsh pdf-merger.sh
```
* Once the merging process is complete, the script will generate a new PDF file containing the merged documents in the ```/merged-pdf``` folder.

## Contributing
Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License, allowing you to modify, distribute, and use the script freely. Please refer to the license file for more information.

## Acknowledgments
The PyPDF2 library for providing a reliable and efficient solution for PDF manipulation in Python.

The open-source community for their continuous efforts in developing and maintaining high-quality software.

ChatGPT for generating the template for this README.md.
