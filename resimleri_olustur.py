from PIL import Image

def create_rgb_image():
    width, height = 300, 100

    # RGB değerleri
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    # Her bir rengin genişliği
    segment_width = width // 3

    # Resimdeki piksel değerleri
    data = []
    for _ in range(height):
        data.extend([red] * segment_width)
        data.extend([green] * segment_width)
        data.extend([blue] * segment_width)

    # Resmi oluşturma
    img = Image.new('RGB', (width, height))
    img.putdata(data)
    img.save('Color-Table.bmp')
    img.show()

# Resim boyutları
width, height = 256, 256

# Her satır için siyah ve beyaz pikseller oluşturma
data = []
for y in range(height):
    # Yatay çizgide ilk yarısı siyah, ikinci yarısı beyaz olacak şekilde
    data.extend([0] * (width // 2) + [255] * (width // 2))

def create_gray_image():
    width, height = 1365, 768

    # Gri tonları değerleri
    shades_of_gray = [
        230,  # Açık gri
        200,  # Orta açık gri
        170,  # Orta gri
        140,  # Orta koyu gri
        110   # Koyu gri
    ]

    # Her bir gri tonunun genişliği
    segment_width = width // 5

    # Resimdeki piksel değerleri
    data = []
    for _ in range(height):
        for shade in shades_of_gray:
            data.extend([shade] * segment_width)

    # Resmi oluşturma
    img = Image.new('L', (width, height))
    img.putdata(data)
    img.save('Gray-Scale.bmp')
    img.show()

# Resmi oluşturma
img = Image.new('1', (width, height))
img.putdata(data)
img.save('Black&White.bmp')
img.show()
create_rgb_image()
create_gray_image()
