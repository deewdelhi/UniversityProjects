$(document).ready(function () {
  $("table").on("click", ".btnDelete", function () {
    var result = confirm("are you sure??");
    if (result) {
      let id = $(this).closest("tr")[0].cells[0].innerText;
      $.post("delete.php", { id: id });
      $(this).closest("tr").remove();
      alert("SUCCESS!");
    }
  });

  $("table").on("click", ".btnUpdate", function () {
    let tableId = $(this).closest("tr")[0].cells[0].innerText;
    let tableTitle = $(this).closest("tr")[0].cells[1].innerText;
    let tableFileType = $(this).closest("tr")[0].cells[2].innerText;
    let tableGenre = $(this).closest("tr")[0].cells[3].innerText;
    let tablePath = $(this).closest("tr")[0].cells[4].innerText;

    $(".update_form #id").val(tableId);
    $(".update_form #title").val(tableTitle);
    $(".update_form #formatType").val(tableFileType);
    $(".update_form #genre").val(tableGenre);
    $(".update_form #path").val(tablePath);
    if ($(".update_form").css("display") === "none")
      $(".update_form").css("display", "inline");
    else $(".update_form").css("display", "none");
  });
});
