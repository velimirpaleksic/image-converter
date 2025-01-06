# Image Converter
Efficient Python tool for batch image conversion (.png, .jpg, .ico, .webp, .heic), with easy access via context menu.

## **Features**
- Convert a single image or batch of images to formats such as `PNG`, `JPEG`, `WEBP`, `HEIC`, and `ICO`.
- Automatically handles naming conflicts and ensures unique file names.
- Provides error handling with message boxes for common issues.
- GUI notifications for success or failure.

## **Requirements**
- Python 3.x
- `Pillow` library (for image processing)
- `Tkinter` library (for GUI notifications)

To install the required dependencies:

```bash
pip install pillow tk
```

## **Usage**
### **Command-Line Interface (CLI)**
You can run the script from the command line with the following syntax:

```bash
python main.py <input_path_or_dir> <output_format>
```

Where:
- `<input_path_or_dir>` is the path to either a single image or a directory containing images you want to convert.
- `<output_format>` is the desired image format (e.g., `png`, `jpeg`, `webp`, `heic`, `ico`).

#### **Example:**
To convert a single image to PNG:
```bash
python main.py "C:/images/sample.jpg" png
```

To convert all images in a folder to PNG:
```bash
python main.py "C:/images/" png
```

### **Build Executable**
To create an executable (`.exe`) version of the program without a console window, follow these steps:

1. **Install PyInstaller**:
   If you don't have `PyInstaller`, install it using pip:
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable**:
   In the directory where `main.py` is located, run the following command:

   ```bash
   pyinstaller --noconsole --onefile main.py
   ```

   This will generate a single `.exe` file inside the `dist` folder.

### **Setting up the Program for Use**
1. **Move the executable**:
   Move the compiled `.exe` file from the `dist` folder to `C:/ImageConverter/`.

2. **Add the icon**:
   Place an `icon.ico` file inside the `C:/ImageConverter/` folder. This will be used as the program's icon.

3. **Renaming**:
   Rename the compiled `main.exe` file to `ImageConverter.exe` for clarity and easy access.

4. **Running the Program**:
   Now, you can double-click the `add-context-menu.reg` file to add it to context menu for easy access.

## **Contact** ✉
- E-mail: [velimir.paleksic@gmail.com](velimir.paleksic@gmail.com).
- VexSystems GitHub: [github.com/vexsystems](https://github.com/vexsystems).
- VexSystems Instagram: [@vex.systems](https://www.instagram.com/vex.systems/).