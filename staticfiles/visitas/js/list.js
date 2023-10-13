$(function () {
    var miTabla = new DataTable('#data',{
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json',
        },
        responsive: false,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        scrollX:true,
        dom:'Qlfrtip',
        fixedColumns:{
            left:3,
            // right:2
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
            {"data": "id"},//0
            {"data": "estado"},//1
            {"data": "names"},//2
            {"data": "h_inicio"},//3
            {"data": "h_termino"},//4
            {"data":"h_llegada"},//5
            {"data": "h_salida"},//6
            {"data": "fecha"},//7
            {"data": "dni"},//8
            {"data": "id"},//9
            {"data": "empresa"},//10
            {"data": "cargo"},//11
            {'data': "motivo"},//12
            {'data': "sala"},//13
            {'data': "sctr_salud"},//14
            {'data': "p_visita"},//15
            {'data': "id"},//16
            {'data': "id"},//17
        ],
        columnDefs:[
            {
                targets:[1],
                class:'text-center',
                render:function(data,type,row){
                    var opt = ''
                    if(row.estado==1){
                        opt = `<div style="width:150px;display: flex; align-items: center; height: 50px;">
                        <strong class="bg-success" style="font-size:11px;border-radius:5px; padding:5px;">PROGRAMADO</strong>
                        <input class="btn btn-danger btn-sm" id="anular" type="button" value="ANULAR" style="font-size:11px;border-radius:5px; padding:5px;"/>
                    </div>`
                    }else if(row.estado==2){
                       
                        opt = `<div style="width:150px;display: flex; align-items: center; height: 50px;">
                                    <strong class="bg-success" style="font-size:11px;border-radius:5px; padding:5px;">EN CURSO</strong>
                                    <input class="btn btn-danger btn-sm" id="hora_final" type="button" value="FINALIZAR" style="font-size:11px;border-radius:5px; padding:5px;"/>
                                </div>
                                `
                    }else if(row.estado==3){
                        opt='<strong class="bg-success" style="font-size:11px;border-radius:5px; padding:5px;">FINALIZADO</strong>'
                    }else{
                        opt = '<strong class="bg-danger" style="font-size:11px;border-radius:5px; padding:5px;">ANULADO</strong>'
                    }
                   
                    return opt
                }
            },
            {
               
                class:'text-center',
                targets:[2],
                render:function(data,type,row){
                    return '<div style="width:250px;font-size:12px; font-weight: bold;">'+row.names+'</div>'
                }
            },
            {
                targets:[5],
                class:'text-center',
                render:function(data,type,row){
                    var hora = '<input type="button" value="Confirmar" id="hora_llegada" class="form-control form-control-xs btn btn-secondary">'
                    if(row.h_llegada!==null){
                        hora = '<strong style="font-weight:bold;">'+row.h_llegada+'</strong>'
                    }
                    return hora
                }
            },
           
            {
                targets:[6],
                class:'text-center',
                render:function(data,type,row){
                    if(row.h_salida===null){
                        return '<input class="btn btn-secondary" value="MARCAR" type="button" id="h_salida"/>'
                    }
                    return row.h_salida
                }
            },
             {
                targets:[7],
                class:'text-center',
                render:function(data,type,row){
                    return `<div style="width:110px;">${row.fecha}</div>`
                }
            },
            {
               
                class:'text-center',
                targets:[9],
                render:function(data,type,row){
                   var date = (row.tipo==1)?`<input type='button' id='btnaddperson' class='btn btn-success' value='Asistente.'/>`:'';
                    return date
                }
            },
            {
               
                class:'text-center',
                targets:[10],
                render:function(data,type,row){
                    var cargo = (row.cargo!=null)?row.cargo:"";
                    return '<div style="width:200px;"><strong style="width:font-size:13px;">'+cargo+'</strong></div>'
                }
            },
            {
               
                class:'text-center',
                targets:[11],
                render:function(data,type,row){
                    return '<div style="width:200px;"><strong style="width:font-size:13px;">'+row.empresa+'</strong></div>'
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
                targets:[-3],
                class:'text-center',
                render:function(data,type,row){
                    return `<div style="width:150px; font-weight: bold;font-size:12px;">${row.p_visita}</div>`
                }
            },
            {
                targets:[-3],
                class:'text-center',
                render:function(data,type,row){
                    return '<input type="button" class="btn btn-warning" value="info." id="addvehiculo"/>'
                }
            },
            {
                targets:[-1],
                class:'text-center',
                render:function(data,type,row){
                    var buttons = '<div class="d-flex justify-content-center"><a href="/erp/visita/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/visita/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a></row>';
                    return buttons;
                }
            },
            

        ],
        createdRow: function (row, data, dataIndex) {
            
            if (data.estado==0) {
                $(row).css('background-color','#f58d8d'); 
               
            }
        },
        initComplete: function (settings, json) {
          
            new $.fn.dataTable.Buttons(miTabla, {
                buttons: [
                    {
                        text:"<i class='fas fa-plus'></i> VISITA",
                        action:function ( e, dt, node, conf ) {
                            window.location.href = '/erp/visita/create/';
                        }
                    },
                    {
                        text:"<i class='fas fa-plus'></i> DELIVERY",
                        action:function ( e, dt, node, conf ) {
                            window.location.href = '/erp/delivery/create/';
                        }
                    },
                    'copy',
                    'excel',
                    'csv',
                    {
                        extend: "pdf",
                        text: 'pdf',
                        orientation: "landscape", 
                        pageSize: "LEGAL", 
                        exportOptions: {
                          columns: ':visible',
                        }
                    },
                    'print',
                    
                ],
               
                dom: {
                    button: {
                        className: 'btn btn-primary'
                    }
                }
            });

           
            var $exportButtonsContainer = $('<div class="export-buttons-container"></div>');
            miTabla.buttons().container().appendTo($exportButtonsContainer);

           
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
                                <button type="button" class="btn btn-danger" data-dismiss="modal">CERRAR</button>
                            </div>
                        </div>
                    </div>
                </div>
    
                    `)};
    var datos = []
    var parqueos = []
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
            <td>
            <p>
                <a href="${datos[item].sctr}" target="_blank">file</a></>
            </td>
            <td>${(datos[item].n_parqueo===null)?'':datos[item].n_parqueo}</td>
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
        datos = []
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
                
                datos = data.asis
                parqueos = data.parking
                var opt_select = '<select name="n_parqueo"  class="form-control ml-3"  id="n_parqueo">'
                for(var item of parqueos){
                    opt_select+=`
                    <option value="${item.id}" class="form-control">${item.numero}</option>
                `
                }
                opt_select+= "</select>"
               
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
                            <label class="form-label">SCTR: </label><input  class="form-control ml-3" type='file'  id="sctr" name="sctr" />
                            <label class="form-label ml-1">N° Parqueo: </label>${opt_select}
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
                                    <th style='width:100'>SCTR</th>
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
   
    $(document).on('click', '#addperson', function () {
        var datas = {}
        var formData = new FormData($('#myForm')[0]);
        formData.append('action', 'addperson');
        for (var pair of formData.entries()) {
           datas[pair[0]]=pair[1]
        }
        datos.push(datas)
        $.ajax({
            type: 'POST',
            url: '/erp/visita/asis/add/',
            dataType: 'json',
            data: formData,
            processData: false, 
            contentType: false,
            success: function (data) {
               
            },
            error: function (data) {
                alert(data.error);
            }
        });
    
        listdates();
    });
    
    $(document).on('input','#documento',function(event){
        const doc = $('#documento').val();
        $('#nombre').val('')
        $('#apellidos').val('')
        if (doc.trim().length==8){
            $.ajax({
                type:'POST',
                url:'/erp/visita/create/',
                dataType:'json',
                data:{
                    action:'searchdni',
                    dni:doc.trim(),
                },
                success:function(data){
                    if(data.error){
                        $('#nombre').val('')
                        $('#apellidos').val('')
                        return alert(data.error);
                    }
                
                    $('#nombre').val(`${data.data.nombres}`)
                    $('#apellidos').val(`${data.data.apellido_paterno} ${data.data.apellido_materno}`)
                   
                },
                error:function(data){
                    $('#nombre').val('')
                    $('#apellidos').val('')
                    alert(data.error)
                }
    
            })
        }
        
    })
    $(document).on('click',"#hora_llegada",function(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex,0).data();
        $.confirm({
            theme: 'material',
            title: 'Alerta',
            icon: 'fas fa-info',
            content: "¿Esta seguro de marcar la hora de llegada?",
            columnClass: 'small',
            typeAnimated: true,
            cancelButtonClass: 'btn-primary',
            draggable: true,
            dragWindowBorder: false,
            buttons:{
                info:{
                    text:'Si',
                    btnClass:'btn-primary',
                    action:function(){
                        $.ajax({
                            type:'POST',
                            url:window.location.pathname,
                            dataType:'json',
                            data:{
                                "id":id,
                                "action":"confirm",
                            },
                            success:function(data){
                                window.location.reload()
                                if(data.error){
                                    return alert(data.error)
                                }
                              
                            },
                            error:function(){
                                alert("Hubo un error en la peticion")
                            }
                        })
                    }
                },
                danger:{
                    text:'No',
                    btnClass:'btn-red',
                    action:function(){

                    }
                }
            }
        })
        
    })
    $(document).on('click',"#hora_final",function(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex,0).data();
        $.confirm({
            theme: 'material',
            title: 'Alerta',
            icon: 'fas fa-info',
            content: "¿Esta seguro de marcar la hora final?",
            columnClass: 'small',
            typeAnimated: true,
            cancelButtonClass: 'btn-primary',
            draggable: true,
            dragWindowBorder: false,
            buttons:{
                info:{
                    text:'Si',
                    btnClass:'btn-primary',
                    action:function(){
                        $.ajax({
                            type:'POST',
                            url:window.location.pathname,
                            dataType:'json',
                            data:{
                                "id":id,
                                "action":"h_final",
                            },
                            success:function(data){
                                window.location.reload()
                                if(data.error){
                                    
                                    return alert(data.error)
                                }
                            },
                            error:function(){
                                alert("Hubo un error en la peticion")
                            }
                        })
                    }
                },
                danger:{
                    text:'No',
                    btnClass:'btn-red',
                    action:function(){

                    }
                }
            }
        })
       
    })
    $(document).on("click","#addvehiculo",function(){
        $('body').append(contenidoModal);
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex,0).data();
        $.ajax({
            type:'POST',
            url:window.location.pathname,
            dataType:'json',
            data:{
                "id":id,
                "action":"addvh"
            },
            success:function(data){
              
                if(data.error){
                    return alert(data.error)
                }
                var opt = '<select class="form-control" id="num_park">'
                if(data.vh.n_parqueo==null){
                    opt+=`<option value="">-------</option>`
                    for(let item of  data.parking){
                        opt+=`<option value="${item.id}">${item.numero}</option>`
                    }
                }else{
                    opt+=`<option>${data.vh.n_parqueo}</option>`
                }
                
                opt+="</select>"
                $('.modal-body').html(
                    ` <form  enctype="multipart/form-data" id="FormVH">
                        <input type='hidden' class="form-control ml-3" value="${id}" editable='false' id="id" name="id"/>
                        <div class="mt-1">
                            <div class="d-flex">
                                <label class="form-label">MARCA: </label><input class="form-control ml-4" ${(data.vh.v_marca!==null)?'value="'+data.vh.v_marca+'"':''}  id="v_marca" name="v_marca"/>
                            </div>
                            <div class="d-flex mt-2">
                                <label class="form-label">MODELO: </label><input  class="form-control ml-4 " ${(data.vh.v_modelo!==null)?'value="'+data.vh.v_modelo+'"':''}  id="v_modelo" name="v_modelo"/>
                            </div>
                            <div class="d-flex mt-2">
                                <label class="form-label">Placa: </label><input  class="form-control ml-4 " ${(data.vh.v_placa!==null)?'value="'+data.vh.v_placa+'"':''} id="v_placa" name="v_placa" />
                            </div>
                            <div class="d-flex mt-2">
                                <label class="form-label">FV-SOAT: </label><input  class="form-control ml-4 " ${(data.vh.fv_soat!=='None')?'value="'+data.vh.fv_soat+'"':''} id="fv_soat" name="fv_soat" type="date" />
                            </div>
                            <div class="d-flex mt-2">
                                <label class="form-label ml-1">N° Parqueo: </label>
                                ${opt}
                            </div>
                            <div class="d-flex mt-2">
                                <label class="form-label">Obervacion: </label><input  class="form-control ml-4 " ${(data.vh.observacion!==null)?'value="'+data.vh.observacion+'"':''} id="observacion" name="observacion" />
                            </div>
                        </div>
                        <input type="button" class="btn btn-success" value="GUARDAR" id="formvh"/>
                    <form>`
                )
                $('#miModal').modal('show')
            },
            error:function(){
                alert("Ocurrio un error")
            }
        })
        
    })
    $(document).on("click","#h_salida",function(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex,0).data();
        $.confirm({
            theme: 'material',
            title: 'Alerta',
            icon: 'fas fa-info',
            content: "¿Esta seguro de marcar la hora de salida?",
            columnClass: 'small',
            typeAnimated: true,
            cancelButtonClass: 'btn-primary',
            draggable: true,
            dragWindowBorder: false,
            buttons:{
                info:{
                    text:'Si',
                    btnClass:'btn-primary',
                    action:function(){
                        $.ajax({
                            type:"POST",
                            url:window.location.pathname,
                            dataType:'json',
                            data:{
                                "id":id,
                                "action":"h_salida"
                            },
                            success:function(data){
                                window.location.reload()
                            },
                            error:function(jqXHR, textStatus, errorThrown){
                                alert("Error en la solicitud "+textStatus,errorThrown)
                            }
                        })
                    }
                },
                danger:{
                    text:'No',
                    btnClass:'btn-red',
                    action:function(){

                    }
                }
            }
        })
       
    })
    $(document).on("click","#anular",function(){
        var rowIndex = miTabla.row($(this).closest('tr')).index();
        var id = miTabla.cell(rowIndex,0).data();
        $.confirm({
            theme: 'material',
            title: 'Alerta',
            icon: 'fas fa-info',
            content: "¿Esta seguro de anular?",
            columnClass: 'small',
            typeAnimated: true,
            cancelButtonClass: 'btn-primary',
            draggable: true,
            dragWindowBorder: false,
            buttons:{
                info:{
                    text:'Si',
                    btnClass:'btn-primary',
                    action:function(){
                        $.ajax({
                            type:'POST',
                            url : window.location.pathname,
                            dataType:'json',
                            data:{
                                "id":id,
                                "action":'anular'
                            },
                            success:function(data){
                                if(data.error){
                                    return alert(data.error)
                                }
                                window.location.reload()
                            },
                            error:function(jqXHR, textStatus, errorThrown){
                                        alert("Error en la solicitud "+textStatus,errorThrown)
                                    }
                        })
                    }
                },
                danger:{
                    text:'No',
                    btnClass:'btn-red',
                    action:function(){

                    }
                }
            }
        })
    })
    $(document).on('click','#formvh',function(){
        const formData = new FormData($('#FormVH')[0])
        formData.append('action', 'formvh');
        formData.append('n_parqueo',$('#num_park').val() );
        
        $.ajax({
            type:'POST',
            dataType:'json',
            url:window.location.pathname,
            data:formData,
            processData: false, 
            contentType: false,
            success:function(data){
                if(data.error){
                    return alert(data.error)
                }
                window.location.reload()
            },
            error:function(jqXHR, textStatus, errorThrown){
                alert("Ocurrio un error ",textStatus,errorThrown)
                window.location.reload()
            }
        })
    })
});

