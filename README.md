# comfyui-negativewildcardsprocessor
Negative wildcards processor node for ComfyUI

Moves any text from the positive prompt to the negative prompt, that is surrounded by <! !>.
Useful for creating wildcards that include negative prompts like this:
{ rain, <!umbrella,!> | sunshine, <!sunglasses,!> }

Example usage and connections:
![image](https://github.com/user-attachments/assets/0a38353b-7bec-4a5e-ba36-0883af3b21a8)
