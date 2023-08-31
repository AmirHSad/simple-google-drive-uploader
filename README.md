<a name="readme-top"></a>
[![LinkedIn][linkedin-shield]][linkedin-url]
[![MIT License][license-shield]][license-url]


<br />
<div align="center">
  <h3 align="center">Simple Google Drive Uploader</h3>

  <p align="center">
    A simple project to upload a file on your Google Drive using Python.
    It gives you a concept and you can customize it for your projects.
    <br />
    <a href="https://github.com/AmirHSad/simple-google-drive-uploader/issues">Report Bug</a>
  </p>
</div>


## Getting Started

### Prerequisites
First, you need to get an OAuth 2.0 for Google Service API, which you can read Step 2 of the following link to do that:
</br>
[How to Upload File to Google Drive using Python Script?](https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python)
</br>
Place your 'client_secrets.json' file path as value of client_secrets_file inside upload_basic.py

### Installation and Usage
1. Clone the repo
   ```sh
   git clone https://github.com/AmirHSad/simple-google-drive-uploader.git
   ```
2. Go to project directory, create and activate a virtual environment and install python requirements
    ```sh
    cd simple-google-drive-uploader

    python3 -m vevn venv
    source venv/bin/activate

    pip3 install -r requirements.txt
    ```
3. Place your 'client_secrets.json' file path as value of client_secrets_file inside upload_basic.py
    ```python
    client_secrets_file = 'path/to/client_secret_xxxxxxxxxxxx.json'
    ```
4. Run the script
   ```sh
   python3 upload_basic.py <file_to_be_uploaded>
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [How to Upload File to Google Drive using Python Script?](https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python)
* [Upload file to google drive using Python](https://www.codespeedy.com/upload-file-to-google-drive-using-python/)
* [Google APIs & Services](https://console.cloud.google.com/apis/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[license-shield]: https://img.shields.io/github/license/AmirHSad/simple-google-drive-uploader.svg?style=for-the-badge
[license-url]: https://github.com/AmirHSad/simple-google-drive-uploader/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/amirhsad/
[product-screenshot]: images/screenshot.png