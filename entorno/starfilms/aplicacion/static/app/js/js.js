// Función para agregar una película a la lista
function agregarPelicula(nombre, director, anio) {
    // Crear un elemento de lista
    const li = document.createElement('li');
    li.className = 'list-group-item';
    
    // Crear un botón para eliminar la película
    const botonEliminar = document.createElement('button');
    botonEliminar.className = 'btn btn-danger float-end';
    botonEliminar.innerText = 'Eliminar';
    botonEliminar.addEventListener('click', () => {
      li.remove();
    });
    
    // Crear un span con la información de la película
    const span = document.createElement('span');
    span.innerText = `${nombre} - ${director} (${anio})`;
    
    // Agregar el botón y el span a la lista
    li.appendChild(botonEliminar);
    li.appendChild(span);
    document.getElementById('lista-peliculas').appendChild(li);
  }
  
  // Función para listar las películas
  function listarPeliculas() {
    // Obtener el array de películas desde el localStorage
    const peliculas = JSON.parse(localStorage.getItem('peliculas')) || [];
    
    // Iterar sobre el array de películas y agregar cada una a la lista
    peliculas.forEach(pelicula => {
      agregarPelicula(pelicula.nombre, pelicula.director, pelicula.anio);
    });
  }
  
  // Obtener el formulario
  const formPeliculas = document.getElementById('form-peliculas');
  
  // Agregar un evento para cuando se envíe el formulario
  formPeliculas.addEventListener('submit', (event) => {
    // Prevenir que seenvíe el formulario
event.preventDefault();

// Obtener los valores del formulario
const nombre = document.getElementById('nombre').value;
const director = document.getElementById('director').value;
const anio = document.getElementById('anio').value;

// Agregar la película a la lista
agregarPelicula(nombre, director, anio);

// Guardar la película en el localStorage
const pelicula = {nombre, director, anio};
const peliculas = JSON.parse(localStorage.getItem('peliculas')) || [];
peliculas.push(pelicula);
localStorage.setItem('peliculas', JSON.stringify(peliculas));

// Limpiar los campos del formulario
formPeliculas.reset();
});

// Listar las películas cuando se carga la página
listarPeliculas();
formPeliculas.addEventListener('submit', (event) => {
    // Prevenir que se envíe el formulario
    event.preventDefault();
    
    // Obtener los valores del formulario
    const nombre = document.getElementById('nombre').value;
    const director = document.getElementById('director').value;
    const anio = document.getElementById('anio').value;
    
    // Agregar la película a la lista
    agregarPelicula(nombre, director, anio);
    
    // Guardar la película en el localStorage
    const pelicula = {nombre, director, anio};
    const peliculas = JSON.parse(localStorage.getItem('peliculas')) || [];
    peliculas.push(pelicula);
    localStorage.setItem('peliculas', JSON.stringify(peliculas));
    
    // Limpiar los campos del formulario
    formPeliculas.reset();
    
    // Listar las películas actualizadas
    listarPeliculas();
  });
  document.addEventListener('DOMContentLoaded', () => {
    // Obtener la lista de películas del localStorage y mostrarla en la página
    listarPeliculas();
  });
  