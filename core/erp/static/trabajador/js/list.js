
$(function () {
    var miTabla = new DataTable('#data',{
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json',
        },
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        dom:'Qlfrtip',
        conditions:{
            num:{
                'MultipleOf':{
                    conditionName:'MultipleOf',
                    init : function(that,fn,preDefined=null){
                        var el = $`<input/>`.on('input',function(){fn(that,this)});
                        if(preDefined!==null){
                            $(el).val(preDefined[0]);
                        }
                        return el
                    },
                    inputValue:function(el){
                        return $(el[0].val());
                    },
                    isInputValid:function(el,that){
                        return $(el[0].val().length!==0);
                    },
                    search:function(value,comparison){
                        return value%comparison===0;
                    }
                }
            }
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "tipo"},
            {"data": "documento"},
            {"data": "nombre"},
            {"data": "apellidos"},
            {"data": "id"},
            {"data": "id"},
            {"data": "id"},
            {"data": "id"},
        ],
        columnDefs:[
           
            {
                targets:[-4],
                class:'text-center',
                render:function(date,type,row){
                   
                    
                    return '<button id="btnepps" class="btn btn-primary" >VER DATOS</button>'
                }
            },
            {
                targets:[-3],
                class:'text-center',
                render:function(date,type,row){
                   
                    
                    return '<button id="btnvh" class="btn btn-secondary" >VER DATOS</button>'
                }
            },
            {
                targets:[-2],
                class:'text-center',
                render:function(date,type,row){
                   
                    
                    return '<button id="btnepv" class="btn btn-success" >VER DATOS</button>'
                }
            },
            {
                targets:[-1],
                class:'text-center',
                render:function(date,type,row){
                    var buttons = '<div class="d-flex justify-content-center"><a href="/erp/trab/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/trab/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a></row>';
                    return buttons;
                }
            }
        ],

        initComplete: function (settings, json) {
            // Habilitar los botones de exportación
            new $.fn.dataTable.Buttons(miTabla, {
                buttons: [
                    {
                        text:'<i class="fas fa-plus"></i>Nuevo registro',
                        action:function(e,dt,node,conf){
                            window.location.href = '/erp/trab/create/'
                        }
                    },
                    'copy', 'excel', 'csv', 'pdf', 'print'
                ],
                // Personalizar la apariencia de los botones (opcional)
                dom: {
                    button: {
                        className: 'btn btn-primary'
                    }
                }
            });

            // Crear un contenedor para los botones de exportación
            var $exportButtonsContainer = $('<div class="export-buttons-container"></div>');
            miTabla.buttons().container().appendTo($exportButtonsContainer);

            // Agregar el contenedor de botones antes del input de búsqueda
            $exportButtonsContainer.insertBefore($('#data_wrapper .dataTables_filter'));
        }
    });
    const contenidoModal = ()=>{
    return (`
            <div class="modal fade" id="miModal" tabindex="-1" role="dialog" aria-labelledby="miModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="miModalLabel">VEHICULO</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                        
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-success" id="btnsumbit">GUARDAR</button>
                            <button type="button" class="btn btn-danger" data-dismiss="modal">CERRAR</button>
                        </div>
                    </div>
                </div>
            </div>

                `)};
    function showepps(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex, 0).data();
        $.ajax({
            type: "POST",
            url: "/erp/epps/list/",
            dataType: "json",
            data:{
                "id":id,
                "action":"epps"
            },
            success: function(data) {
                
                $('.modal-body').html(
                    ` <form method="POST" action="." enctype="multipart/form-data" id="myForm1">
                        <input type="hidden" value="${data.action}" readonly="true" id="action" name="action" />
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">ID: </label><input class="form-control ml-3" value="${data.id}" readonly="true" id="id" name="id"/>
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">CASCO: </label><input type="checkbox" class="form-control ml-3" ${data.casco ? 'checked' : ''} id="casco" name="casco" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">BARBIQUEJO: </label><input type="checkbox" class="form-control ml-3" ${data.barbiquejo ? 'checked' : ''} id="barbiquejo" name="barbiquejo" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">BOTAS: </label><input type="checkbox" class="form-control ml-3" ${data.botas ? 'checked' : ''} id="botas" name="botas" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">TAPONES: </label><input type="checkbox" class="form-control ml-3"  ${data.tapones ? 'checked' : ''} id="tapones" name="tapones" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">LENTES: </label><input type="checkbox" class="form-control ml-3"  ${data.lentes ? 'checked' : ''} id="lentes" name="lentes" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">CHALECO: </label><input type="checkbox" class="form-control ml-3" ${data.chaleco ? 'checked' : ''} id="chaleco" name="chaleco" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">RESPIRADOR: </label><input type="checkbox" class="form-control ml-3"  ${data.respirador ? 'checked' : ''} id="respirador" name="respirador" />
                        </div>
                    <form>
                    `
                );
                
               $("#btnsumbit").on("click", function() {
                var datos = {
                    "id": $("#id").val(),
                    "action": $("#action").val(),
                    "casco": $("#casco").prop("checked") ? 1 : 0,
                    "barbiquejo": $("#barbiquejo").prop("checked") ? 1 : 0,
                    "botas": $("#botas").prop("checked") ? 1 : 0,
                    "tapones": $("#tapones").prop("checked") ? 1 : 0,
                    "lentes": $("#lentes").prop("checked") ? 1 : 0,
                    "chaleco": $("#chaleco").prop("checked") ? 1 : 0,
                    "respirador": $("#respirador").prop("checked") ? 1 : 0,
                };
                $.ajax({
                    type : "POST",
                    url : ".",
                    dataType : "json",
                    data:datos,
                    success:function(data){
                        window.location.href = "."
                    },
                    error:function(jqXHR,textStatus,errorThrown){
                        console.log("Error en la peticion:",textStatus,errorThrown)
                    }
                })
                
                
            });
               
            },
            error: function(jqXHR, textStatus, errorThrown) {
                // Función que se ejecutará si hay algún error en la petición
                console.error("Error en la petición:", textStatus, errorThrown);
            }
        });
      
           
        $("body").append(contenidoModal);

        
        $("#miModal").modal("show");
    }
   
    $(document).on("click", "#btnepps", showepps);
    function showvh(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex, 0).data();


        $.ajax({
            type: "POST",
            url: "/erp/epps/list/",
            dataType: "json",
            data:{
                "id":id,
                "action":"vh"
            },
            success: function(data) {
              
                $('.modal-body').html(
                    ` <form method="POST" action="." enctype="multipart/form-data" id="myForm">
                        <input type="hidden" value="${data.action}" readonly="true" id="action" name="action" />
                        <div class="mt-1 mr-3">
                            <label class="form-label">ID: </label><input class="form-control ml-3" value="${id}" readonly="true" id="id" name="id"/>
                        </div>
                        <div class="mt-1 mr-3">
                            <label class="form-label">MARCA: </label><input  class="form-control ml-3" value="${data.marca}" id="marca" name="marca" />
                        </div>
                        <div class="mt-1 mr-3">
                            <label class="form-label">MODELO: </label><input  class="form-control ml-3" value="${data.modelo}" id="modelo" name="modelo"/>
                        </div>
                        <div class="mt-1 mr-3">
                            <label class="form-label">PLACA: </label><input  class="form-control ml-3" value="${data.placa}" id="placa" name="placa" />
                        </div>
                        <div class="mt-1 mr-3">
                            <label class="form-label">FV-SOAT: </label><input  class="form-control ml-3" value="${data.fv_soat}" id="fv_soat" name="fv_soat"  />
                        </div>
                    <form>
                    `
                );
                
               $("#btnsumbit").on("click", function() {
                var date = $("#myForm").serialize()
                var datos = date;
                $.ajax({
                    type : "POST",
                    url : ".",
                    dataType : "json",
                    data:datos,
                    success:function(data){
                        window.location.href = "."
                    },
                    error:function(jqXHR,textStatus,errorThrown){
                        console.log("Error en la peticion:",textStatus,errorThrown)
                    }
                })
                
                
            });
               
            },
            error: function(jqXHR, textStatus, errorThrown) {
               
                console.error("Error en la petición:", textStatus, errorThrown);
            }
        });
      
            // Agrega el contenido del modal al cuerpo de la página
            $("body").append(contenidoModal);
    
            // Activa el modal utilizando la función modal() de Bootstrap
            $("#miModal").modal("show");
    }
   
    $(document).on("click", "#btnvh", showvh);
   
    function showepv(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex, 0).data();


        $.ajax({
            type: "POST",
            url: "/erp/epps/list/",
            dataType: "json",
            data:{
                "id":id,
                "action":"vheps"
            },
            success: function(data) {
              
                $('.modal-body').html(
                    ` <form method="POST" action="." enctype="multipart/form-data" id="myForm">
                        <input type="hidden" value="${data.action}" readonly="true" id="action" name="action" />
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">ID: </label><input class="form-control ml-3" value="${id}" readonly="true" id="id" name="id"/>
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">BOTIQUIN: </label><input type="checkbox" class="form-control ml-3" ${data.botiquin? 'checked':''} id="botiquin" name="botiquin" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">EXTINTOR: </label><input type="checkbox" class="form-control ml-3" ${data.extintor? 'checked':''} id="extintor" name="extintor"/>
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">TRIANGULO: </label><input type="checkbox" class="form-control ml-3" ${data.triangulo_s? 'checked':''} id="triangulo_s" name="triangulo_s" />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">CONO: </label><input type="checkbox" class="form-control ml-3" ${data.cono_s? 'checked':''} id="cono_s" name="cono_s"  />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">TACO: </label><input type="checkbox" class="form-control ml-3" ${data.taco? 'checked':''} id="taco" name="taco"  />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">CIRCULINA: </label><input type="checkbox" class="form-control ml-3" ${data.circulina? 'checked':''} id="circulina" name="circulina"  />
                        </div>
                        <div class="d-flex justify-content-around mt-1">
                            <label class="form-label" style="width:50px;">PERTIGA: </label><input type="checkbox" class="form-control ml-3" ${data.pertiga? 'checked':''} id="pertiga" name="pertiga"  />
                        </div>
                    <form>
                    `
                );
                
               $("#btnsumbit").on("click", function() {
               
                var datos =  {
                    "id": $("#id").val(),
                    "action": $("#action").val(),
                    "botiquin": $("#botiquin").prop("checked") ? 1 : 0,
                    "extintor": $("#extintor").prop("checked") ? 1 : 0,
                    "triangulo_s": $("#triangulo_s").prop("checked") ? 1 : 0,
                    "cono_s": $("#cono_s").prop("checked") ? 1 : 0,
                    "taco": $("#taco").prop("checked") ? 1 : 0,
                    "circulina": $("#circulina").prop("checked") ? 1 : 0,
                    "pertiga": $("#pertiga").prop("checked") ? 1 : 0,
                };
                $.ajax({
                    type : "POST",
                    url : ".",
                    dataType : "json",
                    data:datos,
                    success:function(data){
                        window.location.href = "."
                    },
                    error:function(jqXHR,textStatus,errorThrown){
                        console.log("Error en la peticion:",textStatus,errorThrown)
                    }
                })
                
                
            });
               
            },
            error: function(jqXHR, textStatus, errorThrown) {
               
                console.error("Error en la petición:", textStatus, errorThrown);
            }
        });
      
            // Agrega el contenido del modal al cuerpo de la página
            $("body").append(contenidoModal);
    
            // Activa el modal utilizando la función modal() de Bootstrap
            $("#miModal").modal("show");
    }
   
    $(document).on("click", "#btnepv", showepv);
   
});
