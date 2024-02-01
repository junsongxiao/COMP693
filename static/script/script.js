// toggle sidebar width function 

$("#menu-toggle").click(function (e) {
   e.preventDefault();
   $("#wrapper").toggleClass("toggled");
});
$("#menu-toggle-2").click(function(e) {
   e.preventDefault();
   $("#wrapper").toggleClass("toggled-2");
   $('#menu ul').hide();
});

function initMenu() {
   $('#menu ul').hide();
   $('#menu ul').children('.current').parent().show();
   // $('#menu ul:first').show();
   $('#menu li a').click(
      function() {
         var checkElement = $(this).next();
         if ((checkElement.is('ul')) && (checkElement.is(':visible'))) {
            return false;
         }
         if ((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
            $('#menu ul:visible').slideUp('normal');
            checkElement.slideDown('normal');
            return false;
         }
      }
   );
}

$(document).ready(function() {
   initMenu();
});

//toggle flash message modal

    $(document).ready(function(){

 
        // Close modal on button click
        $(".close").click(function(){
            $("#alertmsg").modal('hide');
        });
    });

    document.addEventListener("DOMContentLoaded", function() {
        let closeAlertButtons = document.querySelectorAll("#alertmsg .alert .close");
        for (let i = 0; i < closeAlertButtons.length; i++) {
            closeAlertButtons[i].addEventListener("click", function() {
                this.parentElement.style.display = "none";
            });
        }
    });

    // //toggle seats function
    // function toggleSeat(seat) {
    //     if(seat.classList.contains("available")) {
    //         seat.classList.remove("available");
    //         seat.classList.add("selected");
    //     } else if(seat.classList.contains("selected")) {
    //         seat.classList.remove("selected");
    //         seat.classList.add("available");
    //     }
    //     // Update hidden input fields for form submission
    //     let selectedSeatsInput = document.getElementById("selected_seats");
    //     let selectedSeats = document.querySelectorAll(".selected");
    //     selectedSeatsInput.value = Array.from(selectedSeats).map(s => s.dataset.seatId).join(",");
    // }
    
    // $(document).ready(function() {
        
    // });
    
 



    // // JavaScript for handling modals
    // document.addEventListener('DOMContentLoaded', (event) => {
    //     // Handle opening modals
    //     document.querySelectorAll('.inquiry-btn').forEach(button => {
    //         button.onclick = () => {
    //             const modalId = 'modal' + button.id.replace('btn', '');
    //             document.getElementById(modalId).style.display = 'block';
    //         };
    //     });

    //     // Handle closing modals
    //     document.querySelectorAll('.close').forEach(span => {
    //         span.onclick = () => {
    //             const modalId = 'modal' + span.dataset.modal;
    //             document.getElementById(modalId).style.display = 'none';
    //         };
    //     });

    //     // Close modal when clicking outside
    //     window.onclick = event => {
    //         if (event.target.classList.contains('modal')) {
    //             event.target.style.display = 'none';
    //         }
    //     };
    // });
    document.addEventListener('DOMContentLoaded', (event) => {
        // Handle opening modals
        document.querySelectorAll('.modal-btn').forEach(button => {
            button.onclick = () => {
                const modalId = button.id.replace('Btn', 'Modal');
                document.getElementById(modalId).style.display = 'block';
            };
        });
    
        // Handle closing modals
        document.querySelectorAll('.close').forEach(span => {
            span.onclick = () => {
                const modalId = span.dataset.modalId;
                document.getElementById(modalId).style.display = 'none';
            };
        });
    
        // Close modal when clicking outside
        window.onclick = event => {
            if (event.target.classList.contains('modal')) {
                event.target.style.display = 'none';
            }
        };
    });
    