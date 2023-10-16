$(function(){
    var miTabla = new DataTable('#data',{
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json',
        },
        responsive:true,
        autoWidth:false,
        destroy:true,
        deferRender:true,
        scrollX:true,
        dom:"Qlfrtip",
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
            {"data":"h_entrada"},
            {"data":"h_salida"},
            {"data":"id"},
           
        ],
        columnDefs:[
            {
                targets:[-1],
                class:"text-center",
                render:function(date,type,row){
                    return "<a href='/erp/ingsal/edit/"+row.id+"/' ><i class='fas fa-edit'></i><a/>"
                }

            }
        ],
        initComplete:function(settings,json){
            new $.fn.dataTable.Buttons(miTabla,{
                buttons:[
                    {
                        text:'<i class="fas fa-plus"></i>Nuevo registro',
                        action:function(e,dt,node,conf){
                            window.location.href = '/erp/ingsal/add/'
                        }
                    },
                    'copy','excel',"csv","pdf"
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