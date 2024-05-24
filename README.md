# Blender Copy Material Assignments Add-on

This Blender add-on allows you to copy material assignments from one object (the active object) to other selected objects. 
The material slots are not only copied, but also assigned to the to the corresponding geometry of the target object.
This is useful when you have multiple objects with the same geometry and want to ensure they all have the same material assignments, including .

## Installation

1. Download the `copy_material_assignments.py` file from this repository.
2. Open Blender.
3. Go to **Edit > Preferences**.
4. In the Preferences window, go to the **Add-ons** section.
5. Click the **Install** button at the top of the window.
6. Navigate to where you downloaded the `copy_material_assignments.py` file and select it.
7. After installation, enable the add-on by checking the box next to "Copy Material Assignments".

## Usage

1. Select the target objects (the ones you want to assign the materials to).
2. Shift-select the source object (the one with the correct material assignments) so that it is the active object.
3. Go to **Object > Copy Material Assignments** in the 3D Viewport menu.

The add-on will copy the material assignments from the active object to the selected objects.

## Features

- Copies material slots and their assignments from the active object to all selected objects.
- Ensures the target objects have the same material assignments as the source object.
- Designed to work with Blender 2.8 and newer versions.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

Created by Edouard J. Simon, with support from ChatGPT 4o.
