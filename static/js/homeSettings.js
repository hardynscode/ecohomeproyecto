$(document).ready(function () {
    // Cargar los tipos de casas y despegarlos en el selector de tipos
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/api/settings?tipo=tiposDeCasas",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        async: true,
        success: function (response) {

            const tipos = response;
            let content = "<option value=''>Seleccione el tipo de la casa..</option>";

            for (const key in tipos) {
                if (Object.hasOwnProperty.call(tipos, key)) {
                    const tipoCasa = tipos[key];
                    content += "<option value='" + key + "'>" + tipoCasa + "</option>";
                }
            }
            $("#tipoCasa").html(content);

            if (editando == true && dataCasa) {
                cargarTipoCasa();
            }
        },
        error: function (response) {
            console.log(response.responseJSON.message);
        }
    });

    // Cargar los paises en la DB y despegarlos en el selector de paises
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/api/settings?tipo=paises",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        async: true,
        success: function (response) {

            const paises = response;
            console.log("paises", paises);
            let content = "<option value=''>Seleccione..</option>";

            for (const key in paises) {
                if (Object.hasOwnProperty.call(paises, key)) {
                    const pais = paises[key];
                    content += "<option value='" + key + "'>" + pais.nombre + "</option>";
                }
            }
            $("#pais").html(content);

            if (editando == true && dataCasa) {
                cargarPais();
            }
        },
        error: function (response) {
            console.log(response.responseJSON.message);
        }
    });

    // codigo para cargar los departamentos dependiendo del pais seleccionado
    $("#pais").change(function () {
        const paisSeleccionado = $(this).val();

        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/api/settings?tipo=paises/" + paisSeleccionado + "/departamentos",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            async: true,
            success: function (response) {

                const departamentos = response;
                console.log("departamentos", departamentos);
                let content = "<option value=''>Seleccione..</option>";

                for (const key in departamentos) {
                    if (Object.hasOwnProperty.call(departamentos, key)) {
                        const depto = departamentos[key];
                        content += "<option value='" + key + "'>" + depto.nombre + "</option>";
                    }
                }
                $("#departamento").html(content);

                if (editando == true && dataCasa) {
                    cargarDepartamento();
                }
            },
            error: function (response) {
                console.log(response.responseJSON.message);
            }
        });
    });


    // codigo para cargar las ciudades dependiendo del departamento seleccionado
    $("#departamento").change(function () {
        const paisSeleccionado = $("#pais").val();
        const deptoSeleccionado = $(this).val();

        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/api/settings?tipo=paises/" + paisSeleccionado + "/departamentos/" + deptoSeleccionado + "/ciudades",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            async: true,
            success: function (response) {

                const ciudades = response;
                console.log("ciudades", ciudades);
                let content = "<option value=''>Seleccione..</option>";

                for (const key in ciudades) {
                    if (Object.hasOwnProperty.call(ciudades, key)) {
                        const ciudad = ciudades[key];
                        content += "<option value='" + key + "'>" + ciudad + "</option>";
                    }
                }
                $("#ciudad").html(content);

                if (editando == true && dataCasa) {
                    cargarCiudad();
                }
            },
            error: function (response) {
                console.log(response.responseJSON.message);
            }
        });


    });
});
