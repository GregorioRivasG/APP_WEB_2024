function operacion() {
    let n1, n2, tipo_op, oper, tipo, resultado;
    
    // Obtener valores del formulario
    n1 = parseFloat(document.getElementById("n1").value);
    n2 = parseFloat(document.getElementById("n2").value);
    tipo_op = document.getElementById("tipo").value; // Cambiado a "tipo" para coincidir con el HTML

    // Validar que ambos valores sean números
    if (isNumber(n1) && isNumber(n2)) {
        switch (tipo_op) {
            case "suma":
                oper = n1 + n2;
                tipo = "+";
                break;
            case "resta":
                oper = n1 - n2;
                tipo = "-";
                break;
            case "multiplicar":
                oper = n1 * n2;
                tipo = "*";
                break;
            case "dividir":
                if (n2 !== 0) {
                    oper = n1 / n2;
                    tipo = "/";
                } else {
                    oper = "Error: No se puede dividir por 0.";
                    tipo = "/";
                }
                break;
            default:
                oper = "Operación no válida";
        }
        
        // Mostrar resultado
        resultado = document.getElementById("resultado");
        resultado.innerHTML = `
        <hr>
        <h2>${n1} ${tipo} ${n2} = ${oper}</h2>`;
    } else {
        // Manejo de error si no son números válidos
        resultado = document.getElementById("resultado");
        resultado.innerHTML = `
        <hr>
        <h2>Por favor, ingresa números válidos.</h2>`;
    }
}

function isNumber(n) {
    // Validación de número
    return !isNaN(n) && isFinite(n);
}
