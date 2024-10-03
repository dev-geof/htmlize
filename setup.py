import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="htmlize",
    version="0.0.1",
    author="Geoffrey Gilles",
    description="A script to generate HTML galleries for PDFs, PNGs, and JPEG/JPG images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-geof/htmlize",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'htmlize=html_gallery:main',  # Create a command-line tool called htmlize
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
