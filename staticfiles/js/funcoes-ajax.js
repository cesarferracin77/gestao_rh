function utilizouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
            $("[name='utilizada']").attr({'checked':'checked'});

            $("#btn-recuperar-he").attr( "hidden", false);
            $("#btn-utilizar-he").attr( "hidden", true);
        }
    });

}

function recuperouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/recuperou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
            $("[name='utilizada']").attr( "checked", false);
            $("#btn-recuperar-he").attr( "hidden", true);
            $("#btn-utilizar-he").attr( "hidden", false);

        }
    });

}