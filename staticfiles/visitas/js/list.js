$(function () {
    var miTabla = $('#data').DataTable({
        responsive: false,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        scrollX:true,
        dom:'Qlfrtip',
        fixedColumns:{
            left:3,
            right:2
        },
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
            {"data": "estado"},
            {"data": "user"},
            {"data": "nombre"},
            {"data": "apellidos"},
            {"data": "dni"},
            {"data": "id"},
            {"data": "empresa"},
            {"data": "cargo"},
            {"data": "h_inicio"},
            {"data": "h_termino"},
            {"data": "fecha"},
            {'data': "motivo"},
            {'data': "sala"},
            {'data': "v_marca"},
            {'data': "v_modelo"},
            {'data': "v_placa"},
            {'data': "fv_soat"},
            {'data': "strc_salud"},
            {'data': "n_parqueo"},
            {'data': "id"},
        ],
        columnDefs:[
            {
                targets:[1],
                class:'text-center',
                render:function(data,type,row){
                    var estado = (row.estado==1)?'PROGRAMÓ':(row.estado==2)?'ENTRÓ':'VISITÓ'
                    return '<strong class="bg-success" style="font-size:11px;border-radius:5px">'+estado+'</strong>'
                }
            },
            {
               
                class:'text-center',
                targets:[4],
                render:function(data,type,row){
                    return '<div style="width:200px;"><strong style="width:font-size:13px;">'+row.apellidos+'</strong></div>'
                }
            },
            {
               
                class:'text-center',
                targets:[6],
                render:function(data,type,row){
                   var date = (row.tipo==1)?`<input type='button' id='btnaddperson' class='btn btn-success' value='Asistente.'/>`:'';
                    return date
                }
            },
            {
               
                class:'text-center',
                targets:[7],
                render:function(data,type,row){
                    return '<div style="width:200px;"><strong style="width:font-size:13px;">'+row.empresa+'</strong></div>'
                }
            },
            {
               
                class:'text-center',
                targets:[8],
                render:function(data,type,row){
                    var cargo = (row.cargo!=null)?row.cargo:"";
                    return '<div style="width:200px;"><strong style="width:font-size:13px;">'+cargo+'</strong></div>'
                }
            },
            {
                targets:[9],
                class:'text-center',
                render:function(data,type,row){
                    return '<div style="width:100px;"><strong>'+row.h_inicio+'</strong></div>'
                }
            },
            {
                targets:[10],
                class:'text-center',
                render:function(data,type,row){
                    var h_termino = (row.h_termino!=null)?row.h_termino:""
                    return '<div style="width:100px;"><strong>'+h_termino+'</strong></div>'
                }
            },
            {
                targets:[11],
                class:'text-center',
                render:function(data,type,row){
                   
                    return '<div style="width:100px;"><strong>'+row.fecha+'</strong></div>'
                }
            },
            {
                targets:[12],
                class:'text-center',
                render:function(data,type,row){
                    return '<div style="width:200px;"><strong style="font-size:13px;"">'+row.motivo+'</strong></div>'
                }
            },
            {
                targets:[-4],
                class:'text-center',
                render:function(data,type,row){
                    var fecha = (row.fv_soat!=null)?row.fv_soat:''
                    return '<div style="width:100px;"><strong style="font-size:13px;"">'+fecha+'</strong></div>'
                }
            },
            {
                targets:[-1],
                class:'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var url = (parseInt(row.tipo) ==1)?'/erp/visita/update/':'/erp/delivery/update/'
                    var buttons = `<div class="row d-flex justify-content-center"><a href="${url}${row.id}/"` + '" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/visita/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a></row>';
                    return buttons;
                }
            },

        ],

        initComplete: function (settings, json) {
            // Habilitar los botones de exportación
            new $.fn.dataTable.Buttons(miTabla, {
                buttons: [
                    {
                        extend:'copy',
                        text: '<i class="fas fa-copy"></i>',
                        className: 'btn btn-primary'
                    },
                    {
                        extend:'excel',
                        text: '<i class="fas fa-file-excel"></i>',
                        className:'btn btn-success'
                    },
                    {
                        extend:'csv',
                        text: '<i class="fas fa-file-csv"></i>',
                        className:'btn btn-success'
                    },
                    {
                        extend: "pdf",
                        text: '<i class="fas fa-file-pdf"></i>',
                        className:"btn btn-danger",
                        orientation: "landscape", 
                        pageSize: "LEGAL", 
                        exportOptions: {
                          columns: ':visible',
                        }
                    },
                    {
                        extend:'print',
                        text: '<i class="fas fa-print"></i>',
                        className:'btn btn-success'
                    },
                    {
                        text:"<i class='fas fa-plus'></i> DELIVERY",
                        action:function ( e, dt, node, conf ) {
                            window.location.href = '/erp/delivery/create/';
                        }
                    },
                    {
                        text:"<i class='fas fa-plus'></i> VISITA",
                        action:function ( e, dt, node, conf ) {
                            window.location.href = '/erp/visita/create/';
                        }
                    },
                ],
               
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
    $('.btnTest').css('display','none')
    const contenidoModal = ()=>{
        return (`
                <div class="modal fade bd-example-modal-lg" id="miModal" tabindex="-1" role="dialog" aria-labelledby="miModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="miModalLabel">Personas en la reunion</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                            
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-success" id="btnsubmit">GUARDAR</button>
                                <button type="button" class="btn btn-danger" data-dismiss="modal">CERRAR</button>
                            </div>
                        </div>
                    </div>
                </div>
    
                    `)};
    var datos = []
    function formatJSON(data){
        var dates = {}
        data.forEach(function(field){
            dates[field.name] = field.value;
        });
        
        return dates;
    }
    function listdates(){
        var tdhtml = ''
        for(item in datos){
          
            tdhtml+=`<tr>
            <td>${datos[item].documento}</td>
            <td>${datos[item].nombre}</td>
            <td>${datos[item].apellidos}</td>
            <td>${datos[item].empresa}</td>
            <td>${datos[item].modelo_v}</td>
            <td>${datos[item].placa_v}</td>
            <td>${datos[item].soat_v}</td>
            <td>${datos[item].strc}</td>
            <td>${datos[item].n_parqueo}</td>
            <tr>`
        }
        $('.table-group-divider').html(
            tdhtml
        )
        $('#documento').val('')
        $('#nombre').val('')
        $('#apellidos').val('')
        $('#apellido').val('')
        $('#empresa').val('')
        $('#modelo_v').val('')
        $('#placa_v').val('')
        $('#n_parqueo').val('')

    }
    function showperson(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex,0).data();
        $.ajax({
            type:"POST",
            url:window.location.pathname,
            dataType:'json',
            data:{
                "id":id,
                "action":'addperson',
            },
            success:function(data){
                datos = data
                console.log(datos)
                $('.modal-body').html(
                    ` <form  enctype="multipart/form-data" id="myForm">
                        <input type='hidden' class="form-control ml-3" value="${id}" editable='false' id="id" name="id"/>
                        <div class="mt-1  d-flex felx-row">
                            <label class="form-label ml-1">DNI: </label><input  class="form-control ml-3"  id="documento" name="documento" />
                            <label class="form-label">Nombre: </label><input class="form-control ml-3"   id="nombre" name="nombre"/>
                        </div>
                        <div class="mt-1  d-flex felx-row">
                            <label class="form-label ml-1">Apellidos: </label><input  class="form-control ml-3"  id="apellidos" name="apellidos" />
                            <label class="form-label">Empresa: </label><input  class="form-control ml-3"  id="empresa" name="empresa"/>
                        </div>
                        
                        <div class="mt-1  d-flex felx-row">
                            <label class="form-label ml-1">Marca: </label><input  class="form-control ml-3"  id="marca_v" name="marca_v"/>
                            <label class="form-label ml-1">Modelo: </label><input  class="form-control ml-3"  id="modelo_v" name="modelo_v"/>
                        </div>
                            
                        <div class="mt-1 d-flex felx-row">
                            <label class="form-label">Placa: </label><input  class="form-control ml-3"  id="placa_v" name="placa_v" />
                            <label class="form-label ml-1">FV-SOAT: </label><input  class="form-control ml-3" type='date'  id="soat_v" name="soat_v"  />
                        </div>
                        <div class="mt-1 d-flex felx-row">
                            <label class="form-label">STRC: </label><input  class="form-control ml-3" type='file'  id="strc" name="strc" />
                            <label class="form-label ml-1">N° Parqueo: </label><input  class="form-control ml-3"  id="n_parqueo" name="n_parqueo"  />
                        </div>
                    <form>
                    <a type='button' class='btn btn-primary mt-1 mb-1' id='addperson'><i class='fas fa-plus'></i>Agregar</a>
                    <div class="table-responsive">
                        <table class="table table-striped">
                            <thead class="table-light">
                                <caption>Table Name</caption>
                                <tr>
                                    <th style='width:100'>DNI</th>
                                    <th style='width:100'>NOMBRE</th>
                                    <th style='width:200'>APELLIDO</th>
                                    <th style='width:200'>EMPRESA</th>
                                    <th style='width:100'>MODELO</th>
                                    <th style='width:100'>PLACA</th>
                                    <th style='width:100'>SOAT</th>
                                    <th style='width:100'>STRC</th>
                                    <th style='width:50'>PARQUE</th>
                                </tr>
                                </thead>
                                <tbody class="table-group-divider">
                                
                                </tbody>
                                <tfoot>
                                    
                                </tfoot>
                        </table>
                    </div>


                    `
                );
                listdates();
            },
            error:function(){
                alert("Error en la peticion")
            }
        });
        $('body').append(contenidoModal);
        $("#miModal").modal('show');
    }
    
    $(document).on("click","#btnaddperson",showperson);
   
    $(document).on('click','#addperson',function(){
        var data = $('#myForm').serializeArray();
        data.push({'name':'strc',"value":$('#strc').val()})
        datos.push(formatJSON(data));
      
        listdates()
    })
    $(document).on('click','#btnsubmit',function(){
        var data = {
            id:$('id').val(),
            action:"addperson",
            items:JSON.stringify(datos),
        }
        $.ajax({
            type:'POST',
            url:'/erp/visita/asis/add/',
            dataType:'json',
            data:data,
            
            success:function(){
                datos = []
                $('#miModal').modal('hide');
            },
            error:function(){
                alert("Ocurrio un error")
            }
        });
    })
});

