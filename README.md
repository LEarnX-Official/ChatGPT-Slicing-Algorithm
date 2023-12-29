
# ChatGPT Slicing Algorithm and Text Generator

Welcome to the ChatGPT Slicing Algorithm and Text Generator repository! This project offers two powerful tools to enhance your text processing capabilities.

## ChatGPT Slicing Algorithm

### Overview

The ChatGPT Slicing Algorithm is an advanced utility designed to optimize the interaction with the ChatGPT 3.5 model. With the ability to handle inputs exceeding a standard size of 128 MB, this algorithm intelligently slices large inputs into manageable chunks that fit within the context window. Key features include:

- **Overlap:** Two slices can overlap, ensuring a smooth transition between consecutive slices.
- **Inclusion:** No slice is included in another, preserving the integrity of each segment.
- **Distinctiveness:** Adjacent slices must be different enough, as determined by cosine distance.

### Getting Started

#### Requirements

- Python 3
- NLTK library
- scikit-learn library

Install the necessary libraries using the following command:

```bash
pip install nltk scikit-learn

Usage:-
Clone the repository:

git clone https://github.com/yourusername/ChatGPT-Slicing-Algorithm.git
cd ChatGPT-Slicing-Algorithm

Run the program:

python3 final.py
Input the path to your text file when prompted.

Program Components
final.py: The main Python script containing the slicing algorithm.
sample_text.txt: An example input text file for testing.


Text Generator
Overview
The Text Generator is a versatile Bash script designed to facilitate the creation of large text files with customizable content. Whether you need to generate a sample_text.txt file or create custom text for various applications, this script provides an efficient solution.

Usage:
Make the script executable:

chmod +x create2.sh
chmod +x create3.sh

Before Run the script create a empty txt file and add the path or file name in BASH script.

Run the script:

./create2.sh(For create file in MB)
./create3.sh(For Create file in KB)
Script Details
Bash script to generate a large text file with customizable content.
Customization
Adjust the script variables (output_file and desired_size) to tailor the generated text to your needs. The script fetches text data until the specified file size is reached.


