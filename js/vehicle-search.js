// API NHTSA para obtener marcas y modelos de vehículos
const NHTSA_API_BASE = 'https://vpic.nhtsa.dot.gov/api/vehicles';

const makesInput = document.getElementById('makesInput');
const makesDropdown = document.getElementById('makesDropdown');
const modelsInput = document.getElementById('modelsInput');
const modelsDropdown = document.getElementById('modelsDropdown');
const yearInput = document.getElementById('yearInput');

let vehicleData = {
  makes: [],
  models: {},
  filteredMakes: [],
  filteredModels: []
};

let selectedMake = '';
let selectedModel = '';

// ========== FUNCIONES PARA MARCAS ==========

// Cargar marcas de vehículos
async function loadMakes() {
  try {
    makesInput.placeholder = 'Cargando marcas...';
    makesInput.disabled = true;

    const response = await fetch(`${NHTSA_API_BASE}/GetAllMakes?format=json`);
    const data = await response.json();

    if (data.Results) {
      vehicleData.makes = data.Results.sort((a, b) =>
        a.Make_Name.localeCompare(b.Make_Name)
      );

      makesInput.placeholder = 'Busca marca...';
      makesInput.disabled = false;
    }
  } catch (error) {
    console.error('Error cargando marcas:', error);
    makesInput.placeholder = 'Error al cargar marcas';
  }
}

// Filtrar marcas según el input del usuario
function filterMakes(query) {
  const searchTerm = query.toLowerCase().trim();

  if (!searchTerm) {
    vehicleData.filteredMakes = [];
    makesDropdown.style.display = 'none';
    return;
  }

  vehicleData.filteredMakes = vehicleData.makes.filter(make =>
    make.Make_Name.toLowerCase().includes(searchTerm)
  );

  if (vehicleData.filteredMakes.length > 0) {
    displayMakesDropdown();
  } else {
    makesDropdown.style.display = 'none';
  }
}

// Mostrar dropdown de marcas filtradas
function displayMakesDropdown() {
  makesDropdown.innerHTML = '';

  vehicleData.filteredMakes.slice(0, 15).forEach((make, index) => {
    const li = document.createElement('li');
    li.className = 'autocomplete-item';
    li.textContent = make.Make_Name;
    li.dataset.value = make.Make_Name;
    li.dataset.index = index;

    li.addEventListener('click', () => selectMake(make.Make_Name));
    li.addEventListener('mouseenter', () => highlightMakeItem(index));

    makesDropdown.appendChild(li);
  });

  makesDropdown.style.display = 'block';
}

// Resaltar item en el dropdown de marcas
function highlightMakeItem(index) {
  const items = makesDropdown.querySelectorAll('.autocomplete-item');
  items.forEach(item => item.classList.remove('active'));
  if (items[index]) {
    items[index].classList.add('active');
  }
}

// Seleccionar una marca
function selectMake(makeName) {
  makesInput.value = makeName;
  selectedMake = makeName;
  makesDropdown.style.display = 'none';
  loadModels(makeName);
  makesInput.focus();
}

// Autocompletado: llenar automáticamente si hay una sola opción (marcas)
function autocompleteMake() {
  if (vehicleData.filteredMakes.length === 1) {
    selectMake(vehicleData.filteredMakes[0].Make_Name);
  }
}

// ========== FUNCIONES PARA MODELOS ==========

// Cargar modelos según la marca seleccionada
async function loadModels(makeName) {
  try {
    modelsInput.disabled = true;
    modelsInput.placeholder = 'Cargando modelos...';
    modelsInput.value = '';
    modelsDropdown.style.display = 'none';

    if (!makeName) {
      modelsInput.placeholder = 'Selecciona marca primero';
      return;
    }

    // Usar cache si ya tenemos los datos
    if (vehicleData.models[makeName]) {
      enableModelsInput(vehicleData.models[makeName]);
      return;
    }

    const response = await fetch(
      `${NHTSA_API_BASE}/GetModelsForMake/${makeName}?format=json`
    );
    const data = await response.json();

    if (data.Results) {
      const models = data.Results.sort((a, b) =>
        a.Model_Name.localeCompare(b.Model_Name)
      );

      // Guardar en cache
      vehicleData.models[makeName] = models;
      enableModelsInput(models);
    }
  } catch (error) {
    console.error('Error cargando modelos:', error);
    modelsInput.placeholder = 'Error al cargar modelos';
    modelsInput.disabled = true;
  }
}

// Habilitar el input de modelos
function enableModelsInput(models) {
  modelsInput.disabled = false;
  modelsInput.placeholder = 'Busca modelo...';
  modelsInput.value = '';
  modelsDropdown.innerHTML = '';
  modelsDropdown.style.display = 'none';
}

// Filtrar modelos según el input del usuario
function filterModels(query) {
  if (!selectedMake || !vehicleData.models[selectedMake]) {
    return;
  }

  const searchTerm = query.toLowerCase().trim();

  if (!searchTerm) {
    vehicleData.filteredModels = [];
    modelsDropdown.style.display = 'none';
    return;
  }

  vehicleData.filteredModels = vehicleData.models[selectedMake].filter(model =>
    model.Model_Name.toLowerCase().includes(searchTerm)
  );

  if (vehicleData.filteredModels.length > 0) {
    displayModelsDropdown();
  } else {
    modelsDropdown.style.display = 'none';
  }
}

// Mostrar dropdown de modelos filtrados
function displayModelsDropdown() {
  modelsDropdown.innerHTML = '';

  vehicleData.filteredModels.slice(0, 15).forEach((model, index) => {
    const li = document.createElement('li');
    li.className = 'autocomplete-item';
    li.textContent = model.Model_Name;
    li.dataset.value = model.Model_Name;
    li.dataset.index = index;

    li.addEventListener('click', () => selectModel(model.Model_Name));
    li.addEventListener('mouseenter', () => highlightModelItem(index));

    modelsDropdown.appendChild(li);
  });

  modelsDropdown.style.display = 'block';
}

