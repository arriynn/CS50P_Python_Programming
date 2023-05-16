import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    # Check that exactly two arguments were provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_file output_file")

    # Check that both filenames end in .jpg, .jpeg, or .png
    valid_extensions = {".jpg", ".jpeg", ".png"}
    input_ext = splitext(sys.argv[1])[1].lower()
    output_ext = splitext(sys.argv[2])[1].lower()
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Input and output filenames must end in .jpg, .jpeg, or .png")

    # Check that input and output have the same extension
    if input_ext != output_ext:
        sys.exit("Input and output filenames must have the same extension")

    # Check that input file exists
    try:
        Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input file does not exist")

    # Open input file and shirt image
    input_img = Image.open(sys.argv[1])
    shirt_img = Image.open("shirt.png")

    # Resize and crop input to match shirt image size
    input_size = shirt_img.size
    input_img = ImageOps.fit(input_img, input_size)

    # Overlay shirt on input
    input_img.paste(shirt_img, (0, 0), shirt_img)

    # Save result
    input_img.save(sys.argv[2])


if __name__ == "__main__":
    main()
