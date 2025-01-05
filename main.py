import pandas as pd
import os
import shutil
import logging
from tkinter import Tk, Label, Button, StringVar, filedialog, messagebox
from tkinter.ttk import Progressbar, OptionMenu as TtkOptionMenu, Label as TtkLabel, Button as TtkButton, Style
from googleapiclient.discovery import build
from PIL import Image
from dotenv import load_dotenv
import asyncio
import aiohttp

# Load environment variables
load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Google Gemini API
def get_gemini_service():
    return build('gemini', 'v1', developerKey=API_KEY)

# Function to analyze image using Gemini API
async def analyze_image_async(image_path):
    service = get_gemini_service()
    with open(image_path, 'rb') as image_file:
        image_content = image_file.read()

    try:
        request = service.images().analyze(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('ISO-8859-1')
                },
                'features': [{'type': 'LABEL_DETECTION'}]
            }]
        })
        response = request.execute()
        labels = response['responses'][0]['labelAnnotations']
        tags = [label['description'] for label in labels]
        return tags
    except Exception as e:
        logging.error(f"Error analyzing image {image_path}: {e}")
        return []

# Load metadata
metadata = pd.read_csv('metadata.csv')

# Get unique brands and categories
brands = ['All'] + list(metadata['brand'].unique())
categories = ['All'] + list(metadata['category'].unique())

# Initialize Tkinter window
root = Tk()
root.title("AI-Enhanced Image Filter App")
root.geometry("500x300")
root.resizable(False, False)

# Variables to store selected brand and category
selected_brand = StringVar(value=brands[0])
selected_category = StringVar(value=categories[0])

async def filter_and_move_images_async():
    brand = selected_brand.get()
    category = selected_category.get()
    
    filtered = metadata
    if brand != "All":
        filtered = filtered[filtered['brand'] == brand]
    if category != "All":
        filtered = filtered[filtered['category'] == category]

    if filtered.empty:
        messagebox.showinfo("No Images", "No images match the selected criteria.")
        return
    
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        messagebox.showwarning("No Directory", "No output directory selected.")
        return

    total_images = len(filtered)
    progress_bar['maximum'] = total_images
    copied_images = 0

    for _, row in filtered.iterrows():
        image_name = row['image_name']
        source_path = os.path.join('images', image_name)
        destination_path = os.path.join(output_dir, image_name)
        shutil.copy(source_path, destination_path)
        copied_images += 1
        progress_bar['value'] = copied_images
        root.update_idletasks()

    messagebox.showinfo("Success", f"Filtered images moved to {output_dir}")
    progress_bar['value'] = 0

def run_filtering():
    asyncio.run(filter_and_move_images_async())

# GUI components
TtkLabel(root, text="Filter Images by Brand and Category").grid(row=0, column=0, columnspan=2, pady=10)

TtkLabel(root, text="Select Brand:").grid(row=1, column=0, sticky='e')
TtkOptionMenu(root, selected_brand, *brands).grid(row=1, column=1, sticky='w')

TtkLabel(root, text="Select Category:").grid(row=2, column=0, sticky='e')
TtkOptionMenu(root, selected_category, *categories).grid(row=2, column=1, sticky='w')

TtkButton(root, text="Filter Images", command=run_filtering).grid(row=3, column=0, columnspan=2, pady=20)

progress_bar = Progressbar(root, length=300, mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
