#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio de imágenes si no existe
os.makedirs('images', exist_ok=True)

categories = [
    {
        'name': 'Llantas',
        'filename': 'category_llantas.jpg',
        'color': '#2C3E50',
        'accent': '#FF6B6B',
        'emoji': '🛞'
    },
    {
        'name': 'Baterías',
        'filename': 'category_baterias.jpg',
        'color': '#34495E',
        'accent': '#F39C12',
        'emoji': '🔋'
    },
    {
        'name': 'Filtros',
        'filename': 'category_filtros.jpg',
        'color': '#1E5631',
        'accent': '#2ECC71',
        'emoji': '🔧'
    },
    {
        'name': 'Frenos',
        'filename': 'category_frenos.jpg',
        'color': '#8B0000',
        'accent': '#FF4444',
        'emoji': '🛑'
    },
    {
        'name': 'Aceites',
        'filename': 'category_aceites.jpg',
        'color': '#3D2817',
        'accent': '#D4A574',
        'emoji': '🛢️'
    },
    {
        'name': 'Amortiguadores',
        'filename': 'category_amortiguadores.jpg',
        'color': '#1A1A2E',
        'accent': '#00A8E8',
        'emoji': '⚙️'
    }
]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generate_category_image(category):
    width, height = 300, 300

    # Crear imagen con gradiente de fondo
    img = Image.new('RGB', (width, height), hex_to_rgb(category['color']))
    draw = ImageDraw.Draw(img, 'RGBA')

    # Crear gradiente simple (de arriba a abajo)
    for y in range(height):
        ratio = y / height
        r1, g1, b1 = hex_to_rgb(category['color'])
        r2, g2, b2 = hex_to_rgb(category['accent'])

        r = int(r1 + (r2 - r1) * ratio * 0.3)
        g = int(g1 + (g2 - g1) * ratio * 0.3)
        b = int(b1 + (b2 - b1) * ratio * 0.3)

        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Agregar círculos decorativos
    circle_color = hex_to_rgb(category['accent'])

    # Círculo grande
    draw.ellipse([
        (width * 0.5 - 80, height * 0.5 - 80),
        (width * 0.5 + 80, height * 0.5 + 80)
    ], fill=circle_color + (30,), outline=circle_color + (80,), width=2)

    # Círculos pequeños
    draw.ellipse([
        (width * 0.2 - 20, height * 0.2 - 20),
        (width * 0.2 + 20, height * 0.2 + 20)
    ], fill=circle_color + (20,), outline=circle_color + (60,), width=1)

    draw.ellipse([
        (width * 0.8 - 30, height * 0.8 - 30),
        (width * 0.8 + 30, height * 0.8 + 30)
    ], fill=circle_color + (25,), outline=circle_color + (70,), width=1)

    # Agregar texto (categoría)
    try:
        # Intentar usar una fuente del sistema
        font_size = 48
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        except:
            font = ImageFont.load_default()

    # Dibujar nombre de categoría
    text = category['name']
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 20

    # Sombra de texto
    draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0, 100))
    # Texto principal
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    # Guardar imagen
    img.save(f'images/{category["filename"]}', 'JPEG', quality=95)
    print(f'✅ Generado: images/{category["filename"]}')

# Generar todas las imágenes
for category in categories:
    generate_category_image(category)

print('\n✨ ¡Todas las imágenes han sido generadas exitosamente!')
