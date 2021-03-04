function cargarDepartamentos() {
    var array = ["Amazonas", "Antioquia", "Arauca", "Atlantico", "Bolivar",
                "Boyaca", "Caldas", "Caqueta", "Casanare", "Cauca",
                "Cesar", "Choco", "Cordoba", "Cundinamarca", "Guainia",
                "Guaviare", "Huila", "Guajira", "Magdalena", "Meta", "Nariño",
                "Norte_de_Santander", "Putumayo", "Quindio", "Risaralda", "San_Andres_y_Providencia",
                "Santander", "Sucre", "Tolima", "Valle", "Vaupes", "Vichada"];
    array.sort();
    addOptions("departamento", array);
}


//Función para agregar opciones a un <select>.
function addOptions(domElement, array) {
    var selector = document.getElementsByName(domElement)[0];
    for (departamento in array) {
        var opcion = document.createElement("option");
        opcion.text = array[departamento];
        // Añadimos un value a los option para hacer mas facil escoger los pueblos
        opcion.value = array[departamento].toLowerCase()
        selector.add(opcion);
    }
}



function cargarCiudades() {
    // Objeto de provincias con pueblos
    var listaCiudades = {
      Amazonas: ["El Encanto", "La Chorrera", "La Pedrera", "La Victoria", "Leticia","Puerto Alegria", "Puerto Nariño"],
      Antioquia: ["Medellin", "Bello", "Itagui", "Envigado", "Sabaneta"],
      Arauca: ["Arauca", "Arauquita", "Saravena", "Tame", "Fortul"],
      Atlantico: ["Barranquilla", "Malambo", "Soledad", "Sabanagrande", "Galapa"],
      Bolivar: ["Cartagena", "Turbaco", "Mompos", "Santa Rosa", "Magangué"],
      Boyaca: ["Tunja", "Arcabuco", "Aquitania", "Santana", "Villa de Leiva"],
      Caldas: ["Manizales", "Riosucio", "La Dorada", "Aguadas", "Chinchiná"],
      Caqueta: ["Florencia", "Solano", "Belen", "Morelia", "Albania"],
      Casanare: ["Yopal", "villanueva", "Tauramena", "Orocúe", "Aguazul"],
      Cauca: ["Popayan", "Caloto", "Corinto", "Toribio", "Cajibío"],
      Cesar: ["Valledupar", "Aguachica", "Chiriguana", "Chimichagua", "Manaure"],
      Choco: ["Quibdo", "Bagadó", "Bojayá", "Cértegui", "Condoto"],
      Cordoba: ["Monteria", "Cereté", "Lorica", "Montelibano", "Sahagún"],
      Cundinamarca: ["Bogotá", "Soacha", "Mosquera", "Facatativa", "Cajicá"],
      Guainia: ["Inirida", "Cacahual", "Mapiripana", "Guadalupe", "Puerto Colombia"],
      Guaviare: ["Miraflorez", "SJ del Guaviare", "Retorno", "Calamar"],
      Huila: ["Neiva", "Pitalito", "Rivera", "Algeciras", "Palermo"],
      Guajira: ["rioacha", "Maicao", "Uribia", "Fonseca", "Manaure"],
      Magdalena: ["Santa Marta", "Ciénaga", "Aracataca", "Ariguani", "Puebloviejo"],
      Meta: ["Villavicencio", "Acacías", "Mesetas", "Guamal", "Granada"],
      Nariño: ["Pasto", "Tumaco", "Ipiales", "Túquerres", "Samaniego"],
      Norte_de_Santander: ["Cúcuta", "Pamplona", "Ocaña", "Tibú", "Chinácota"],
      Putumayo: ["Mocoa", "Villagarzón", "Orito", "Sibundoy", "Pto Asis"],
      Quindio: ["Armenia", "Buenavista", "Córdoba", "Montenegro", "Calarcá"],
      Risaralda: ["Pereira", "Apia", "Balboa", "Guatica", "Dosquebradas"],
      San_Andres_y_Providencia: ["San Andres", "Providencia"],
      Santander: ["Bucaramanga", "Floridablanca", "Giron", "Simacota", "Velez"],
      Sucre: ["Sincelejo", "Corozal", "Tolú", "Morroa", "Sincé"],
      Tolima: ["Ibague", "Espinal", "Libano", "Melgar", "Honda"],
      Valle: ["Cali", "Buenaventura", "Jamundí", "Palmira", "Buga"],
      Vaupes: ["Mitú", "Papunathua", "Miraflorez", "Carurú", "Taraira"],
      Vichada: ["Pto Carreño", "Cumaribo", "Rosalía", "Maipures", "Gaviotas"]
    }
    
    var departamento = document.getElementById('departamento')
    var ciudad = document.getElementById('ciudad')
    var departamentoSeleccionado = departamento.value
    
    // Se limpian los pueblos
    ciudad.innerHTML = '<option value="">Seleccione una Ciudad...</option>'
    
    if(departamentoSeleccionado !== ''){
      // Se seleccionan los pueblos y se ordenan
      departamentoSeleccionado = listaCiudades[departamentoSeleccionado]
      departamentoSeleccionado.sort()
    
      // Insertamos los pueblos
      departamentoSeleccionado.forEach(function(ciudad){
        let opcion = document.createElement('option')
        opcion.value = ciudad
        opcion.text = ciudad
        ciudades.add(opcion)
      });
    }
    
  }
  