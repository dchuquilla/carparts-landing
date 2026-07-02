#!/usr/bin/env python3
"""
Script para generar imágenes específicas de repuestos automotrices
Crea imágenes con iconos y diseños representativos
"""

from PIL import Image, ImageDraw, ImageFont
import math

CATEGORIES = [
    {
        "name": "Llantas",
        "filename": "category_llantas.jpg",
        "bg_color": "#1a1a1a",
        "accent_color": "#FFD700",
        "draw_func": "draw_tire"
    },
    {
        "name": "Baterías",
        "filename": "category_baterias.jpg",
        "bg_color": "#2C3E50",
        "accent_color": "#FF6B6B",
        "draw_func": "draw_battery"
    },
    {
        "name": "Filtros",
        "filename": "category_filtros.jpg",
        "bg_color": "#1E5631",
        "accent_color": "#90EE90",
        "draw_func": "draw_filter"
    },
    {
        "name": "Frenos",
        "filename": "category_frenos.jpg",
        "bg_color": "#8B0000",
        "accent_color": "#FF4444",
        "draw_func": "draw_brakes"
    },
    {
        "name": "Aceites",
        "filename": "category_aceites.jpg",
        "bg_color": "#3D2817",
        "accent_color": "#D4A574",
        "draw_func": "draw_oil"
    },
    {
        "name": "Amortiguadores",
        "filename": "category_amortiguadores.jpg",
        "bg_color": "#1A1A2E",
        "accent_color": "#00A8E8",
        "draw_func": "draw_shock"
    }
]

