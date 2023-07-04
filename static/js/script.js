
document.addEventListener('DOMContentLoaded', function() {
  // Initialization of sidenav
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // Initialization of collapsible view of showtimes
  let showtimes = document.querySelectorAll('.collapsible');
  M.Collapsible.init(showtimes);

  // Initialization of dropdown list for number of tickets to book
  let tickets = document.querySelectorAll('select');
  M.FormSelect.init(tickets);
});
