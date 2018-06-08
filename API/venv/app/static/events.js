
  $(function() {

    $('#email').bind('focusout', function() {
      $.getJSON($SCRIPT_ROOT + '/_envoi_ajax', {
        email: $('input[name="email"]').val()
      }, function(data) {
        if (data.mail_existe)
        {
          $("#commentaire_email").text("Cette adresse mail existe déjà");
          $("#email").addClass("erreur_champ");
        }
        else
        {
          if(email != ""){
            $("#commentaire_email").text("");
          }
          $("#email").removeClass("erreur_champ");
        }
      });
      return false;
    });

    $(".saisie_obligatoire").bind('focusout', function() {
      id= $(this).attr('id');

      if ($(this).val() == "") {                 // Tester aussi si la classe erreu_champ est déjà présente ?
        $("#commentaire_"+id).text("Saisie Obligatoire");
        $("#commentaire_"+id).addClass("commentaire_erreur");
      }
      else {
        $("#commentaire_"+id).text("");
        $("#commentaire_"+id).removeClass("commentaire_erreur");
      }
     });

     $(".champ_form.text").bind('focusout', function() {
       id= $(this).attr('id');
       mise_a_jour_champ(id,'dede')

      });

      function mise_a_jour_champ(id, value) {
        alert('hello world');
        $("#"+id).val(value);
      }

  });
