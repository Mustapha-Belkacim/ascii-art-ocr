from PIL import Image, ImageFont, ImageDraw


def string_to_bitmap(text, font_style='arialbd.ttf', font_weight=9):
	font = ImageFont.truetype(font_style, font_weight)  # load the font
	size = font.getsize(text)  # claculate the size of text in pixels
	image = Image.new('1', size, 'white')  # create a white image
	draw = ImageDraw.Draw(image)
	draw.text((0, 0), text, font=font)  # render the text to bitmap
	return image