// Resaltar item en el dropdown de modelos
function highlightModelItem(index) {
  const items = modelsDropdown.querySelectorAll('.autocomplete-item');
  items.forEach(item => item.classList.remove('active'));
  if (items[index]) {
    items[index].classList.add('active');
  }
}

// Seleccionar un modelo
function selectModel(modelName) {
  modelsInput.value = modelName;
  selectedModel = modelName;
  modelsDropdown.style.display = 'none';
  modelsInput.focus();
}

// Autocompletado: llenar automáticamente si hay una sola opción (modelos)
function autocompleteModel() {
  if (vehicleData.filteredModels.length === 1) {
    selectModel(vehicleData.filteredModels[0].Model_Name);
  }
}

// ========== FUNCIONES PARA AÑO ==========

// Validar entrada de año
function validateYear(value) {
  // Permitir solo números
  const numbersOnly = value.replace(/\D/g, '');

  // Limitar a 4 dígitos
  const limitedNumbers = numbersOnly.slice(0, 4);

  // Actualizar el input
  yearInput.value = limitedNumbers;

  // Validar que sea mayor a 1900
  if (limitedNumbers.length === 4) {
    const year = parseInt(limitedNumbers, 10);
    if (year < 1900) {
      yearInput.classList.add('error');
      yearInput.title = 'El año debe ser mayor a 1900';
    } else {
      yearInput.classList.remove('error');
      yearInput.title = '';
    }
  } else {
    yearInput.classList.remove('error');
  }
}

// ========== EVENT LISTENERS PARA MARCAS ==========

makesInput.addEventListener('input', (e) => {
  filterMakes(e.target.value);
});

makesInput.addEventListener('keydown', (e) => {
  const items = makesDropdown.querySelectorAll('.autocomplete-item');
  const activeItem = makesDropdown.querySelector('.autocomplete-item.active');
  let activeIndex = activeItem ? Array.from(items).indexOf(activeItem) : -1;

  switch (e.key) {
    case 'ArrowDown':
      e.preventDefault();
      activeIndex = Math.min(activeIndex + 1, items.length - 1);
      if (items[activeIndex]) {
        highlightMakeItem(activeIndex);
        items[activeIndex].scrollIntoView({ block: 'nearest' });
      }
      break;

    case 'ArrowUp':
      e.preventDefault();
      activeIndex = Math.max(activeIndex - 1, -1);
      if (activeIndex >= 0 && items[activeIndex]) {
        highlightMakeItem(activeIndex);
        items[activeIndex].scrollIntoView({ block: 'nearest' });
      } else {
        items.forEach(item => item.classList.remove('active'));
      }
      break;

    case 'Enter':
      e.preventDefault();
      if (activeItem) {
        selectMake(activeItem.dataset.value);
      } else if (vehicleData.filteredMakes.length === 1) {
        selectMake(vehicleData.filteredMakes[0].Make_Name);
      }
      break;

    case 'Tab':
      autocompleteMake();
      makesDropdown.style.display = 'none';
      break;

    case 'Escape':
      makesDropdown.style.display = 'none';
      break;
  }
});

// ========== EVENT LISTENERS PARA MODELOS ==========

modelsInput.addEventListener('input', (e) => {
  filterModels(e.target.value);
});

modelsInput.addEventListener('keydown', (e) => {
  const items = modelsDropdown.querySelectorAll('.autocomplete-item');
  const activeItem = modelsDropdown.querySelector('.autocomplete-item.active');
  let activeIndex = activeItem ? Array.from(items).indexOf(activeItem) : -1;

  switch (e.key) {
    case 'ArrowDown':
      e.preventDefault();
      activeIndex = Math.min(activeIndex + 1, items.length - 1);
      if (items[activeIndex]) {
        highlightModelItem(activeIndex);
        items[activeIndex].scrollIntoView({ block: 'nearest' });
      }
      break;

    case 'ArrowUp':
      e.preventDefault();
      activeIndex = Math.max(activeIndex - 1, -1);
      if (activeIndex >= 0 && items[activeIndex]) {
        highlightModelItem(activeIndex);
        items[activeIndex].scrollIntoView({ block: 'nearest' });
      } else {
        items.forEach(item => item.classList.remove('active'));
      }
      break;

    case 'Enter':
      e.preventDefault();
      if (activeItem) {
        selectModel(activeItem.dataset.value);
      } else if (vehicleData.filteredModels.length === 1) {
        selectModel(vehicleData.filteredModels[0].Model_Name);
      }
      break;

    case 'Tab':
      autocompleteModel();
      modelsDropdown.style.display = 'none';
      break;

    case 'Escape':
      modelsDropdown.style.display = 'none';
      break;
  }
});

// ========== EVENT LISTENERS PARA AÑO ==========

yearInput.addEventListener('input', (e) => {
  validateYear(e.target.value);
});

// ========== CERRAR DROPDOWNS AL HACER CLICK FUERA ==========

document.addEventListener('click', (e) => {
  // Cerrar dropdown de marcas
  if (!makesInput.contains(e.target) && !makesDropdown.contains(e.target)) {
    makesDropdown.style.display = 'none';
  }

  // Cerrar dropdown de modelos
  if (!modelsInput.contains(e.target) && !modelsDropdown.contains(e.target)) {
    modelsDropdown.style.display = 'none';
  }
});

// ========== INICIALIZAR ==========

document.addEventListener('DOMContentLoaded', loadMakes);
