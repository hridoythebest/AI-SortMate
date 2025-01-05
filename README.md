# AI-SortMate

# AI-Enhanced Image Filter App

This is an AI-powered image filtering application designed to categorize and filter images by brand and category. It leverages Google Gemini API for image analysis and provides a graphical user interface (GUI) for easy interaction. 

## Features

- **Image Analysis**: Utilizes Google Gemini API to analyze images and extract relevant labels.
- **Filtering**: Filter images based on brand and category using metadata.
- **Batch Processing**: Move filtered images to a selected directory.
- **Asynchronous Operations**: Efficiently handles long-running tasks using async/await.
- **User-Friendly GUI**: Simple and intuitive interface built with Tkinter.

## Prerequisites

- Python 3.8 or higher
- Google Gemini API Key
- Necessary Python libraries: `pandas`, `tkinter`, `shutil`, `logging`, `googleapiclient`, `PIL`, `aiohttp`, `asyncio`, `python-dotenv`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-enhanced-image-filter.git
   cd ai-enhanced-image-filter
   ```

2. **Install Dependencies**:
   Create and activate a virtual environment (optional but recommended).
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables**:
   Create a `.env` file in the project root directory and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

## Usage

1. **Load Metadata**: Ensure `metadata.csv` containing `brand`, `category`, and `image_name` columns is in the project directory.
2. **Launch GUI**: Run the `app.py` file to open the GUI.
3. **Filter Images**: Select brand and category to filter images, then choose the destination folder to move the filtered images.

## Project Structure

```
ai-enhanced-image-filter/
├── images/                   # Directory containing images
├── metadata.csv              # Metadata file
├── app.py                    # Main application file
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not included in the repo)
└── README.md                 # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [Google Gemini API](https://cloud.google.com/gemini) for image analysis.
- The Python community for their awesome libraries and tools.

---

**Author**: [Your Name](https://github.com/yourusername)

Feel free to reach out with any questions or suggestions!
```

### Notes:
- Replace placeholders like `yourusername` and `your_api_key_here` with actual values.
- Include the `requirements.txt` file listing all dependencies.
- If applicable, add a `LICENSE` file in the project root.