def hex_to_rgb(hex_color):
    """Convierte color hex a RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def draw_tire(draw, center_x, center_y, size, accent_rgb):
    """Dibuja un neumático"""
    # Círculo exterior (llanta)
    r = size
    draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r],
                 fill=accent_rgb, outline=accent_rgb, width=3)

    # Círculo interior (espacio vacío)
    r_inner = size * 0.6
    draw.ellipse([center_x - r_inner, center_y - r_inner, center_x + r_inner, center_y + r_inner],
                 fill=(61, 40, 23), width=0)

    # Líneas de diseño en la llanta
    num_lines = 8
    for i in range(num_lines):
        angle = (360 / num_lines) * i * math.pi / 180
        x1 = center_x + (size * 0.8) * math.cos(angle)
        y1 = center_y + (size * 0.8) * math.sin(angle)
        x2 = center_x + (size * 0.7) * math.cos(angle)
        y2 = center_y + (size * 0.7) * math.sin(angle)
        draw.line([(x1, y1), (x2, y2)], fill=(100, 100, 100), width=2)

def draw_battery(draw, center_x, center_y, size, accent_rgb):
    """Dibuja una batería"""
    w, h = size * 1.2, size * 2
    # Cuerpo de la batería
    draw.rectangle([center_x - w/2, center_y - h/2, center_x + w/2, center_y + h/2],
                   fill=accent_rgb, outline=(255, 255, 255), width=3)

    # Bornes (+ y -)
    bore_h = size * 0.3
    draw.rectangle([center_x - w/3, center_y - h/2 - bore_h,
                   center_x - w/6, center_y - h/2],
                   fill=accent_rgb, outline=(255, 255, 255), width=2)
    draw.rectangle([center_x + w/6, center_y - h/2 - bore_h,
                   center_x + w/3, center_y - h/2],
                   fill=accent_rgb, outline=(255, 255, 255), width=2)

def draw_filter(draw, center_x, center_y, size, accent_rgb):
    """Dibuja un filtro"""
    # Forma cilíndrica
    w, h = size * 0.8, size * 1.8

    # Cuerpo principal
    draw.rectangle([center_x - w/2, center_y - h/2, center_x + w/2, center_y + h/2],
                   fill=accent_rgb, outline=(255, 255, 255), width=3)

    # Tapa superior
    draw.polygon([
        (center_x - w/2, center_y - h/2),
        (center_x + w/2, center_y - h/2),
        (center_x + w/2 - 5, center_y - h/2 - 15),
        (center_x - w/2 + 5, center_y - h/2 - 15)
    ], fill=accent_rgb, outline=(255, 255, 255))

    # Líneas de textura
    for i in range(-int(h/4), int(h/4), 10):
        draw.line([(center_x - w/2 + 5, center_y + i),
                  (center_x + w/2 - 5, center_y + i)],
                 fill=(100, 100, 100), width=1)

def draw_brakes(draw, center_x, center_y, size, accent_rgb):
    """Dibuja un sistema de frenos (disco y pastillas)"""
    # Disco de freno circular
    draw.ellipse([center_x - size, center_y - size, center_x + size, center_y + size],
                 fill=accent_rgb, outline=(255, 255, 255), width=3)

    # Centro del disco
    draw.ellipse([center_x - size*0.3, center_y - size*0.3,
                 center_x + size*0.3, center_y + size*0.3],
                 fill=(100, 100, 100), width=0)

    # Líneas radiales (ranuras del disco)
    for i in range(8):
        angle = (360 / 8) * i * math.pi / 180
        x1 = center_x + size * 0.9 * math.cos(angle)
        y1 = center_y + size * 0.9 * math.sin(angle)
        x2 = center_x + size * 0.4 * math.cos(angle)
        y2 = center_y + size * 0.4 * math.sin(angle)
        draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255), width=2)

def draw_oil(draw, center_x, center_y, size, accent_rgb):
    """Dibuja una lata de aceite"""
    # Cuerpo de la lata
    w, h = size * 0.8, size * 2.2
    draw.rectangle([center_x - w/2, center_y - h/2 + 20, center_x + w/2, center_y + h/2],
                   fill=accent_rgb, outline=(255, 255, 255), width=3)

    # Tapa (círculo en la parte superior)
    draw.ellipse([center_x - w/2, center_y - h/2, center_x + w/2, center_y - h/2 + 40],
                 fill=(200, 150, 100), outline=(255, 255, 255), width=2)

    # Línea de textura
    draw.line([(center_x - w/2 + 10, center_y - 20), (center_x + w/2 - 10, center_y - 20)],
             fill=(100, 100, 100), width=2)

def draw_shock(draw, center_x, center_y, size, accent_rgb):
    """Dibuja un amortiguador"""
    # Tubo principal
    w, h = size * 0.5, size * 2.5
    draw.rectangle([center_x - w/2, center_y - h/2, center_x + w/2, center_y + h/2],
                   fill=accent_rgb, outline=(255, 255, 255), width=3)

    # Cilindro inferior (émbolo)
    cyl_w, cyl_h = w * 1.5, size * 0.6
    draw.rectangle([center_x - cyl_w/2, center_y + h/2 - 10,
                   center_x + cyl_w/2, center_y + h/2 + cyl_h - 10],
                   fill=accent_rgb, outline=(255, 255, 255), width=2)

    # Resorte (líneas onduladas)
    wave_points = 5
    for i in range(wave_points):
        y = center_y - h/2 + (h / wave_points) * i
        x_offset = 15 * (1 if i % 2 == 0 else -1)
        draw.line([(center_x - w/2 - x_offset, y), (center_x + w/2 + x_offset, y)],
                 fill=(150, 150, 150), width=1)

def create_category_image(category):
    """Crea una imagen para una categoría"""
    width, height = 400, 400
    img = Image.new('RGB', (width, height), hex_to_rgb(category["bg_color"]))
    draw = ImageDraw.Draw(img)

    # Gradiente de fondo
    accent_rgb = hex_to_rgb(category["accent_color"])
    for y in range(height):
        ratio = y / height
        r = int(hex_to_rgb(category["bg_color"])[0] * (1 - ratio * 0.3))
        g = int(hex_to_rgb(category["bg_color"])[1] * (1 - ratio * 0.3))
        b = int(hex_to_rgb(category["bg_color"])[2] * (1 - ratio * 0.3))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Dibujar el componente
    if category["draw_func"] == "draw_tire":
        draw_tire(draw, width//2, height//2 - 20, 80, accent_rgb)
    elif category["draw_func"] == "draw_battery":
        draw_battery(draw, width//2, height//2, 50, accent_rgb)
    elif category["draw_func"] == "draw_filter":
        draw_filter(draw, width//2, height//2, 60, accent_rgb)
    elif category["draw_func"] == "draw_brakes":
        draw_brakes(draw, width//2, height//2, 70, accent_rgb)
    elif category["draw_func"] == "draw_oil":
        draw_oil(draw, width//2, height//2, 50, accent_rgb)
    elif category["draw_func"] == "draw_shock":
        draw_shock(draw, width//2, height//2, 50, accent_rgb)

    # Guardar imagen
    img.save(category["filename"], 'JPEG', quality=95)
    print(f"✅ Generado: {category['filename']}")

def main():
    print("=" * 60)
    print("🎨 GENERANDO IMÁGENES DE REPUESTOS AUTOMOTRICES")
    print("=" * 60 + "\n")

    for category in CATEGORIES:
        print(f"📝 Creando imagen para: {category['name']}")
        create_category_image(category)

    print("\n" + "=" * 60)
    print("✨ ¡Todas las imágenes han sido generadas!")
    print("=" * 60)

if __name__ == "__main__":
    main()
