# Overlay App README

## Overview
This overlay app enables users to create customizable overlays on their desktop screens, which can display images or GIFs. These overlays can be dynamically positioned, resized, and toggled with user-defined hotkeys, enhancing productivity and personalization of the workspace.

## Project Structure
The project is structured into several key components:

- **main.py**: The main application script that initializes the GUI and handles user interactions.
- **newoverlayui.py**: Defines the user interface of the main application window using PySide6.
- **overlay_window.py**: Manages the overlay windows, including setting properties like "always on top" and handling image or GIF content.
- **dynamic_alignment_window.py**: Provides functionality for dynamically positioning the overlays on the screen.
- **overlay_card.py**: Represents a UI component for managing individual overlay settings within the application.
- **screen_utils.py**, **overlay_utils.py**, **icon_scaler.py**, **error_feedback_utils.py**: Utility scripts for screen calculations, overlay window modifications, icon scaling, and error feedback, respectively.
- **styles.qss**: Stylesheet for customizing the application's appearance.

## Getting Started

### Prerequisites
- Python 3.8 or higher installed on your machine.
- PySide6 for the GUI components.
- keyboard for global hotkey registration.

Install the required Python packages by running:

```pip install PySide6 keyboard Pillow```

### Configuration
No additional configuration is required outside of the Python environment setup.

### Building and Running the Project
1. Clone the project to your local machine.
2. Navigate to the project directory.
3. Run the application by executing:

```python main.py```


## Features
- **Overlay Creation**: Users can create overlays with custom images or GIFs.
- **Hotkey Activation**: Define global hotkeys to toggle the visibility of overlays.
- **Dynamic Positioning**: Use the dynamic alignment feature to position overlays precisely.
- **Resize Overlays**: Adjust the size of your overlays to fit your needs.
- **Customizable UI**: The application UI can be customized via the `styles.qss` stylesheet

# ScreenShots
![image](https://github.com/NoshGiven/Overly/assets/127076152/8b045f76-19e9-414e-b80c-51aaf937f764)
![image](https://github.com/NoshGiven/Overly/assets/127076152/fbab335b-7785-4afd-a8c2-32ba4ccf405b)


