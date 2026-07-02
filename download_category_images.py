#!/usr/bin/env python3
"""
Script para descargar imágenes de repuestos automotrices desde Pexels API
Imágenes específicas de: Llantas, Baterías, Filtros, Frenos, Aceites, Amortiguadores
"""

import requests
import os
from pathlib import Path

# API de Pexels (gratuita)
PEXELS_API_KEY = "PG6PQQ9I9xyoVL3g7dYr6ZQWLn7N7W7yzwDMX0P0E0vXvVHNmg5h3Fz0"
PEXELS_API_URL = "https://api.pexels.com/v1/search"

# Categorías con términos de búsqueda específicos en inglés
CATEGORIES = [
    {
        "id": "llantas",
        "name": "Llantas",
        "query": "car tire wheel",
        "filename": "category_llantas.jpg"
    },
    {
        "id": "baterias",
        "name": "Baterías",
        "query": "car battery automotive",
        "filename": "category_baterias.jpg"
    },
    {
        "id": "filtros",
        "name": "Filtros",
        "query": "air filter engine filter car",
        "filename": "category_filtros.jpg"
    },
    {
        "id": "frenos",
        "name": "Frenos",
        "query": "car brake disc brake pad",
        "filename": "category_frenos.jpg"
    },
    {
        "id": "aceites",
        "name": "Aceites",
        "query": "motor oil engine oil car",
        "filename": "category_aceites.jpg"
    },
    {
        "id": "amortiguadores",
        "name": "Amortiguadores",
        "query": "shock absorber suspension car",
        "filename": "category_amortiguadores.jpg"
    }
]

def download_image_from_pexels(query, filename, category_name):
    """Descarga una imagen de Pexels usando la API"""
    try:
        print(f"📥 Buscando imagen de: {category_name}")
        print(f"   Búsqueda: '{query}'")

        headers = {
            "Authorization": PEXELS_API_KEY
        }

        params = {
            "query": query,
            "per_page": 1,
            "orientation": "square",
            "size": "medium"
        }

        response = requests.get(PEXELS_API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data.get("photos") or len(data["photos"]) == 0:
            print(f"⚠️  No se encontraron imágenes para: {category_name}\n")
            return False

        # Obtener la primera imagen
        photo = data["photos"][0]
        image_url = photo["src"]["medium"]
        photographer = photo["photographer"]

        print(f"   ✓ Foto por: {photographer}")
        print(f"   Descargando imagen...")

        image_response = requests.get(image_url, timeout=15)
        image_response.raise_for_status()

        # Guardar la imagen en la raíz del proyecto
        with open(filename, "wb") as f:
            f.write(image_response.content)

        file_size = len(image_response.content) / 1024  # En KB
        print(f"✅ Descargada: {filename} ({file_size:.1f} KB)\n")
        return True

    except requests.exceptions.Timeout:
        print(f"❌ Timeout al descargar {category_name}\n")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error descargando {category_name}: {str(e)}\n")
        return False
    except Exception as e:
        print(f"❌ Error inesperado en {category_name}: {str(e)}\n")
        return False

def download_all_images():
    """Descarga todas las imágenes de categorías"""
    print("=" * 70)
    print("🚀 DESCARGANDO IMÁGENES DE REPUESTOS AUTOMOTRICES")
    print("   Fuente: Pexels API (imágenes de alta calidad)")
    print("=" * 70 + "\n")

    successful = 0
    failed = 0

    for category in CATEGORIES:
        success = download_image_from_pexels(
            category["query"],
            category["filename"],
            category["name"]
        )

        if success:
            successful += 1
        else:
            failed += 1

    print("=" * 70)
    print(f"📊 RESUMEN: {successful} exitosas, {failed} fallidas")
    print("=" * 70)

    return successful > 0

if __name__ == "__main__":
    try:
        if download_all_images():
            print("\n✨ ¡Descarga completada!")
            print("\n📁 Imágenes descargadas en la raíz del proyecto:")
            for cat in CATEGORIES:
                if os.path.exists(cat["filename"]):
                    size = os.path.getsize(cat["filename"]) / 1024
                    print(f"   ✓ {cat['name']}: {cat['filename']} ({size:.1f} KB)")
                else:
                    print(f"   ✗ {cat['name']}: {cat['filename']} (no encontrado)")

            print("\n✅ El HTML está configurado para usar estas imágenes locales.")
            print("🚀 Ejecuta: pnpm start")
        else:
            print("\n⚠️  No se pudieron descargar las imágenes.")
            print("💡 Verifica:")
            print("   • Tu conexión a internet")
            print("   • Que la API key de Pexels sea válida")
    except KeyboardInterrupt:
        print("\n\n❌ Descarga cancelada por el usuario.")
    except Exception as e:
        print(f"\n❌ Error general: {str(e)}")
