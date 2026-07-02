# QuienTiene - Landing Page

Landing page para **QuienTiene.com**, una plataforma que conecta a usuarios con tiendas de repuestos verificadas en Ecuador. Permite buscar, comparar y comprar repuestos automotrices de forma rápida y sencilla.

## 🎯 Descripción del Proyecto

QuienTiene es una solución integral para encontrar repuestos automotrices:
- **Búsqueda inteligente**: Filtra por marca, modelo y año del vehículo
- **Múltiples opciones**: Recibe cotizaciones de diferentes tiendas verificadas
- **Comparación de precios**: Ahorra dinero comparando precios antes de comprar
- **Cobertura nacional**: Red de tiendas en todo Ecuador

## 📋 Requisitos

- **Node.js** v18 o superior
- **pnpm** v10 o superior (gestor de paquetes)

## 🚀 Instalación y Inicio

### 1. Instalar dependencias

```bash
pnpm install
```

### 2. Iniciar el servidor

**Modo producción:**
```bash
pnpm start
```

**Modo desarrollo (con auto-reload):**
```bash
pnpm dev
```

### 3. Acceder a la aplicación

Abre tu navegador y ve a: **http://localhost:5051**

## 📁 Estructura del Proyecto

```
carparts-landing/
├── index.html              # Página principal (home)
├── contacto.html           # Página de contacto
├── privacidad.html         # Política de privacidad
├── terminos.html           # Términos y condiciones
├── css/
│   └── style.css          # Estilos personalizados
├── server.js              # Servidor Express
├── package.json           # Dependencias del proyecto
├── pnpm-lock.yaml         # Lock file de pnpm
├── favicon.*              # Iconos de la aplicación
├── android-chrome-*       # Iconos para Android
├── apple-touch-icon.png   # Ícono para iOS
├── site.webmanifest       # Manifest de PWA
├── quien_tiene_logo_*.png # Logo de QuienTiene
└── README.md              # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3, Tailwind CSS
- **Backend**: Node.js, Express.js
- **Iconografía**: Font Awesome 6.0
- **Framework CSS**: Tailwind CSS (CDN)
- **Meta SEO**: Open Graph, Schema.org

## 📄 Páginas Disponibles

| Página | Ruta | Descripción |
|--------|------|-------------|
| Home | `/` | Página principal con búsqueda de repuestos |
| Contacto | `/contacto.html` | Formulario de contacto |
| Privacidad | `/privacidad.html` | Política de privacidad |
| Términos | `/terminos.html` | Términos y condiciones |

## ✨ Características Principales

### Hero Section
- Headline impactante
- Búsqueda avanzada por marca, modelo y año
- Búsqueda de repuestos específicos
- Call-to-action para usuarios nuevos

### Navegación
- Header responsivo con menú hamburguesa
- Links de navegación principal
- Acciones de sesión y publicación de solicitudes

### Optimizaciones
- Diseño responsive (mobile-first)
- SEO optimizado
- PWA ready (Web App Manifest)
- Iconografía moderna con Font Awesome

## 🔧 Scripts Disponibles

```bash
# Iniciar servidor en producción
pnpm start

# Iniciar servidor en desarrollo con auto-reload
pnpm dev

# Instalar dependencias
pnpm install
```

## 🌍 Acceso Remoto

Para acceder al servidor desde otra máquina en la red:

```bash
# Obtén tu IP local
ifconfig | grep "inet "

# Accede usando: http://TU_IP_LOCAL:5051
```

## 📱 Responsive Design

La landing page está optimizada para:
- 📱 Dispositivos móviles (360px y superior)
- 📱 Tablets (768px y superior)
- 💻 Escritorio (1024px y superior)

## 🎨 Personalización

### Cambiar puerto del servidor
Edita `server.js`:
```javascript
const PORT = 5051; // Cambia este número
```

### Modificar estilos
- Estilos globales: `css/style.css`
- Estilos Tailwind: se cargan desde CDN en `index.html`

## 🚨 Resolución de Problemas

### Puerto 5051 ya está en uso
```bash
# Encuentra el proceso usando el puerto
lsof -i :5051

# Mata el proceso (reemplaza PID)
kill -9 PID
```

### Dependencias no instalan
```bash
# Limpia el cache de pnpm
pnpm store prune

# Reinstala
pnpm install
```

### Archivos estáticos no se cargan
Asegúrate que el servidor esté ejecutándose y verifica la consola del navegador (F12) para errores de red.

## 📞 Contacto y Soporte

Para reportar problemas o sugerencias, contacta a través de:
- Página de contacto: `/contacto.html`
- Email: dario.chuquilla@gmail.com

## 📝 Licencia

Proyecto privado de QuienTiene.com

---

**Última actualización**: Julio 2026
