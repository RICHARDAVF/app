
$(function(){
    var table = new DataTable('#data',{
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json',
        },
        responsive:true,
        autoWidth:false,
        destroy:true,
        deferRender:true,
        dom:'Qfrtip',
        "order": [[0, 'desc']],
        lengthMenu: [
            [ 10, 25, 50, -1 ],
            [ '10 filas', '25 filas', '50 filas', 'Todo' ]
        ],
        dom:"Qfrtip",
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
        ajax:{
            url:window.location.pathname,
            type:'POST',
            data:{
                "action":"searchdata",
            },
            dataSrc:''
        },
        columns:[
            {"data":"id"},
            {"data":"documento"},
            {"data":"nombres"},
            {"data":"fecha"},
            {"data":"hora_ingreso"},
            {"data":"hora_salida"},
            {"data":"placa"},
            {"data":"n_parqueo"},
            {"data":"motivo"},
            {"data":"id"},
           
        ],
        columnDefs:[
            {
                targets:[2],
                class:'rext-center',
                render:function(date,type,row){
                    
                    return `<div style="width:250px;">${date}</div>`;
                }
            },
            {
                targets:[3],
                class:'rext-center',
                render:function(date,type,row){
                    
                    return `<div style="width:100px;">${date}</div>`;
                }
            },
            {
                targets:[5],
                class:'rext-center',
                render:function(date,type,row){
                    var hora_salida  = date
                    if(hora_salida==null){
                        hora_salida = `<button class="btn btn-secondary btn-sm" id="hora_salida">MARCAR</button>`
                    }
                    return hora_salida;
                }
            },
            {
                targets:[-1],
                class:'rext-center',
                render:function(date,type,row){
                    if(row.hora_salida==null){

                        var buttons = '<div class="d-flex justify-content-center"><a href="/erp/ingsal/edit/' + row.id + '/" class="btn btn-warning btn-sm btn-flat"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="/erp/ingsal/delete/' + row.id + '/" type="button" class="btn btn-danger btn-sm btn-flat"><i class="fas fa-trash-alt"></i></a></row>';
                        return buttons;
                    }
                    return '-------'
                }
            },
        ],
        initComplete:function(settings,json){
            new $.fn.dataTable.Buttons(table,{
                buttons:[
                    {
                        text:'<i class="fas fa-plus"></i>Nuevo registro',
                        action:function(e,dt,node,conf){
                            window.location.href = '/erp/ingsal/add/'
                        }
                    },
                    'copy','excel',"csv","pdf",'pageLength'
                ],
                
            });
            var $exportButtonsContainer = $('<div class="export-buttons-container"></div>');
            table.buttons().container().appendTo($exportButtonsContainer);

            // Agregar el contenedor de botones antes del input de búsqueda
            $exportButtonsContainer.insertBefore($('#data_wrapper .dataTables_filter'));
            var desde = $('<label for="desde" class="ml-1">Desde </label><input id="desde" name="desde" type="date" class="form-control form-control-sm" style="height:30px;" />')
            var hasta = $('<label for="desde" class="ml-1">Hasta </label><input id="hasta" name="hasta" type="date" class="form-control form-control-sm" style="height:30px;" />')
            $('#data_filter').append(desde)
            $('#data_filter').append(hasta)
        
           
        }
    });

    $(document).on('click','#hora_salida',function(){
        var rowIndex = table.row($(this).closest('tr')).index();
        var id = table.cell(rowIndex,0).data();
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
                            type:'POST',
                            url:window.location.pathname,
                            dataType:'json',
                            data:{
                                "id":id,
                                "action":"confirm_hora_salida",
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
    $(document).on('change','#hasta', function() {
        aplicarFiltro();
    });

    function aplicarFiltro() {
        var fechaInicio = $('#desde').val();
        var fechaFin = $('#hasta').val();
        if (fechaInicio !== '' && fechaFin !== '') {
            $.fn.dataTable.ext.search.push(
                function(settings, data, dataIndex) {
              
                    var fechaRegistro = data[3]; 
                    var fechaInicio = $('#desde').val();
                    var fechaFin = $('#hasta').val();
                    
                    if (fechaInicio !== '' && fechaFin !== '') {
                        return (fechaRegistro >= fechaInicio && fechaRegistro <= fechaFin);
                    }
                    return true
                }
            );
            table.draw();
        }else{
            table.search('').columns().search('').draw();
        }
    }

})