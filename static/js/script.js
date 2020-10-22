$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $(".collapsible").collapsible();
  $(".tooltipped").tooltip();
  $(".datepicker").datepicker({
    format: "dd mmmm, yyyy",
    yearRange: [2020, 2023],
    showClearBtn: true,
    i18n: {
      done: "Select",
    },
  });
});
