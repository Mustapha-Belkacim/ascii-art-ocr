from ascii_art import text_to_ascii_art, ascii_art_to_text


if __name__ == '__main__':
	text = input('Please enter a text : ')
	ascii_art = text_to_ascii_art(text, font_weight=20)
	print(ascii_art)
	print('Detected text : ', ascii_art_to_text(ascii_art))
