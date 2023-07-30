from PIL import Image
from functools import cache
import os


path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "static", "img", "character"
)


@cache
def get_character_image_filename(
    body: str, head: str, face: str, hair: str, hat: str
) -> str:
    """
    Returns the filename to an image corresponding to the given inputs.
    If the image doesn't exist yet, this function first creates the image
    using Pillow. It also caches function calls using @lru_cache
    """

    args = [body, head, face, hair, hat]
    save_path = (
        f"{''.join([arg if not arg.isdigit() else f'body{arg}' for arg in args])}.png"
    )
    if os.path.exists(os.path.join(path, save_path)):
        return save_path

    def open_image(name: str) -> Image.Image:
        """Opens fragment of character image using Pillow"""
        return Image.open(
            os.path.join(
                path,
                name,
            )
        )

    # Create new image if it doesn't exist yet
    images = []
    for arg in args:
        if arg is not None and arg != "None":
            if arg.isdigit():
                body_image = open_image(f"body{arg}.png")
            else:
                images.append(open_image(f"{arg}.png"))
    for image in images:
        body_image.paste(image, (0, 0), image)
    body_image.save(os.path.join(path, save_path))
    return save_path
