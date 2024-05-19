# Color Converter

This project provides functionality to convert between RGB, Hex, and CMYK color formats. The user can input values for each format and receive the corresponding converted values.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example](#examples)
5. [License](#license)

## Features
- Convert RGB values to Hex and CMYK.
- Convert Hex values to RGB and CMYK.
- Convert CMYK values to RGB and Hex.
- Input validation to ensure values are within acceptable ranges:
  - RGB values: 0-255
  - Hex values: 7 characters starting with #
  - CMYK values: 0-100%

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Maw1z/Color-Converter.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Color-Converter
    ```

## Usage
1. Run the main script:
    ```sh
    python main.py
    ```
2. Follow the prompts to enter values for RGB, Hex, or CMYK as needed.

## Example

### Converting RGB to Hex 
```sh
Enter choice: 1
Enter R value: 100
Enter G value: 100
Enter B value: 100
The hexadecimal value for this color is: #646464
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
