$(function(){
    $('#id_v_marca').on('input',function(event){
        $('#id_estado').val(2)
    });
    $('#id_h_termino').on('change',function(event){
        
        $('#id_estado').val(3)
    })
    function searchDNI(dni){
        const url = window.location.pathname,
        data = {dni:dni,action:'searchdni'};
        
        $.ajax({
            url:url,
            type:'POST',
            dataType:'json',
            data:data,
            success:function(result){
                if(result.error){
                    message_error(result.error)
                }else{
                    
                    const name = $('#id_nombre');
                    const last_name = $('#id_apellidos');
                    name.val(result.data.nombres)
                    last_name.val(`${result.data.apellido_paterno} ${result.data.apellido_materno}`)
                }
            },
            error:function(result){
               message_error(result.error)
            }
    
        });
       }
  

    

    const dni = $('#id_dni');
    dni.on('input',function(event){
        const value = event.target.value.trim();
        var tipo_documento = $("#id_tipo_documento").val();
        if(parseInt(tipo_documento)==1 && value.length==8){
            searchDNI(value)
        }else{
            $('#id_nombre').val('')
            $('#id_apellidos').val('')
        }
    });
      
    
    
})
