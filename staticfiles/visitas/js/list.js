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
                    return '<div style="width:200px;"><strong style="width:font-size:13px;">'+row.empresa+'</strong></div>'
                }
            },
            {
               
                class:'text-center',
                targets:[7],
                render:function(data,type,row){
                    var cargo = (row.cargo!=null)?row.cargo:"";
                    return '<div style="width:200px;"><strong style="width:font-size:13px;">'+cargo+'</strong></div>'
                }
            },
            {
                targets:[8],
                class:'text-center',
                render:function(data,type,row){
                    return '<div style="width:100px;"><strong>'+row.h_inicio+'</strong></div>'
                }
            },
            {
                targets:[9],
                class:'text-center',
                render:function(data,type,row){
                    var h_termino = (row.h_termino!=null)?row.h_termino:""
                    return '<div style="width:100px;"><strong>'+h_termino+'</strong></div>'
                }
            },
            {
                targets:[10],
                class:'text-center',
                render:function(data,type,row){
                   
                    return '<div style="width:100px;"><strong>'+row.fecha+'</strong></div>'
                }
            },
            {
                targets:[11],
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
                    console.log(url,row.tipo)
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
                        text: '<i class="fas fa-copy"></i> COPY',
                        className: 'btn btn-primary'
                    },
                    {
                        extend:'excel',
                        text: '<i class="fas fa-file-excel"></i> EXCEL',
                        className:'btn btn-success'
                    },
                    {
                        extend:'csv',
                        text: '<i class="fas fa-file-csv"></i> CSV',
                        className:'btn btn-success'
                    },
                    {
                        extend: "pdf",
                        text: '<i class="fas fa-file-pdf"></i> PDF',
                        className:"btn btn-danger",
                        orientation: "landscape", 
                        pageSize: "LEGAL", 
                        exportOptions: {
                          columns: ':visible',
                        }
                    },
                    {
                        extend:'print',
                        text: '<i class="fas fa-print"></i> PRINT',
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
                        className: 'btn btn-primary ml-3'
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
});

