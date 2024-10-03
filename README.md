# HTML Gallery Generator

This Python script generates an HTML gallery of `.pdf` and image `.png`, `.jpeg`, `.jpg` files located in a specified folder. The gallery is displayed with thumbnail images and allows users to click on any image to view the full PDF in a new tab.

## Installation

Clone the repository or download the Python script:
   ```bash
   git clone https://github.com/your-username/html-gallery-generator.git
   cd html-gallery-generator
   ```

## Usage

To generate an HTML gallery, you need to pass the folder containing the input files as an argument. You can also specify the name of the HTML output file.

```bash
python html_gallery.py --path <input-folder> --htmlname <output-file-name>
```

### Arguments:
- `--path`: The folder containing the input files. Defaults to the current directory (`.`).
- `--htmlname`: The name of the generated HTML file. Defaults to `index.html`.

This command will create a folder `html` inside `my-pdfs`, copy all PDF files to `html/img`, and generate `gallery.html` inside the `html` folder.

## Folder Structure

- `html/` (automatically created):
  - `img/`: Folder containing the copied `.pdf` files.
  - `app.css`: CSS file for styling the HTML page.
  - `foundation.css`: Another CSS file for basic styling.
  - `gallery.html`: The generated HTML file.

## Customization

You can customize the following:
- The structure of the HTML file by editing the `htmlize` function.
- The CSS styling by modifying `app.css` and `foundation.css`.

