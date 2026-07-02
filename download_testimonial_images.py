#!/usr/bin/env python3
"""
Script para descargar fotografías reales de personas latinoamericanas
Utiliza URLs directas de Unsplash sin autenticación
"""

import requests
import os
import random

# URLs directas de imágenes de Unsplash de personas latinoamericanas
# Estas URLs se obtienen de búsquedas públicas de Unsplash
TESTIMONIALS = [
    {
        "id": "carlos",
        "name": "Carlos M.",
        "filename": "testimonial_carlos.jpg",
        "gender": "male",
        "urls": [
            # URLs de hombres latinoamericanos de Unsplash
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1507009997318-601c67f75869?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1489424731266-a570ea7015a7?w=400&h=400&fit=crop",
        ]
    },
    {
        "id": "andrea",
        "name": "Andrea P.",
        "filename": "testimonial_andrea.jpg",
        "gender": "female",
        "urls": [
            # URLs de mujeres latinoamericanas de Unsplash
            "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop",
        ]
    },
    {
        "id": "luis",
        "name": "Luis F.",
        "filename": "testimonial_luis.jpg",
        "gender": "male",
        "urls": [
            # URLs de hombres de Unsplash
            "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=400&fit=crop",
            "https://images.unsplash.com/photo-1489549132488-d0921edfb77f?w=400&h=400&fit=crop",
        ]
    }
]

def download_testimonial_image(testimonial):
    """Descarga una imagen de testimonial desde URLs de Unsplash"""
    print(f"📥 Descargando foto para: {testimonial['name']}")

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; QuienTiene/1.0)"
    }

    # Intentar con cada URL disponible
    for i, url in enumerate(testimonial['urls'], 1):
        try:
            print(f"   Intentando URL {i}/{len(testimonial['urls'])}...")

            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()

            # Verificar que es una imagen válida
            if len(response.content) > 5000:  # Al menos 5KB
                with open(testimonial['filename'], "wb") as f:
                    f.write(response.content)

                file_size = len(response.content) / 1024
                print(f"✅ Descargada: {testimonial['filename']} ({file_size:.1f} KB)\n")
                return True
        except Exception as e:
            print(f"   Error: {str(e)[:50]}")
            continue

    print(f"❌ No se pudo descargar imagen para {testimonial['name']}\n")
    return False

def download_all_testimonials():
    """Descarga todas las imágenes de testimoniales"""
    print("=" * 70)
    print("🚀 DESCARGANDO FOTOS DE PERSONAS LATINOAMERICANAS")
    print("   Fuente: Unsplash (imágenes públicas sin autenticación)")
    print("=" * 70 + "\n")

    successful = 0
    failed = 0

    for testimonial in TESTIMONIALS:
        success = download_testimonial_image(testimonial)
        if success:
            successful += 1
        else:
            failed += 1

    print("=" * 70)
    print(f"📊 RESUMEN: {successful} exitosas, {failed} fallidas")
    print("=" * 70)

    return successful > 0

def update_html():
    """Actualiza el HTML para usar las imágenes descargadas"""
    print("\n📝 Actualizando HTML...")

    html_file = "index.html"

    try:
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Reemplazar URLs de randomuser.me con las nuevas imágenes
        replacements = [
            ('https://randomuser.me/api/portraits/men/32.jpg', 'testimonial_carlos.jpg'),
            ('https://randomuser.me/api/portraits/women/44.jpg', 'testimonial_andrea.jpg'),
            ('https://randomuser.me/api/portraits/men/65.jpg', 'testimonial_luis.jpg'),
        ]

        for old_url, new_file in replacements:
            content = content.replace(old_url, new_file)

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(content)

        print("✅ HTML actualizado exitosamente\n")
        return True

    except Exception as e:
        print(f"❌ Error actualizando HTML: {str(e)}\n")
        return False

def main():
    print("\n")
    if download_all_testimonials():
        print("\n✨ ¡Descarga completada!")
        print("\n📁 Imágenes descargadas:")
        for testimonial in TESTIMONIALS:
            if os.path.exists(testimonial["filename"]):
                size = os.path.getsize(testimonial["filename"]) / 1024
                print(f"   ✓ {testimonial['name']}: {testimonial['filename']} ({size:.1f} KB)")
            else:
                print(f"   ✗ {testimonial['name']}: No descargada")

        if update_html():
            print("\n✅ El HTML ha sido actualizado con las nuevas imágenes.")
            print("🚀 Ahora ejecuta: pnpm start")
        else:
            print("\n⚠️  Problema actualizando el HTML.")
    else:
        print("\n⚠️  No se pudieron descargar todas las imágenes.")
        print("💡 Verifica tu conexión a internet.")

if __name__ == "__main__":
    main()
