import argparse
import os
import glob
from shutil import copy
from pathlib import Path

def htmlize(path, output):
    """
    Generate an HTML gallery from an input folder, supporting PDFs and image files.

    Parameters
    ----------
    path : str
        Path to the input folder containing files to be included in the gallery.
    output : str
        Path to the output HTML file.
    """
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="robots" content="noindex">
        <meta name="googlebot" content="noindex">
        <title>Gallery</title>
        <link rel="stylesheet" href="foundation.css">
        <link rel="stylesheet" href="app.css">
    </head>
    <body>
        <div class="grid-container">
            <div class="grid-x grid-padding-x">
                <div id="Home" class="large-12 cell">
                    <div class="callout secondary">
                        <h3><center>Summary Plots</center></h3>
                        <div class="grid-x grid-padding-x">
    """

    # List of supported file types
    supported_extensions = ["*.pdf", "*.png", "*.jpg", "*.jpeg"]

    # Loop through all supported files in the folder and add them to the HTML
    for extension in supported_extensions:
        for file in sorted(Path(path).glob(extension)):
            file_name = file.name
            file_extension = file.suffix.lower()

            # Check if it's an image or PDF, and render accordingly
            if file_extension in ['.png', '.jpg', '.jpeg']:
                # Display the image
                html_template += f"""
                    <div class="large-6 cell">
                        <div class="callout">
                            <center>
                                <h5><b>{file_name}</b></h5>
                                <hr/>
                                <a href='./img/{file_name}' target='_blank'>
                                    <img src='./img/{file_name}' width='300'/>
                                </a>
                            </center>
                        </div>
                    </div>
                """
            elif file_extension == '.pdf':
                # Display a thumbnail for the PDF
                html_template += f"""
                    <div class="large-6 cell">
                        <div class="callout">
                            <center>
                                <h5><b>{file_name}</b></h5>
                                <hr/>
                                <a href='./img/{file_name}' target='_blank'>
                                    <img src='./img/pdf-thumbnail.png' alt='PDF Thumbnail' width='300'/>
                                </a>
                            </center>
                        </div>
                    </div>
                """

    html_template += """
                        </div>
                    </div>
                </div>
            </div>
            <footer class="grid-x grid-padding-x">
                <div class="large-12 cell">
                    <hr/>
                    <div class="large-6 cell">
                        <p>&copy; 2021 - G. GILLES</p>
                    </div>
                </div>
            </footer>
        </div>
    </body>
    </html>
    """

    # Write the HTML content to the output file
    with open(output, "w") as f:
        f.write(html_template)


def main():
    parser = argparse.ArgumentParser(description="Generate an HTML gallery from an input folder")
    parser.add_argument("--path", type=str, default=".", help="Input folder path")
    parser.add_argument("--htmlname", type=str, default="index.html", help="Output HTML file name")
    args = parser.parse_args()

    input_path = Path(args.path)
    html_output_dir = input_path / "html"
    img_dir = html_output_dir / "img"

    # Create necessary directories
    try:
        html_output_dir.mkdir(parents=True, exist_ok=True)
        img_dir.mkdir(exist_ok=True)
    except Exception as e:
        print(f"Error creating directories: {e}")
        return

    # Copy CSS/JS files
    try:
        current_dir = Path(__file__).parent
        css_js_dir = current_dir / "../css"
        copy(css_js_dir / "app.js", html_output_dir)
        copy(css_js_dir / "foundation.css", html_output_dir)
    except Exception as e:
        print(f"Error copying CSS/JS files: {e}")
        return

    # Copy supported files (.pdf, .png, .jpg, .jpeg) to img folder
    try:
        supported_extensions = ["*.pdf", "*.png", "*.jpg", "*.jpeg"]
        for extension in supported_extensions:
            for file in input_path.glob(extension):
                copy(file, img_dir / file.name)
    except Exception as e:
        print(f"Error copying files: {e}")
        return

    # Generate HTML gallery
    htmlize(img_dir, html_output_dir / args.htmlname)


if __name__ == "__main__":
    main()
