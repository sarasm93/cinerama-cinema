
document.addEventListener('DOMContentLoaded', function() {
    // Initialization of sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

// Character counter on registration form
  $(document).ready(function() {
    $('input#input_text, textarea#textarea2').characterCounter();
  });