$(function(){
    $('#btn-cancel').css('display','none')
})

function search_doc(){
    var doc = $(this).val()
    $('#id_nombres').val('')
    if(doc.trim().length==8){
        $.ajax({
            url:'/search_doc/',
            type:'POST',
            dataType:'json',
            data:{
                "action":'search_doc',
                "doc":doc
            },
            success:function(data){
                if(data.error){
                    return alert(data.error)
                }
                $('#id_nombres').val(data.data.nombre_completo)
            },
            error:function(){
    
            }
        })
    }
}
$(document).on('input','#id_documento',search_doc)