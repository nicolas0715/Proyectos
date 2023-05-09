const selectColumna = document.querySelector("#seleccion");
const inputValor = document.querySelector("#valor_input");

selectColumna.addEventListener("change", () => {
    switch (selectColumna.value) {
        case "nombre":
            inputValor.placeholder = "Introduzca el nombre";
            break;
        case "apellido":
            inputValor.placeholder = "Introduzca el apellido";
            break;
        case "fecha_nacimiento":
            inputValor.placeholder = "YYYY/MM/DD";
            break;
    }
});





