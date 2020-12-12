$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-class .modal-content").html("");
          $("#modal-class").modal("show");
        },
        success: function (data) {
          $("#modal-class .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#book-table tbody").html(data.html_class_list);
            $("#modal-class").modal("hide");
          }
          else {
            $("#modal-class .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create book
    $(".js-create-class").click(loadForm);
    $("#modal-class").on("submit", ".js-class-create-form", saveForm);
  
    // Update book
    $("#book-table").on("click", ".js-update-class", loadForm);
    $("#modal-class").on("submit", ".js-class-update-form", saveForm);
  
    // Delete book
    $("#book-table").on("click", ".js-delete-class", loadForm);
    $("#modal-class").on("submit", ".js-class-delete-form", saveForm);
  
  });
  