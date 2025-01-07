from PIL import Image, ImageFilter, ImageEnhance


def play_with_pikachu():
    img = Image.open('./assets/Pokedex/pikachu.png')
    print(img)
    print(img.format)
    print(dir(img))

    # ajusta a paleta de cores
    img = img.convert('RGB')
    filtered_image = img.filter(ImageFilter.BLUR)
    filtered_image.save('./assets/experimentos/blur.png', 'png')
    filtered_image = img.filter(ImageFilter.SHARPEN)
    filtered_image.save('./assets/experimentos/sharp.png', 'png')

    # PNG suporta mais filtros que jpg

    filtered_image = img.convert('L')
    filtered_image.save('./assets/experimentos/grey.png', 'png')

    rotated_image = img.rotate(90)
    rotated_image.save('./assets/experimentos/rotated.png', 'png')

    small_image = img.resize((300, 300))
    small_image.save('./assets/experimentos/small.png', 'png')

    box = (100, 100, 400, 400)
    cropped_image = img.crop(box)
    cropped_image.save('./assets/experimentos/crop.png', 'png')


def playing_with_big_images():
    big_img = Image.open('./assets/misc/armor.jpg')
    print(big_img.size)
    # como a proporção do resize não é a mesma, ela fica expremida
    new_image = big_img.resize((400, 400))
    new_image.save('./assets/experimentos/armor_thumbnail.png', 'png')
    # Podemos usar o metodo de thumbnail para manter a proporção
    big_img.thumbnail((400, 400))
    big_img.save('./assets/experimentos/armor_thumbnail_fixed.png', 'png')


# play_with_pikachu()
# playing_with_big_images()
