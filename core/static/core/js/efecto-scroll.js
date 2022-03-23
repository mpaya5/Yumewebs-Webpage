document.addEventListener("DOMContentLoaded", function () {
    // Obtener todos los enlaces en una lista de nodos
    let lineas = document.querySelectorAll('#lineas a');

    let fps = new FullPageScroll('wrap', {
        mediaQuery: 'screen and (min-width: 100px)',
        goToTopOnLast: false
    });
    fps.onslide = function (e) {
        // Eliminar clase en todas las líneas
        lineas.forEach(linea => linea.classList.remove('activo'));
        // Agregar clase a elemento actual
        lineas[e.target.currentSlide].classList.add('activo');
    }
    // Agregar evento a los enlaces
    lineas.forEach((linea, x) => {
        linea.addEventListener('click', (e) => {
            // El enlace hace scroll y afecta a la función .goToSlide()
            e.preventDefault();
            // Seleccionar sección por índice de enlace que recibió clic
            fps.goToSlide(x);
        });
    });
    document.querySelectorAll('a.top').forEach(function (el) {
        el.addEventListener('click', function (event) {
            event.preventDefault();
            fps.goToFirstSlide();
        });
    });
});