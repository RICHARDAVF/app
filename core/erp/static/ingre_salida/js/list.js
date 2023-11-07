$(function(){
    var miTabla = new DataTable('#data',{
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json',
        },
        responsive:true,
        autoWidth:false,
        destroy:true,
        deferRender:true,
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
            {"data":"tipo"},
            {"data":"fecha"},
            {"data":"hora"},
            {"data":"motivo"},
            {"data":"id"},
           
        ],
        columnDefs:[
            {
                targets:[3],
                class:'text-center',
                render:function(data,type,row){
                    var opt = '<strong class="bg-success" style="font-size:12px;border-radius:5px;padding:4px;">INGRESO</strong>'
                    if(data==2){
                        opt = '<strong class="bg-danger" style="font-size:12px;border-radius:5px;padding:4px;">SALIDA</strong>'
                    }
                    return opt
                }
            },
            {
                targets:[-1],
                class:'rext-center',
                render:function(date,type,row){
                    var buttons = '<div class="d-flex justify-content-center"><a href="/erp/ingsal/edit/' + row.id + '/" class="btn btn-warning btn-sm btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/ingsal/delete/' + row.id + '/" type="button" class="btn btn-danger btn-sm btn-flat"><i class="fas fa-trash-alt"></i></a></row>';
                    return buttons;
                }
            },
        ],
        initComplete:function(settings,json){
            new $.fn.dataTable.Buttons(miTabla,{
                buttons:[
                    // {
                    //     text:'<i class="fas fa-plus"></i>Nuevo registro',
                    //     action:function(e,dt,node,conf){
                    //         window.location.href = '/erp/ingsal/add/'
                    //     }
                    // },
                    'copy','excel',"csv","pdf",'pageLength'
                ],
                dom:{
                    button:{
                        className:'btn btn-primary'
                    }
                }
            });
            var $exportButtonsContainer = $('<div class="export-buttons-container"></div>');
            miTabla.buttons().container().appendTo($exportButtonsContainer);

            // Agregar el contenedor de botones antes del input de búsqueda
            $exportButtonsContainer.insertBefore($('#data_wrapper .dataTables_filter'));
        }
    });
})