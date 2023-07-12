
/* All code in this file is taken from Materializecss.com and altered to fit this project. */
document.addEventListener('DOMContentLoaded', function() {
  // Initialization of sidenav. (https://materializecss.com/sidenav.html)
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // Initialization of collapsible view of showtimes. (https://materializecss.com/collapsible.html)
  let showtimes = document.querySelectorAll('.collapsible');
  M.Collapsible.init(showtimes);

  // Initialization of dropdown list for number of tickets to book. (https://materializecss.com/select.html)
  let tickets = document.querySelectorAll('select');
  M.FormSelect.init(tickets);
});
