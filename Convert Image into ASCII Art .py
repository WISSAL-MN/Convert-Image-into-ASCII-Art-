import ascii_magic


img = ascii_magic.from_image_file('image/wissal.jpg',columns=200,char="#")
ascii_magic.to_terminal(img)
