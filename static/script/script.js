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
    // // });


    // // JavaScript for handling modals BACKUP START
    // document.addEventListener('DOMContentLoaded', (event) => {
    //     // Handle opening modals
    //     document.querySelectorAll('.modal-btn').forEach(button => {
    //         button.onclick = () => {
    //             const modalId = button.id.replace('Btn', 'Modal');
    //             document.getElementById(modalId).style.display = 'block';
    //         };
    //     });
    
    //     // Handle closing modals
    //     document.querySelectorAll('.close').forEach(span => {
    //         span.onclick = () => {
    //             const modalId = span.dataset.modalId;
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
    // //BACKUP END

    


    // JavaScript for handling modals BACKUP START
    // document.addEventListener('DOMContentLoaded', () => {
    //     document.querySelectorAll('.inquiry-btn').forEach(button => {
    //         button.addEventListener('click', function() {
    //             const isLoggedIn = this.getAttribute('data-logged-in') === 'true';
    //             if (!isLoggedIn) {
    //                 window.location.href = "login"; // Redirect to login
    //             } else {
    //                 const modalId = 'inquiryModal-' + this.id.split('-')[1];
    //                 const modal = document.getElementById(modalId);
    //                 if (modal) {
    //                     modal.style.display = 'block';
    //                 }
    //             }
    //         });
    //     });
    
    //     document.querySelectorAll('.close').forEach(span => {
    //         span.addEventListener('click', function() {
    //             const modalId = this.dataset.modalId;
    //             const modal = document.getElementById(modalId);
    //             if (modal) {
    //                 modal.style.display = 'none';
    //             }
    //         });
    //     });
    
    //     window.addEventListener('click', event => {
    //         if (event.target.classList.contains('modal')) {
    //             event.target.style.display = 'none';
    //         }
    //     });
    // });
//   BACKUP END
  
document.addEventListener('DOMContentLoaded', function() {
    // Correctly target buttons and assign click event
    document.querySelectorAll('.inquiry-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var isLoggedIn = this.getAttribute('data-logged-in') === 'true';
            if (isLoggedIn) {
                // Extract the numeric tour ID from button's ID
                var tourId = this.id.split('-')[1];
                // Correctly set the tour ID for the modal's form
                document.getElementById('modalTourId').value = tourId;

                // Display the modal
                var modal = document.getElementById('inquiryModal');
                modal.style.display = 'block';
            } else {
                // Redirect to login if not logged in
                window.location.href = "/login";
            }
        });
    });


// document.addEventListener('DOMContentLoaded', function() {
//     document.querySelectorAll('.inquiry-btn').forEach(function(button) {
//         button.addEventListener('click', function() {
//             var isLoggedIn = this.getAttribute('data-logged-in') === 'true';
//             var tourId = this.getAttribute('id');

//             if (isLoggedIn) {
//                 // User is logged in, open the modal and set the tour ID
//                 var modal = document.getElementById('inquiryModal');
//                 document.getElementById('modalTourId').value = tourId;
//                 modal.style.display = 'block';
//             } else {
//                 // User is not logged in, redirect to login page
//                 window.location.href = "/login";
//             }
//         });
//     });




    // Close the modal when the close button is clicked
    document.querySelector('.close').addEventListener('click', function() {
        document.getElementById('inquiryModal').style.display = 'none';
    });

    // Close the modal when clicking outside of it
    window.addEventListener('click', function(event) {
        var modal = document.getElementById('inquiryModal');
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});
 

//Quote modal control
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.quote-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var modalId = "modal-" + this.getAttribute('id').split('-')[1];
            var modal = document.getElementById(modalId);
            modal.style.display = 'block';
        });
    });

    document.querySelectorAll('.close').forEach(function(closeButton) {
        closeButton.addEventListener('click', function() {
            var modalId = "modal-" + this.getAttribute('data-modal-id');
            var modal = document.getElementById(modalId);
            modal.style.display = 'none';
        });
    });

    window.addEventListener('click', function(event) {
        document.querySelectorAll('.modal').forEach(function(modal) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    });
});
