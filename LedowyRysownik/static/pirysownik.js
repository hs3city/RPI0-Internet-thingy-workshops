$( document ).ready(function(){
    //
    // W momencie załadowania strony zablokuj wszystkie przyciski
    //
    $('input').attr("disabled", true);
    //
    // Spraw, ze wcisniecie jakiegokolwiek przycisku spowoduje natychmiastowe
    // wyslanie informacji do serwera
    //
    $('input').on('change',function(event){
          //
          // Wszystkie piksele maja identyfikator w postaci "pointY_X", wiec
          // aby pobrac wspolzedne piksela nalezy:
          // 1. pobrac identyfikator ( id )
          // 2. Uciac pierwsze piec znakow ( "point" )
          // 3. Uzyskany ciag znakow podzielic w miejscu wustepowania podkreslnika "_"
          //
          pixel_position = event.target.getAttribute('id').substring(5,10).split('_')
          y = parseInt(pixel_position[0])
          x = parseInt(pixel_position[1])
          //
          // Teraz zobaczmy czy piksel zostal zapalony, czy zgaszony i w
          // zaleznosci od tegu ustawmy wysylana do serwera wartosc
          //
          if(event.target.checked){
            val=255
          } else {
            val=0
          }
          //
          // teraz stwozmy dane, ktore poleca do serwera
          //
          data = [x,y,val]
          $.ajax(
           {
                url: "/",
                type: "POST",
                data: JSON.stringify(data),
                dataType: 'json',
                async: false,
            }
        ).always(function(msg) {
                    //
                    // Gdy dane zostana wyslane do serwera - odswiez strone
                    //
                    location.reload();
                });
    });
});

//
// Mechanizm zegarka kontrolujacego moment odblokowania przyciskow na stronie
//
date = new Date()
LOCK_TIMEOUT = 10000
unlock_time = date.getTime() + LOCK_TIMEOUT
unlock_interval = setInterval(function(){
        date = new Date()
        if(date.getTime() - unlock_time > 0) {
            //
            // Pobierz i wyswietl aktualny stan wyswietlacza, a nastepnie
            // odblokuj mozliwosc rysowania.
            //
            $.getJSON('matrix_state.json', function(matrix_state){
                row = 0
                column = 0
                for(var row = 0; row<8; row++){
                    for(var column=0; column<16; column++){
                        if(matrix_state[row][column] != 0){
                            pixel_id="#point" + row.toString() + "_" + column.toString()
                            $(pixel_id).prop("checked", true);
                        }
                    }
                }
                $('input').attr("disabled", false);
                $('#message').text("Umieść swój piksel!")
                clearInterval(unlock_interval)
            })
        }
        else {
            //
            // zaktualizuj zegarek dliczajacy czas do odblokowania strony
            //
            $('#timeout').text(Math.round((unlock_time - date.getTime())/1000))
        }
    },
    100
);

