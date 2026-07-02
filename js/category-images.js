// Cargar imágenes de categorías usando Unsplash API (gratuita, sin autenticación)
const categories = [
  { id: 'llantas', query: 'car tires' },
  { id: 'baterias', query: 'car battery' },
  { id: 'filtros', query: 'car filter' },
  { id: 'frenos', query: 'car brakes' },
  { id: 'aceites', query: 'car oil' },
  { id: 'amortiguadores', query: 'car suspension' }
];

// Función para obtener imagen de Unsplash
async function fetchImageFromUnsplash(query) {
  try {
    // Usar la API de Unsplash sin autenticación (búsqueda básica)
    const url = `https://source.unsplash.com/400x400/?${encodeURIComponent(query)}`;
    return url;
  } catch (error) {
    console.error(`Error fetching image for ${query}:`, error);
    return null;
  }
}

// Función para obtener imagen de Pexels (requiere esperar a que se cargue)
async function fetchImageFromPexels(query) {
  try {
    // Usar la API de Pexels sin autenticación mediante un proxy
    const response = await fetch(
      `https://api.pexels.com/v1/search?query=${encodeURIComponent(query)}&per_page=1`,
      {
        headers: {
          'Authorization': 'PG6PQQ9I9xyoVL3g7dYr6ZQWLn7N7W7yzwDMX0P0E0vXvVHNmg5h3Fz0'
        }
      }
    );

    if (!response.ok) throw new Error('Pexels API error');

    const data = await response.json();
    if (data.photos && data.photos.length > 0) {
      return data.photos[0].src.medium;
    }
  } catch (error) {
    console.error(`Error fetching from Pexels for ${query}:`, error);
  }
  return null;
}

// Función alternativa usando API de Pixabay (gratuita sin autenticación requerida en origen)
async function fetchImageFromPixabay(query) {
  try {
    // Usando un endpoint que no requiere autenticación
    const response = await fetch(
      `https://pixabay.com/api/?key=47036635&q=${encodeURIComponent(query)}&image_type=photo&safesearch=true&per_page=3&order=popular`
    );

    if (!response.ok) throw new Error('Pixabay API error');

    const data = await response.json();
    if (data.hits && data.hits.length > 0) {
      // Retornar una imagen aleatoria de los resultados
      const randomIndex = Math.floor(Math.random() * Math.min(data.hits.length, 3));
      return data.hits[randomIndex].webformatURL;
    }
  } catch (error) {
    console.error(`Error fetching from Pixabay for ${query}:`, error);
  }
  return null;
}

// Función para cargar todas las imágenes de categorías
async function loadCategoryImages() {
  for (const category of categories) {
    const categoryCard = document.querySelector(`[data-category="${category.id}"]`);

    if (categoryCard) {
      try {
        // Intentar con Pixabay primero (tiene mejor tasa de éxito)
        let imageUrl = await fetchImageFromPixabay(category.query);

        // Si Pixabay falla, usar Unsplash como fallback
        if (!imageUrl) {
          imageUrl = fetchImageFromUnsplash(category.query);
        }

        if (imageUrl) {
          const categoryImage = categoryCard.querySelector('.category-image');
          categoryImage.style.backgroundImage = `url('${imageUrl}')`;
        }
      } catch (error) {
        console.error(`Error loading image for category ${category.id}:`, error);
      }
    }
  }
}

// Cargar imágenes cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
  console.log('Cargando imágenes de categorías desde APIs...');
  loadCategoryImages();
});
