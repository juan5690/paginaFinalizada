// Obtener los elementos del formulario
const form = document.querySelector("form");
const firstNameInput = document.getElementById("fname");
const emailInput = document.getElementById("email");
const cardNameInput = document.getElementById("cname");
const cardNumberInput = document.getElementById("ccnum");
const expMonthInput = document.getElementById("expmonth");
const expYearInput = document.getElementById("año");
const cvvInput = document.getElementById("cvv");

// Agregar un evento de escucha al enviar el formulario
form.addEventListener("submit", function (event) {
  // Validar nombre
  if (firstNameInput.value.trim() === "") {
    alert("Por favor, ingresa un nombre válido");
    event.preventDefault(); // Evitar el envío del formulario
    return;
  }

  // Validar correo electrónico
  if (!isValidEmail(emailInput.value)) {
    alert("Por favor, ingresa un correo electrónico válido");
    event.preventDefault();
    return;
  }

  // Validar nombre del dueño de la tarjeta
  if (cardNameInput.value.trim() === "") {
    alert("Por favor, ingresa un nombre válido para el dueño de la tarjeta");
    event.preventDefault();
    return;
  }

  // Validar número de tarjeta
  if (!isValidCardNumber(cardNumberInput.value)) {
    alert("Por favor, ingresa un número de tarjeta válido");
    event.preventDefault();
    return;
  }

  // Validar mes de expiración
  if (!isValidMonth(expMonthInput.value)) {
    alert("Por favor, ingresa un mes de expiración válido");
    event.preventDefault();
    return;
  }

  // Validar año de expiración
  if (!isValidYear(expYearInput.value)) {
    alert("Por favor, ingresa un año de expiración válido");
    event.preventDefault();
    return;
  }

  // Validar CVV
  if (!isValidCVV(cvvInput.value)) {
    alert("Por favor, ingresa un CVV válido");
    event.preventDefault();
    return;
  }

  // Si todos los campos son válidos, el formulario se envía correctamente
});

// Función para validar el formato del correo electrónico
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Función para validar el número de tarjeta (solo dígitos y guiones)
function isValidCardNumber(cardNumber) {
  const cardNumberRegex = /^\d{4}-\d{4}-\d{4}-\d{4}$/;
  return cardNumberRegex.test(cardNumber);
}

// Función para validar el mes de expiración (1-12)
function isValidMonth(month) {
  const monthNumber = parseInt(month, 10);
  return monthNumber >= 1 && monthNumber <= 12;
}

// Función para validar el año de expiración (año actual o futuro)
function isValidYear(year) {
  const currentYear = new Date().getFullYear();
  const yearNumber = parseInt(year, 10);
  return yearNumber >= currentYear;
}

// Función para validar el CVV (código de seguridad de 3 dígitos)
function isValidCVV(cvv) {
  const cvvRegex = /^\d{3}$/;
  return cvvRegex.test(cvv);
}
