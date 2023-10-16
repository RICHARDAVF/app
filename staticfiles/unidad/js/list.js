$(function(){
   var table = new DataTable('#data',{
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json',
        },

        dom:'Qlfrtip',
        initComplete: function (settings, json) {
           
            new $.fn.dataTable.Buttons(table, {
                buttons: [
                    {
                        text:'<i class="fas fa-plus"></i>Nuevo registro',
                        action:function(e,dt,node,conf){
                            window.location.href = '/erp/unidad/add/'
                        }
                    },
                    'copy', 'excel', 'csv', 'pdf', 'print'
                ],
                
                dom: {
                    button: {
                        className: 'btn btn-primary'
                    }
                }
            });

            // Crear un contenedor para los botones de exportación
            var $exportButtonsContainer = $('<div class="export-buttons-container"></div>');
            table.buttons().container().appendTo($exportButtonsContainer);

            // Agregar el contenedor de botones antes del input de búsqueda
            $exportButtonsContainer.insertBefore($('#data_wrapper .dataTables_filter'));
        }
    })
})