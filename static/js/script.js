
document.addEventListener('DOMContentLoaded', function() {
  // Initialization of sidenav
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // Initialization of datepicker
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker);

  // Initialization of collapsible view of showtimes
  let showtimes = document.querySelectorAll('.collapsible');
  M.Collapsible.init(showtimes);
});
